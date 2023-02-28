import argparse
import time

#from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

from src import logger


ARG_DEBUG = None


def set_argument():

    parser = argparse.ArgumentParser(description='daemon/scheduler test module.', usage='python main.py <flags>')
    parser.add_argument('--debug', dest='debug', action="store_true", help='use log level to debug. default: False ( --debug )')
    args = parser.parse_args()

    global ARG_DEBUG
    ARG_DEBUG = args.debug


def job_test1(arg1):
    log = logger.get_logger()
    log.info(f'job start: {time.strftime(arg1)}')
    time.sleep(10)
    log.info(f'job end: {time.strftime(arg1)}')


def run_scheduler():
    scheduler = BlockingScheduler()
    scheduler.add_job(job_test1, 'cron', second='*/5', id='job_1', args=['%H:%M:%S'])
    scheduler.start()


if __name__ == '__main__':

    log = logger.get_logger()
    set_argument()
    if ARG_DEBUG:
        log = logger.set_level_to_debug()

    run_scheduler()
    exit(0)
