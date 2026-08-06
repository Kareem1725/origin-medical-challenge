import logging
from pathlib import Path


LOG_DIR = Path(__file__).resolve().parent / "logs"

LOG_DIR.mkdir(exist_ok=True)


LOG_FILE = LOG_DIR / "pipeline.log"


def get_logger():

    logger = logging.getLogger("medical_pipeline")

    logger.setLevel(logging.INFO)


    # Avoid duplicate handlers
    if logger.handlers:
        return logger


    file_handler = logging.FileHandler(LOG_FILE)

    console_handler = logging.StreamHandler()


    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )


    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)


    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


    return logger