import os
import yaml
import pytz
from aiogram import Router, types
from aiogram.filters import Command, BaseFilter
from aiogram.types import FSInputFile, Message
from datetime import datetime

import config


class RenewConfig:
    # Watch file changing and update content based on it
    def __init__(self):
        self.cached_stamp = 0
        self.cached_cfg = {}

    def get(self) -> dict:
        stamp = os.stat(config.ADBOT_CFG).st_mtime
        if stamp != self.cached_stamp:
            print("Config renewed")
            self.cached_cfg = yaml.safe_load(open(config.ADBOT_CFG))
        return self.cached_cfg


cfg = RenewConfig()


async def start(msg: types.Message) -> None:
    await msg.answer("Hi!\nIt's a bot, that shares AD configs and other stuff")


class BeforeStartFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        json_config = cfg.get()
        tz = pytz.timezone(json_config["game"]["timezone"])
        game_start = tz.localize(json_config["game"]["start_time"])
        now = tz.localize(datetime.now())
        if game_start <= now:
            return True
        else:
            await message.answer("Event is not started yet")
            return False


async def game_config(msg: types.Message) -> None:
    json_config = cfg.get()
    text_config = yaml.safe_dump(json_config["game"])
    await msg.reply(text_config)


# TODO: think how to normally handle LFI stuff
# async def vpn_config(msg: types.Message) -> None:


async def team_token(msg: types.Message) -> None:
    json_config = cfg.get()
    teams = json_config["teams"]
    res = list(map(lambda team: {team["name"]: team.get("token")}, teams))
    text = yaml.safe_dump(res)
    await msg.reply(text)


async def services(msg: types.Message) -> None:
    if not os.path.isfile(config.ARCHIVED_SERVICES):
        await msg.reply("There is no archived services")
        return
    await msg.reply("Start sending services")
    file = FSInputFile(config.ARCHIVED_SERVICES)
    await msg.reply_document(file)


def prepare_router() -> Router:
    router = Router()
    router.message.register(start, Command("start"))
    router.message.filter(BeforeStartFilter())
    router.message.register(game_config, Command("get_config"))
    # router.message.register(vpn_config, Command("get_vpn"))
    router.message.register(team_token, Command("get_token"))
    router.message.register(services, Command("get_services"))
    return router
