import inspy_logger

log_device = inspy_logger.Logger()
log = log_device.start('TestApplication', verbose=True)

second_logger = inspy_logger.Logger()
log_2 = second_logger.start('AnotherApplication')
