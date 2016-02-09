import logging
import sys


def initLogging(path, level=logging.INFO, tee=False):
    '''
    Inialize logger

    path    Path to log output file
    level   Logging level (e.g. logging.INFO, logging.WARN)
    tee     Specifies whether log output should be teed to stdout
    '''
    fmt = '%(asctime)-15s.%(msecs)03d %(levelname)-8s %(message)s'
    # fmt = '%(asctime)s %(levelname)-8s %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'

    # Remove any unwanted, existing loggers from imports
    root = logging.getLogger()
    for h in root.handlers:
        root.removeHandler(h)

    logging.basicConfig(filename=path, filemode='a', level=level,
                        format=fmt,
                        datefmt=datefmt)

    # Tee log to stdout
    if tee:
        hStdout = logging.StreamHandler(sys.stdout)
        hStdout.setLevel(level)
        formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
        hStdout.setFormatter(formatter)

        logger = logging.getLogger('')
        logger.addHandler(hStdout)
