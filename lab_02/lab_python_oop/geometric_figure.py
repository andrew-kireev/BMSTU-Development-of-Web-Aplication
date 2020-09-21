from abc import ABC, abstractmethod

class Figure(ABC):

    TYPE = None

    @abstractmethod
    def square(self):
        pass