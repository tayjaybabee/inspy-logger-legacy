# First you gotta import the package
from inspy_logger import start as start_log

log = start_log('Application', True)
info = log.info
info('This is a test of the inspy-logger package')
