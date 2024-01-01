import yaml

from logic.base import Transform


class Config(Transform):
    def parse(self, text: str):
        self.parsed = yaml.safe_load(text)

    def update_rule(self, cfg: dict):
        for k, v in self.parsed.items():
            cfg[k] = v
        return cfg
