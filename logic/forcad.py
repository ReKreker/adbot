import yaml

from logic.base import Transform


class Config(Transform):
    def parse(self, text: str):
        self.parsed = yaml.safe_load(text)

    def update_rule(self, cfg: dict):
        for k, v in self.parsed.items():
            cfg[k] = v
        return cfg


class Tokens(Transform):
    def parse(self, text: str) -> None:
        self.parsed = {}
        for line in text.splitlines():
            team, token = line.rsplit(":", 1)
            self.parsed[team] = token

    def update_rule(self, cfg: dict) -> None:
        for i in range(len(cfg["teams"])):
            team = cfg["teams"][i]["name"]
            token = self.parsed.get(team)
            if token is None:
                print(f"Not found token for {team}")
                continue
            cfg["teams"][i]["token"] = token
