import logging
import logstash

class CustomLogger:

    def __init__(self, logstash_host, logstash_port, tenant_id, source_system_id, task_name, log_level=logging.INFO):
        # Initialize the logger with the specified name
        self.logger = logging.getLogger('python-logstash-logger')
        
        # Set the logging level for the logger
        self.logger.setLevel(log_level)

        # Store tenant_id, source_system_id, and task_name as attributes
        self.tenant_id = tenant_id
        self.source_system_id = source_system_id
        self.task_name = task_name

        # Create a TCPLogstashHandler to send logs to Logstash
        logstash_handler = logstash.TCPLogstashHandler(logstash_host, logstash_port, version=1)
        
        # Add the Logstash handler to the logger
        self.logger.addHandler(logstash_handler)

    def log(self, level, tenant_id, source_system_id, task_name, message):
        # Log a message with the specified log level
        extra_info = {'tenant_id': tenant_id, 'source_system_id': source_system_id, 'task_name': task_name}
        self.logger.log(level, message, extra=extra_info)

    def debug(self, message):
        # Log a message with DEBUG log level
        self.log(logging.DEBUG, self.tenant_id, self.source_system_id, self.task_name, message)

    def info(self, message):
        # Log a message with INFO log level
        self.log(logging.INFO, self.tenant_id, self.source_system_id, self.task_name, message)

    def warning(self, message):
        # Log a message with WARNING log level
        self.log(logging.WARNING, self.tenant_id, self.source_system_id, self.task_name, message)

    def error(self, message):
        # Log a message with ERROR log level
        self.log(logging.ERROR, self.tenant_id, self.source_system_id, self.task_name, message)

    def critical(self, message):
        # Log a message with CRITICAL log level
        self.log(logging.CRITICAL, self.tenant_id, self.source_system_id, self.task_name, message)
