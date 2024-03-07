# loggingFramework/main.py
import sys
import json
from pylogstash.logger import CustomLogger  # Import CustomLogger class from pylogstash-handler

#103.80.157.134 || localhost
logstash_host = '103.80.157.134'
logstash_port = 5055

logger = CustomLogger(logstash_host, logstash_port) # task id, tenetid, sourcesystem

count = 0

# Log messages as a dictionary
info_log_message = {
    "message": "python-logstash: test logstash info message.",
    "level": "INFO",
    "extra": {
        "test_string": "python version: " + repr(sys.version_info),
        "test_boolean": True,
        "test_dict": {
            "a": 1,
            "b": "c"
        },
        "test_float": 1.23,
        "test_integer": 123,
        "test_list": [
            1,
            2,
            "3"
        ],
    }
}

error_log_message = {
        "message": "python-logstash: test logstash info message.",
        "level": "ERROR",
        "extra": {
            "test_dict": {"a": 1, "b": "c"},
            "test_float": 1.23,
            "test_integer": 123,
            "test_list": [1, 2, "3"]
        }
    }


# Convert the dictionary to a JSON-formatted string
json_info_message = json.dumps(info_log_message)

json_error_message = json.dumps(error_log_message)

# print(json_info_message)

# print(json_error_message)

from time import sleep
while True:

    count = count + 1

    if count % 2 == 0:
        logger.error(json_info_message)
    else:
        logger.info(json_error_message)
    sleep(5)
