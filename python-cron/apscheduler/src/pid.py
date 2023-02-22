import os
import signal

from src import logger
from src.common import fileutil


PID_PATH              = '/var/run/py-daemon.pid'


def get_pid():

    global PID_PATH

    file_pid = None
    try:
        file_pid = fileutil.read_file(PID_PATH)
        file_pid = file_pid.strip()
        file_pid = int(file_pid)
    except:
        return None
    return file_pid


def exist_process():

    global PID_PATH

    file_pid = get_pid()
    if file_pid == None:
        raise FileNotFoundError(f'{PID_PATH} is not found.')
    try:
        os.kill(file_pid, 0)
    except OSError:
        return False
    else:
        return True


def kill_process_if_exist():
    
    global PID_PATH

    if exist_process():
        file_pid = get_pid()
        os.kill(file_pid, signal.SIGKILL)
        try:
            fileutil.remove_file(PID_PATH)
            return True
        except Exception as e:
            log = logger.get_logger()
            log.error(f'Error while remove pid file: {e}', exc_info=True)
    return False


def remove_old_pidfile():
    
    global PID_PATH

    if get_pid() != None:
        if not exist_process():
            try:
                return fileutil.remove_file(PID_PATH)
            except Exception as e:
                log = logger.get_logger()
                log.error(f'Error while remove pid file: {e}', exc_info=True)
    return False

