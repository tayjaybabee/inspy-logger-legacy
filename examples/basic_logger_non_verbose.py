# First you gotta import the package. I like to import and assign to a more friendly name
from inspy_logger import start as start_log
"""

An example module to show the basic usage of inspy-logger w/ line-comment instruction

"""

# Actually start the logger.
##
# The first parameter of the start method asks for a string which will be the 'root' name of your
# application. You will find this one the end of every report.
##
# The 'True' boolean here is for the 'debug' parameter which defaults to
# false.
##
# As of now there are only two modes for the logger. Debug and not-debug modes. The non-debug mode
# pretty silent, I do however want to try to add more granular control in future updates
##
# Todo:
#     - Add more output levels/modes (eg (at least) debug, info, quiet, silent)

# This is the only line that differs between basic_logger_verbose.py and basic_logger_non_verbose.py
log = start_log('Application')

# Assign your most commenly used log level calls to single-simple-word variables with ease without
# losing import information to efficiency
info = log.info
info('This is a test of the inspy-logger package')

warn = log.warning
warn('This is a warning')
