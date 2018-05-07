import time


def millis():
    return int(round(time.time() * 1000 % 1000))


def sec():
    return str(time.localtime().tm_sec)


def min():
    return str(time.localtime().tm_min)

#Belgium timezone (localtime witout changes)
timezone = 0
#New York timezone without my localtime
#timezone = 6
def hour():
    return str(time.localtime().tm_hour - timezone)


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

print(hour())
