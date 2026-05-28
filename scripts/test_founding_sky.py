# ABOUTME: Tests for the Founding Sky generator's astronomy pipeline — Julian date,
# ABOUTME: sidereal time, equatorial->horizontal projection, and BSC5 parsing.
import math
import os

import founding_sky as fs

DATA = os.path.join(os.path.dirname(__file__), "data", "bsc5.dat")


# --- Time -------------------------------------------------------------------

def test_julian_date_j2000_epoch():
    # J2000.0 is defined as JD 2451545.0 at 2000-01-01 12:00 UTC.
    assert fs.julian_date(2000, 1, 1, 12, 0, 0) == 2451545.0


def test_gmst_at_j2000_is_known_value():
    # Greenwich Mean Sidereal Time at the J2000 epoch is 280.46061837 deg
    # (USNO / Meeus). This pins the sidereal-time core of the pipeline.
    assert fs.gmst_degrees(2451545.0) == nearly(280.46061837, tol=1e-4)


# --- Equatorial -> horizontal ----------------------------------------------

def test_zenith_when_dec_equals_latitude_on_meridian():
    # A star on the local meridian (HA = 0) at declination = observer latitude
    # sits at the zenith: altitude 90 deg.
    lat = 33.83
    lst = 123.456  # arbitrary; star RA chosen so hour angle is zero
    alt, _ = fs.equatorial_to_horizontal(ra_deg=lst, dec_deg=lat, lat_deg=lat, lst_deg=lst)
    assert alt == nearly(90.0, tol=1e-6)


def test_due_south_meridian_star():
    # On the meridian, south of the zenith (dec < lat): azimuth is due south
    # (180 deg) and altitude is 90 - (lat - dec).
    lat = 33.83
    lst = 80.0
    dec = 0.0  # equator, well south of a +33.83 observer's zenith
    alt, az = fs.equatorial_to_horizontal(ra_deg=lst, dec_deg=dec, lat_deg=lat, lst_deg=lst)
    assert alt == nearly(90.0 - (lat - dec), tol=1e-6)
    assert az == nearly(180.0, tol=1e-6)


def test_polaris_altitude_tracks_latitude():
    # Polaris sits ~0.74 deg from the celestial pole, so its altitude is the
    # observer's latitude (+/- that offset) and its azimuth is essentially due
    # north — true at any instant. Uses the real Founding Sky instant.
    jd = fs.julian_date(*fs.FOUNDING_INSTANT_UTC)
    lst = fs.local_sidereal_degrees(jd, fs.OBS_LON)
    polaris_ra = (2 + 31 / 60 + 49.09 / 3600) * 15.0  # 02h31m49.09s
    polaris_dec = 89 + 15 / 60 + 51 / 3600            # +89d15'51"
    alt, az = fs.equatorial_to_horizontal(polaris_ra, polaris_dec, fs.OBS_LAT, lst)
    assert abs(alt - fs.OBS_LAT) < 1.0
    assert min(az, 360.0 - az) < 3.0


# --- Catalogue parsing ------------------------------------------------------

def test_parse_bsc5_finds_sirius_and_vega():
    stars = {s.hr: s for s in fs.parse_bsc5(DATA)}
    sirius = stars[2491]
    assert sirius.ra_deg == nearly(101.287, tol=0.01)
    assert sirius.dec_deg == nearly(-16.716, tol=0.01)
    assert sirius.vmag == nearly(-1.46, tol=1e-6)
    vega = stars[7001]
    assert vega.ra_deg == nearly(279.235, tol=0.01)
    assert vega.dec_deg == nearly(38.784, tol=0.01)
    assert vega.vmag == nearly(0.03, tol=1e-6)


def test_parse_bsc5_skips_entries_without_position():
    # ~14 BSC5 entries (novae / deleted) carry no coordinates; they must be
    # dropped rather than parsed as (0, 0).
    stars = fs.parse_bsc5(DATA)
    assert all(s.ra_deg is not None and s.dec_deg is not None for s in stars)
    # The catalogue has 9110 lines; placeable stars are fewer.
    assert 9000 < len(stars) < 9110


# --- Magnitude mapping ------------------------------------------------------

def test_brighter_star_is_larger_and_more_opaque():
    bright = fs.magnitude_style(0.0)
    faint = fs.magnitude_style(5.5)
    assert bright.radius > faint.radius
    assert bright.opacity > faint.opacity


def test_magnitude_style_clamps_to_visible_range():
    very_bright = fs.magnitude_style(-1.5)
    floor = fs.magnitude_style(6.0)
    assert very_bright.radius <= fs.RADIUS_MAX + 1e-9
    assert floor.opacity >= fs.OPACITY_MIN - 1e-9


# --- helpers ----------------------------------------------------------------

class nearly:
    """Assertable approximate float: `value == nearly(target, tol=...)`."""

    def __init__(self, target, tol=1e-6):
        self.target = target
        self.tol = tol

    def __eq__(self, other):
        return abs(other - self.target) <= self.tol

    def __repr__(self):
        return f"nearly({self.target} +/- {self.tol})"
