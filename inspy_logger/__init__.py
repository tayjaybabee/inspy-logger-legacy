#!/usr/bin/env python3


def figure_version():
    pass


from inspy_logger.helpers.decorators import singleton
from inspy_logger.errors import ApplicationError, UnknownError

import logging
from colorlog import ColoredFormatter


@singleton
class Logger(object):


    @staticmethod
    def formatter():
        """

        The formatter for

        Returns:

        """
        __formatter = ColoredFormatter(
            "%(bold_cyan)s%(asctime)-s%(reset)s%(log_color)s::%(module)s.%(name)-14s::%(levelname)-10s%("
            "reset)s%(blue)s%(message)-s",
            datefmt=None,
            reset=True,
            log_colors={
                    'DEBUG':    'bold_cyan',
                    'INFO':     'bold_green',
                    'WARNING':  'bold_yellow',
                    'ERROR':    'bold_red',
                    'CRITICAL': 'bold_red',
                    }
            )
        return __formatter


    def add_handler(self):

        handler = logging.StreamHandler()
        handler.setFormatter(self.formatter)
        self.logger.addHandler(handler)


    @staticmethod
    def set_level(verbose=False, quiet=False, debug=False):
        """
    
        Args:
            verbose (Bool): Should the program output in verbose mode?
            quiet (Bool): Should the program output in quiet mode?
            debug (Bool): Should the program output in debug mode?
        """
        __log_level = None

        if verbose:
            __log_level = logging.DEBUG

        elif quiet:
            __log_level = logging.WARNING

        elif debug:
            __log_level = logging.DEBUG

        if __log_level is None:
            __log_level = logging.INFO

        return __log_level


    def start(self, name, verbose=False, quiet=False, debug=False):
        """
    
        Start a formatted root-logger
    
        :type name: str
        :param debug: Boolean - If True logger will start in at debug level. This is most useful if you're trying to see
                                the internal goings-on immediately on starting the logger.
    
        :param name: str - The name you want to give to the root logger
    
        """

        if self.device is None:
            if self.device_started:
                try:
                    raise UnknownError(info='No logging device detected, but device is flagged as started')
                except UnknownError as e:
                    print(e.message)
                    exit(1)
            else:

        self.log_level = self.set_level(verbose, quiet, debug)

        logger = logging.getLogger(name)
        handler = logging.StreamHandler()
        handler.setFormatter(self.formatter)
        logger.addHandler(handler)

        self.set_level(verbose, quiet, debug)

        logger.info(f'Log device started for {name}')
        self.device_started = True
        logger.debug(f'device_started: {self.device_started}')
        return logger


    def __init__(self):
        try:
            self.device_started
        except AttributeError:
        self.device_started = False
        self.available_levels = [
                'DEBUG',
                'VERBOSE',
                'QUIET'
                ]
