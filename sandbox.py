from Logging import Logger
log = Logger()

class application:

    def __init__(self) -> None:
        pass

    def execute(self):
        log.info("Starting Application")

        isContinueApp = True

        while isContinueApp:
            inp = input()

            if inp.__eq__("exit"):
                isContinueApp = False
            elif inp.__eq__("p1"):
                pass