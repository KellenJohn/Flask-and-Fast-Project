
UTC 轉本地時間
```python
# Hello World program in Python
    
from datetime import datetime
from dateutil import tz

utc_zone = tz.gettz('UTC')
tw_zone = tz.gettz('Asia/Taipei')

utc = datetime.utcnow()
utc = utc.replace(tzinfo = utc_zone)
tw_time = utc.astimezone(tw_zone)
dt = datetime.now()

print('NOW', dt.strftime('%Y/%m/%d %H:%M'))
print('UTC', utc.strftime('%Y/%m/%d %H:%M'))
print('TW', tw_time.strftime('%Y/%m/%d %H:%M'))

# @app.template_filter()
def datetimefilter(utc):
    utc_zone = tz.gettz('UTC')
    tw_zone = tz.gettz('Asia/Taipei')
    utc = utc.replace(tzinfo = utc_zone)
    tw_time = utc.astimezone(tw_zone)
    return tw_time.strftime('%Y/%m/%d %H:%M')
```
