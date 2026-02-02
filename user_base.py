from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def get_access_level(self):
        pass