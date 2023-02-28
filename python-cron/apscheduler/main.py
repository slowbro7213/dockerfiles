import argparse
import time

import daemon
from daemon import pidfile

from src import logger

from src.common import fileutil


ARG_DAEMON = None
ARG_DEBUG = None


def set_argument():

    parser = argparse.ArgumentParser(description='daemon/scheduler test module.', usage='python main.py <flags>')
    parser.add_argument('--daemon', '-d', default='no', dest='daemon', help='run mode. default: no ( --daemon|-d no|start|stop )')
    parser.add_argument('--debug', dest='debug', action="store_true", help='use log level to debug. default: False ( --debug )')
    args = parser.parse_args()

    if args.daemon.lower() != 'no' and args.daemon.lower() != 'start' and args.daemon.lower() != 'stop':
        raise Exception('Error: invalid args. --daemon|-d: no, start or stop')

    global ARG_DAEMON
    global ARG_DEBUG
    ARG_DAEMON = args.daemon.lower()
    ARG_DEBUG = args.debug


if __name__ == '__main__':

    log = logger.get_logger()
    set_argument()
    if ARG_DEBUG:
        log = logger.set_level_to_debug()
    pid.remove_old_pidfile()

    if ARG_DAEMON == 'no':
        print('no daemon')

    elif ARG_DAEMON == 'start':
        print('start daemon')
        with daemon.DaemonContext(working_directory=fileutil.get_project_root(), umask=0o002, pidfile=pidfile.TimeoutPIDLockFile(pid.PID_PATH)) as cxt:
            while(True):
                time.sleep(10)

    elif ARG_DAEMON == 'stop':
        print('stop daemon')
        pid.kill_process_if_exist()

    else:
        log.error(f'Error: invalid mode ({ARG_DAEMON})')
        exit(1)
    exit(0)
