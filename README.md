# ADBot

A telegram bot for sharing vpn-config, round info & etc.

## Setup
Create `.env` - as example use `.env.example` 

## Enrich bot's database
The owner must add the information to the bot manually.

```bash
python main.py -t ForcAD_config < ssh user@13.37.13.37 cat ForcAD/config.yml
python main.py -t ForcAD_tokens -i /var/tmp/team_tokens
```

### Supported config-parsers
- ForcAD_config
- ForcAD_token

## Add your own parser

1. Add logic/%platform%.py
2. Сreate a class that will inherit Transform from logic/base.py
3. Impelement methods `parse` and `update_rule` of created class
4. Add starategy to `strats` in logic/__init__.py
