from abc import ABC, abstractmethod

class DataHandler(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def read_all(self):
        pass
    
    @abstractmethod
    def delete_record(self, name):
        pass
