import logging

def setup_logger():
    logger = logging.getLogger('BirthdayReminderBot')
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler('log.txt')
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Note: To avoid duplicate handlers when importing multiple times
    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger

app_logger = setup_logger()

def log_info(message):
    app_logger.info(message)

def log_error(message):
    app_logger.error(message)
