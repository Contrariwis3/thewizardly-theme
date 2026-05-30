#!/usr/bin/env python3
# ABOUTME: Generates the Founding Sky starfield — real Yale BSC5 stars projected
# ABOUTME: for the All-Night Pavilion masthead, emitted as a static Hugo SVG partial.
"""Render the sky as it stood over 33.83 N, 117.92 W at 03:00 PDT on 22 Apr 2000.

Reads the Yale Bright Star Catalogue (5th ed.), computes each star's altitude and
azimuth at that instant, frames a band of sky above the horizon toward the densest
direction, maps visual magnitude to circle radius and opacity, and writes the SVG
markup the masthead partials include. Real catalogue stars only, no procedural fill
(the Named-Starfield Rule). The theme ships no runtime JS, so the sky is static SVG.

Re-run to regenerate the partial:

    python3 scripts/founding_sky.py            # auto-pick the framing azimuth
    python3 scripts/founding_sky.py --az 168   # force a compass azimuth
"""
from __future__ import annotations

import argparse
import math
import os
import random
from dataclasses import dataclass

# --- The Founding Sky: where and when --------------------------------------
OBS_LAT = 33.83                       # degrees north
OBS_LON = -117.92                     # degrees east (negative = west)
FOUNDING_INSTANT_UTC = (2000, 4, 22, 10, 0, 0)  # 03:00 PDT == 10:00 UTC

# --- Catalogue selection ----------------------------------------------------
MAG_LIMIT = 6.0       # faintest star rendered (naked-eye limit)
MAG_BRIGHT = 2.3      # at or below this, a star wears the lit halo (the anchors)

# --- Magnitude -> visual style ----------------------------------------------
# Wide dynamic range so the named anchor stars read as a pattern against the
# faint field, the way a real sky's brightest stars dominate.
RADIUS_MAX = 3.4
RADIUS_MIN = 0.5
OPACITY_MAX = 0.98
OPACITY_MIN = 0.08
MAG_BRIGHTEST = -1.5  # mapping floor; brighter than this clamps to RADIUS_MAX

# --- Framing ----------------------------------------------------------------
FOV_AZ = 130.0        # degrees of azimuth in frame
FOV_ALT = 62.0        # degrees of altitude in frame, from the horizon up
HORIZON_ALT = 0.0
VIEW_W = 1200.0       # SVG viewBox width (matches the city SVG)
VIEW_H = round(VIEW_W * FOV_ALT / FOV_AZ, 2)  # keep degrees roughly square

TWINKLE_FRACTION = 0.1
TWINKLE_SEED = 20000422  # the Founding date; deterministic cosmetic jitter


def _clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


# --- Time and sidereal angle ------------------------------------------------

def julian_date(year, month, day, hour=0, minute=0, second=0) -> float:
    """Julian Date for a Gregorian-calendar UTC instant."""
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    jdn = day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    return jdn + (hour - 12) / 24.0 + minute / 1440.0 + second / 86400.0


def gmst_degrees(jd: float) -> float:
    """Greenwich Mean Sidereal Time in degrees (USNO / Meeus eq. 12.4)."""
    d = jd - 2451545.0
    t = d / 36525.0
    g = 280.46061837 + 360.98564736629 * d + 0.000387933 * t * t - (t ** 3) / 38710000.0
    return g % 360.0


def local_sidereal_degrees(jd: float, lon_deg: float) -> float:
    return (gmst_degrees(jd) + lon_deg) % 360.0


def equatorial_to_horizontal(ra_deg, dec_deg, lat_deg, lst_deg):
    """Convert equatorial (J2000 RA/Dec) to horizontal (altitude, azimuth) in
    degrees. Azimuth is measured from North (0) increasing eastward."""
    ha = math.radians((lst_deg - ra_deg) % 360.0)
    dec = math.radians(dec_deg)
    lat = math.radians(lat_deg)

    sin_alt = _clamp(math.sin(dec) * math.sin(lat)
                     + math.cos(dec) * math.cos(lat) * math.cos(ha), -1.0, 1.0)
    alt = math.asin(sin_alt)
    cos_alt = math.cos(alt)
    if abs(cos_alt) < 1e-12:
        return math.degrees(alt), 0.0  # at the zenith azimuth is undefined
    cos_az = _clamp((math.sin(dec) - sin_alt * math.sin(lat)) / (cos_alt * math.cos(lat)),
                    -1.0, 1.0)
    az = math.degrees(math.acos(cos_az))  # 0..180, measured from North
    if math.sin(ha) > 0.0:                # star is west of the meridian
        az = 360.0 - az
    return math.degrees(alt), az


# --- Catalogue --------------------------------------------------------------

@dataclass
class Star:
    hr: int
    ra_deg: float
    dec_deg: float
    vmag: float


def parse_bsc5(path: str) -> list[Star]:
    """Parse the fixed-width Yale BSC5 catalogue (Vizier V/50 byte layout).

    Entries without a position or magnitude (novae, deleted rows) are dropped:
    they cannot be placed or sized, so they are not stars on this map.
    """
    stars: list[Star] = []
    with open(path, encoding="latin-1") as fh:
        for line in fh:
            rah, ram, ras = line[75:77].strip(), line[77:79].strip(), line[79:83].strip()
            sign = line[83:84]
            ded, dem, des = line[84:86].strip(), line[86:88].strip(), line[88:90].strip()
            vmag_s = line[102:107].strip()
            if not (rah and ram and ras and ded and vmag_s):
                continue
            try:
                ra_deg = (int(rah) + int(ram) / 60.0 + float(ras) / 3600.0) * 15.0
                dec = int(ded) + int(dem) / 60.0 + (int(des) if des else 0) / 3600.0
                dec_deg = -dec if sign.strip() == "-" else dec
                vmag = float(vmag_s)
            except ValueError:
                continue
            stars.append(Star(int(line[0:4]), ra_deg, dec_deg, vmag))
    return stars


# --- Magnitude -> style -----------------------------------------------------

@dataclass
class MagStyle:
    radius: float
    opacity: float


def magnitude_style(vmag: float) -> MagStyle:
    """Brighter stars are larger and more opaque. Linear in magnitude (the look
    the eye expects from a star chart), clamped to the visible style range."""
    m = _clamp(vmag, MAG_BRIGHTEST, MAG_LIMIT)
    t = (m - MAG_BRIGHTEST) / (MAG_LIMIT - MAG_BRIGHTEST)  # 0 = brightest, 1 = faintest
    return MagStyle(
        radius=RADIUS_MAX - t * (RADIUS_MAX - RADIUS_MIN),
        opacity=OPACITY_MAX - t * (OPACITY_MAX - OPACITY_MIN),
    )


# --- Projection -------------------------------------------------------------

def az_delta(az: float, az0: float) -> float:
    """Signed azimuth offset from the frame centre, in (-180, 180]."""
    return (az - az0 + 180.0) % 360.0 - 180.0


def project(alt: float, az: float, az0: float) -> tuple[float, float]:
    """Equirectangular alt-az: azimuth -> x (east increases rightward),
    altitude -> y (horizon at the bottom, higher sky toward the top)."""
    x = (0.5 + az_delta(az, az0) / FOV_AZ) * VIEW_W
    y = (1.0 - (alt - HORIZON_ALT) / FOV_ALT) * VIEW_H
    return x, y


def in_frame(alt: float, az: float, az0: float) -> bool:
    return HORIZON_ALT <= alt <= FOV_ALT and abs(az_delta(az, az0)) <= FOV_AZ / 2.0


def pick_center_azimuth(visible) -> float:
    """Choose the framing azimuth whose band carries the most starlight, so the
    masthead lands on the richest, most recognizable slice of the founding sky."""
    best_az, best_weight = 0.0, -1.0
    for az0_i in range(0, 360, 2):
        az0 = float(az0_i)
        weight = sum(MAG_LIMIT + 0.5 - vmag
                     for alt, az, vmag in visible if in_frame(alt, az, az0))
        if weight > best_weight:
            best_weight, best_az = weight, az0
    return best_az


# --- SVG emission -----------------------------------------------------------

def build_svg(framed, az0, az_picked, star_count) -> str:
    rng = random.Random(TWINKLE_SEED)
    # Faint-first so the bright anchors paint last and sit on top.
    framed = sorted(framed, key=lambda item: -item[0].vmag)

    circles = []
    for star, alt, az in framed:
        x, y = project(alt, az, az0)
        style = magnitude_style(star.vmag)
        classes = ["fs-star"]
        if star.vmag <= MAG_BRIGHT:
            classes.append("fs-bright")
        extra = ""
        if rng.random() < TWINKLE_FRACTION:
            classes.append("fs-tw")
            delay = round(rng.uniform(0.0, 5.5), 2)
            extra = f' style="--o:{style.opacity:.2f};--d:{delay}s"'
        circles.append(
            f'  <circle class="{" ".join(classes)}" cx="{x:.1f}" cy="{y:.1f}" '
            f'r="{style.radius:.2f}" opacity="{style.opacity:.2f}"{extra}/>'
        )

    facing = _compass(az_picked)
    body = "\n".join(circles)
    return (
        '{{/* ABOUTME: The Founding Sky — real Yale BSC5 stars above 33.83N 117.92W, '
        '03:00 PDT 22 Apr 2000. */}}\n'
        '{{/* ABOUTME: Generated by scripts/founding_sky.py — do not edit by hand. */}}\n'
        f'{{{{/* {star_count} stars, mag <= {MAG_LIMIT:g}, framed {FOV_AZ:g} x {FOV_ALT:g} '
        f'deg toward azimuth {az_picked:g} ({facing}). */}}}}\n'
        f'<svg class="founding-sky" viewBox="0 0 {VIEW_W:g} {VIEW_H:g}" '
        'preserveAspectRatio="xMidYMid slice" aria-hidden="true">\n'
        f'{body}\n'
        '</svg>\n'
    )


def _compass(az: float) -> str:
    points = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S",
              "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return points[round(az / 22.5) % 16]


# --- Entry point ------------------------------------------------------------

def _repo_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Generate the Founding Sky SVG partial.")
    parser.add_argument("--az", type=float, default=None,
                        help="Force the framing azimuth in degrees (default: densest slice).")
    parser.add_argument("--data", default=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                        "data", "bsc5.dat"))
    parser.add_argument("--out", default=os.path.join(_repo_root(), "layouts", "partials",
                                                       "masthead", "founding-sky.html"))
    args = parser.parse_args(argv)

    jd = julian_date(*FOUNDING_INSTANT_UTC)
    lst = local_sidereal_degrees(jd, OBS_LON)

    visible = []
    for star in parse_bsc5(args.data):
        if star.vmag > MAG_LIMIT:
            continue
        alt, az = equatorial_to_horizontal(star.ra_deg, star.dec_deg, OBS_LAT, lst)
        if alt < HORIZON_ALT:
            continue
        visible.append((star, alt, az))

    az_visible = [(alt, az, star.vmag) for star, alt, az in visible]
    az0 = args.az if args.az is not None else pick_center_azimuth(az_visible)

    framed = [(star, alt, az) for star, alt, az in visible if in_frame(alt, az, az0)]
    svg = build_svg(framed, az0, az0, len(framed))

    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(svg)

    print(f"{len(visible)} stars above the horizon; {len(framed)} framed "
          f"toward azimuth {az0:g} ({_compass(az0)}). Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
