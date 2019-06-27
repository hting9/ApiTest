import logging
import utils

def setup_logger(log_file="apitest.log"):
    logger = logging.getLogger("apitest")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_level = utils.get_config_data('logging', 'level').upper()
    if log_file:
        handler = logging.FileHandler(log_file, encoding="utf-8")
    else:
        handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(log_level)
    return logger

def log_debug(message):
    return setup_logger().debug(message)

def log_info(message):
    return setup_logger().info(message)

def log_warning(message):
    return setup_logger().warning(message)

def log_error(message):
    return setup_logger().error(message)



