import logging
import logstash

class CustomLogger:

    def __init__(self, logstash_host, logstash_port, log_level=logging.INFO):
        # Initialize the logger with the specified name
        self.logger = logging.getLogger('python-logstash-logger')
        
        # Set the logging level for the logger
        self.logger.setLevel(log_level)

        # Create a TCPLogstashHandler to send logs to Logstash
        logstash_handler = logstash.TCPLogstashHandler(logstash_host, logstash_port, version=1)
        
        # Add the Logstash handler to the logger
        self.logger.addHandler(logstash_handler)

        print(logstash_host, logstash_port)

    def log(self, level, message):
        # Log a message with the specified log level
        self.logger.log(level, message)

    def debug(self, message):
        # Log a message with DEBUG log level
        self.log(logging.DEBUG, message)

    def info(self, message):
        # Log a message with INFO log level
        self.log(logging.INFO, message)

    def warning(self, message):
        # Log a message with WARNING log level
        self.log(logging.WARNING, message)

    def error(self, message):
        # Log a message with ERROR log level
        self.log(logging.ERROR, message)

    def critical(self, message):
        # Log a message with CRITICAL log level
        self.log(logging.CRITICAL, message)
