import os
from datetime import datetime
from loguru import logger


# Test
#logger.debug("That's it, beautiful and simple logging!")

LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configuration de loguru
logger.add(LOG_FILE_PATH, format="[ {time:YYYY-MM-DD HH:mm:ss} ] {line} {name} - {level} - {message}", level="INFO")



'''
 Testing the code ==> python src/logger.py
 Check the logs folder for the 'logs' foldeer
 if __name__ == "__main__":
    logger.info("This is a test message for starting the logger")
'''
