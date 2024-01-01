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

## Add your own parser

under construction
