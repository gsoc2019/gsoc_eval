# CONVERTING TIMESTAMP TO UTC AND CET(CENTRAL EUROPIAN TIME) TIME

from datetime import datetime
from pytz import timezone 


def convert_to_tz(nano_seconds,zone = 'UTC'):
    UTC = datetime.utcfromtimestamp(nano_seconds)
    return UTC.astimezone(timezone(zone))
