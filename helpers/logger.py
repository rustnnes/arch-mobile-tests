import logging, logging.config, yaml

with open("logger.conf", "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)


class LoggerProvider:
    @staticmethod
    def get_logger(name):
        return logging.getLogger(name)