from environs import Env

env = Env()
env.read_env()

BOT_TOKEN: str = env.str("BOT_TOKEN")
LOGGING_LEVEL: str = env.str("LOGGING_LEVEL")
ARCHIVED_SERVICES: str = env.str("ARCHIVED_SERVICES")

ADBOT_CFG: str = "cfg.yml"