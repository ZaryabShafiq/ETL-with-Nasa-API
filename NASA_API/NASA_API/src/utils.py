import logging
import os

def setup_logger(log_file):
    """Set up the logger."""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger()

def handle_error(logger, error_message):
    """Logs and prints errors."""
    logger.error(error_message)
    print(f"Error: {error_message}")
