from environs import Env

env = Env()
env.read_env()

BOT_TOKEN: str = env.str("BOT_TOKEN")
LOGGING_LEVEL: int = env.str("LOGGING_LEVEL")
LOGGING_LEVEL: str = env.str("LOGGING_LEVEL")

ADBOT_CFG: str = "cfg.yml"