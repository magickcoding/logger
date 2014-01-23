# encoding=utf-8

import os
import os.path
import logging
import logging.handlers

def init_logger(log_conf_items, multi_process = False):
    """ 初始化logger.
    Args:
      log_conf_items: 配置项list.
    由于logging模块在多进程中切分会有丢失现象,Python日志切分统一使用cronolog来处理,因此不再配置suffix
    """
    LOGGER_LEVEL = {
            'DEBUG': logging.DEBUG,
            'INFO' : logging.INFO,
            'WARNING' : logging.WARNING,
            'ERROR' : logging.ERROR,
            'CRITICAL':logging.CRITICAL
            }
    for log_item in log_conf_items:
        logger = logging.getLogger(log_item['name'])
        path = os.path.expanduser(log_item['file'])
        dir = os.path.dirname(path)
        if dir and not os.path.exists(dir):
            os.makedirs(dir)
        handler = logging.FileHandler(path)
        #handler.suffix='%Y%m%d%H'
        formatter = logging.Formatter(log_item['format'])
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(LOGGER_LEVEL[log_item['level']])

if __name__ == '__main__':
    log_items = [
            { 'name':'main', 'file':'main.log', 'level':'DEBUG', 'format':'%(asctime)s %(levelname)s %(message)s' },
            { 'name':'err', 'file':'err.log', 'level':'DEBUG', 'format':'%(asctime)s %(levelname)s %(message)s'},
            ]
    init_logger(log_items)
    logger = logging.getLogger('main')
    logger.info('haha')
