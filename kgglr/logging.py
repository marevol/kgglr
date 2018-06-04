# coding: utf-8

import logging
import sys

if 'stdout' not in globals():
    stdout = sys.stdout
if 'stderr' not in globals():
    stderr = sys.stderr

class StdOutLogger(object):
    def __init__(self, orig, writer):
        self.orig = orig
        self.writer = writer
        self.buffer = ''

    def write(self, s):
        if s.endswith('\n'):
            self.writer(self.buffer + s[0:-1])
            self.buffer = ''
        else:
            self.buffer = self.buffer + s

    def flush(self):
        pass

    def __getattr__(self, name):
        return object.__getattribute__(self.orig, name)


def init_logger(output_file='output.log',
                log_format='%(asctime)-15s [%(levelname)s] %(message)s'):
    logger = logging.getLogger()
    logger.handlers = []
    logger.addHandler(logging.StreamHandler(stdout))
    if output_file is not None:
        logger.addHandler(logging.FileHandler(output_file))
    for x in logger.handlers:
        x.setFormatter(logging.Formatter(log_format))
    logger.setLevel(logging.INFO)
    sys.stdout = StdOutLogger(stdout, lambda s: logger.info(s))
    sys.stderr = StdOutLogger(stderr, lambda s: logger.error(s))
    return logger
