from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from . jobs import db_redistribute

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(db_redistribute, 'interval', seconds = 10)
    scheduler.start()

def startCron():
    scheduler = BackgroundScheduler()
    scheduler.start()

    trigger = CronTrigger(
        year="*", month="*", day="*", hour="23", minute="59", second="59"
    )
    scheduler.add_job(
        db_redistribute,
        trigger=trigger,
    )