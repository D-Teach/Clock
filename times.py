import time

from datetime import datetime, timedelta
from pytz import timezone
import pytz




def dddd(zone='Indian/Mahe'):
    other_zone = timezone(zone)
    ddd = datetime.now(other_zone)
    return ddd.strftime('%T')


def millis():
    return int(round(time.time() * 1000 % 1000))

def sec():
    return str(time.localtime().tm_sec)

def min():
    return str(time.localtime().tm_min)

def hour():
    return str(time.localtime().tm_hour)

def convert(h, m, s):
    res = ""
    if int(h) < 10:
        res = res + "0" + h
    else:
        res = res + h

    if int(m) < 10:
        res = res + ":0" + m
    else:
        res = res + ':' + m

    if int(s) < 10:
        res = res + ":0" + s
    else:
        res = res + ':' + s

    return res

