import logging
import time
from functools import wraps


MODULE_NAME = "profiler"

LOG = logging.getLogger(MODULE_NAME)
LOG.setLevel(logging.DEBUG)


class pdbot_loghandler(logging.StreamHandler):
    on_same_line = False

    def emit(self, record):
        try:
            msg = self.format(record)
            stream = self.stream
            same_line = hasattr(record, 'same_line')
            if self.on_same_line and not same_line:
                stream.write(self.terminator)
            stream.write(msg)
            if same_line:
                stream.write('...')
                self.on_same_line = True
            else:
                stream.write(self.terminator)
                self.on_same_line = False
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


LOG.addHandler(hdlr=pdbot_loghandler())


def profiler_logging(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        if time.time() - started_at != 0:
            LOG.debug("{0} was running for {1}s".format(func.__name__, time.time() - started_at))
        return result
    return wrap
