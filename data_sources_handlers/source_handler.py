from abc import ABC
class SourceDataHandler(ABC):

    def open_source(self):
        ...


    def close_source(self):
        ...


