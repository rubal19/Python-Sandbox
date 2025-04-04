class Logger:

    def __init__(self) -> None:
        pass

    def __generic_log(self, type, message):
        print("[ {t} ] {m}".format(t = type, m = message))

    def info(self, message):
        self.__generic_log("INFO", message)

    def warning(self, message):
        """
        Logs a warning message using the provided message parameter.
        
        Parameters:
            self: the Logger object itself.
            message: a string containing the warning message to be logged.
        """
        self.__generic_log("WARNING", message)

    def debug(self, message):
        self.__generic_log("DEBUG", message)

    def error(self, message, raiseException=False):
        if raiseException:
            raise Exception(message)
        else:
            self.__generic_log("ERROR", message)