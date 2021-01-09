from abc import abstractmethod, ABC


class SystemCall(ABC):
    process = None
    scheduler = None

    @abstractmethod
    def handle(self):
        pass
