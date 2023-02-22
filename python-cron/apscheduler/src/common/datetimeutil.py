from datetime import datetime
from dateutil.relativedelta import relativedelta


def after_days(dt_obj, days):
    dt_obj = dt_obj + relativedelta(days=days)
    return dt_obj


def after_hours(dt_obj, hours):
    dt_obj = dt_obj + relativedelta(hours=hours)
    return dt_obj


def after_minutes(dt_obj, minutes):
    dt_obj = dt_obj + relativedelta(minutes=minutes)
    return dt_obj


def before_days(dt_obj, days):
    dt_obj = dt_obj - relativedelta(days=days)
    return dt_obj


def before_hours(dt_obj, hours):
    dt_obj = dt_obj - relativedelta(hours=hours)
    return dt_obj


def before_minutes(dt_obj, minutes):
    dt_obj = dt_obj - relativedelta(minutes=minutes)
    return dt_obj


def now(new_format):
    return datetime.now().strftime(new_format)


def now_str(new_format):
    return convert_dt_to_str(datetime.now(), new_format)


def is_valid_format(dt_str, format):
    try:
        datetime.strptime(dt_str, format)
    except ValueError:
        return False
    return True


def convert_to_javadate(dt_obj):
    # dt_obj example: 2023-02-01 11:42:42, 2023-02-01 11:42:42.605002, type: datetime
    dt_str = str(dt_obj)
    if len(dt_str) == 19: # if no microseconds
        dt_str = dt_str + '.000000'
    dt_str = dt_str[:10] + 'T' + dt_str[11:-3] + '+09:00'
    return dt_str


def convert_dt_to_str(dt_obj, new_format='%Y-%m-%d %H:%M:%S.%f'):
    # new_format default: '%Y-%m-%d %H:%M:%S.%f'
    return dt_obj.strftime(new_format)


def convert_str_to_dt(dt_str, input_format, new_format=None):
    # input_format: format of dt_str
    dt_obj = datetime.strptime(dt_str, input_format)
    if new_format != None:
        dt_str = dt_obj.strftime(new_format)
        dt_obj = datetime.strptime(dt_str, new_format)
    return dt_obj


if __name__ == '__main__':
    now = convert_to_javadate(datetime.now())
    print(now)