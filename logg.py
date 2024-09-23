
import logging
import ecs_logging

class Logg:

    def __init__(self, name: str= 'logger', arquivo: str= 'robo.json'):
        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(logging.DEBUG)
        self.__handler = logging.FileHandler('/app_logs/' + arquivo)
        self.__handler.setFormatter(ecs_logging.StdlibFormatter())
        self.__logger.addHandler(self.__handler)

    def info(self, message: str) -> str:
        self.__logger.info(message)
        return message

    def warning(self, message: str) -> str:
        self.__logger.warning(message)
        return message

    def error(self, message: str) -> str:
        self.__logger.error(message)
        return message

    def critical(self, message: str) -> str:
        self.__logger.critical(message)
        return message