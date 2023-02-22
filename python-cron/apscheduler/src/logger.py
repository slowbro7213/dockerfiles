import os
import logging
import logging.handlers

from src.common import datetimeutil
from src.common import fileutil


LOGGER_NAME         = 'default-logger'
LOGFILE_DATE_FORMAT = '%Y%m%d%H%M%S'


def get_logger():
    global LOGGER_NAME
    global LOGFILE_DATE_FORMAT

    log = logging.getLogger(LOGGER_NAME)
    if len(log.handlers) > 0:
        return log

    logger_root = fileutil.get_project_root() + '/logs'
    logger_time = datetimeutil.now_str(LOGFILE_DATE_FORMAT)
    os.makedirs(os.path.split(logger_root + '/' + LOGGER_NAME)[0], exist_ok=True)

    log.setLevel(logging.INFO)
    formatter     = logging.Formatter('(%(asctime)s) [%(levelname)s] (%(filename)s:%(lineno)d) > %(message)s')
    fileHandler   = logging.handlers.RotatingFileHandler(filename=logger_root + '/' + LOGGER_NAME + '-' + logger_time + '.log', maxBytes=3*1024*1024*1024)
    streamHandler = logging.StreamHandler()
    fileHandler.setFormatter(formatter)
    streamHandler.setFormatter(formatter)

    log.addHandler(fileHandler)
    log.addHandler(streamHandler)

    return log

def set_level_to_info():
    global LOGGER_NAME

    log = logging.getLogger(LOGGER_NAME)
    log.setLevel(logging.INFO)

def set_level_to_debug():
    global LOGGER_NAME

    log = logging.getLogger(LOGGER_NAME)
    log.setLevel(logging.DEBUG)
