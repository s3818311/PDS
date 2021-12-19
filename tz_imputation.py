from timezonefinder import TimezoneFinder
from datetime import datetime
from pytz import timezone, utc


def get_tz(lat, lng):
    """
    returns a location's time zone offset from UTC.\n
    credits: https://timezonefinder.readthedocs.io/en/latest/2_use_cases.html#getting-a-location-s-time-zone-offset
    """

    tf = TimezoneFinder()
    tz_d = {-8: "US/Pacific", -7: "US/Mountain", -6: "US/Central", -5: "US/Eastern"}

    today = datetime.now()
    tz_target = timezone(tf.certain_timezone_at(lng=lng, lat=lat))
    today_target = tz_target.localize(today)
    today_utc = utc.localize(today)
    utc_offset = int((today_utc - today_target).total_seconds() / 60 / 60)

    return tz_d[utc_offset]
