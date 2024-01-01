import argparse
import asyncio
import logging

from aiogram import Bot, Dispatcher

import config
import handlers.user
from logic import enrich_bot


async def on_startup_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    dispatcher.include_router(handlers.user.prepare_router())
    dispatcher["logger"].info("Started polling")


async def on_shutdown_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    dispatcher["logger"].debug("Stopping polling")
    await bot.session.close()
    await dispatcher.storage.close()
    dispatcher["logger"].info("Stopped polling")


def start_bot():
    logging.basicConfig(level=config.LOGGING_LEVEL)

    bot = Bot(config.BOT_TOKEN, parse_mode="HTML")

    dp = Dispatcher()
    dp["logger"] = logging
    dp.startup.register(on_startup_polling)
    dp.shutdown.register(on_shutdown_polling)

    asyncio.run(dp.start_polling(bot))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input",
                        help="Config file from other projects (i.e. from ForcAD). If not provided - read from stdin")
    parser.add_argument("-t", "--type", help="Type of configuration file that will be extracted",
                        choices=["ForcAD_config", "ForcAD_tokens"])
    args = parser.parse_args()

    if args.type:
        enrich_bot(args)
    else:
        start_bot()


if __name__ == '__main__':
    main()
