from abc import ABC, abstractmethod


class Transform(ABC):
    def __init__(self):
        self.parsed = ""  # method

    # Parsing config from file/stdin. The result have to be inserted to self.parsed
    @abstractmethod
    def parse(self, text: str) -> None:
        pass

    # Update internal config that will be used by tg-bot. @cfg will be changed as dict arg
    @abstractmethod
    def update_rule(self, cfg: dict) -> None:
        pass
