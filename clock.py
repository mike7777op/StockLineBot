from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request
import datetime
import time


sched = BlockingScheduler(timezone="Asia/Taipei")


@sched.scheduled_job('cron', day_of_week='mon-sun', minute='*/20')
def scheduled_job():
    print('========== APScheduler CRON =========')
    # 馬上讓我們瞧瞧
    print('This job runs every day */2 min.')
    # 利用datetime查詢時間
    print(f'{datetime.datetime.now().ctime()}')
    print('========== APScheduler CRON =========')
    url = 'https://stocklinebotgary.herokuapp.com'
    conn = urllib.request.urlopen(url)

    for key, value in conn.getheaders():
        print(key, value)

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=21, minute=50)
def line_test():
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    

sched.start()
