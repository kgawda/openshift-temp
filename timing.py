import pytz
import datetime

def time_now():
    return datetime.datetime.now(pytz.timezone('Europe/Paris'))
