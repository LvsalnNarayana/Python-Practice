import logging
from test_module import test_func

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def testing_logger():
    print(test_func())
    logging.warning("Main    : before running thread")

testing_logger()
