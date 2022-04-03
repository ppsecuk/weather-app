import sys, time
import logging, logging.config, coloredlogs

logging.Formatter.converter = time.gmtime
FORMATTER = logging.Formatter("%(asctime)s - %(levelname)s — %(name)s:%(funcName)s:%(lineno)d — %(message)s")

def getConsoleHandler():
    """ Console handler. """
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)

    return console_handler

def getLogger(logger_name):
    """ Init logger. """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    coloredlogs.install(level='DEBUG', logger=logger)

    if not logger.handlers:
        logger.addHandler(getConsoleHandler())

    logger.propagate = False

    return logger