logger
======

python logging module init 

使用举例：
from logger import *
log_items = [
        { 'name':'main', 'file':'main.log', 'level':'DEBUG', 'format':'%(asctime)s %(levelname)s %(message)s' },
        { 'name':'err', 'file':'err.log', 'level':'DEBUG', 'format':'%(asctime)s %(levelname)s %(message)s'},
]
init_logger(log_items)
log = logging.getLogger('main')
log.info('just for test')

