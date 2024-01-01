import os
import sys
from difflib import Differ

import yaml
from argparse import Namespace

import config
import logic.forcad

strats = {
    "ForcAD_config": forcad.Config,
    # "ForcAD_tokens":
}


def show_diff(original, updated):
    print("Differences:")
    d = Differ()
    original = yaml.dump(original).splitlines(keepends=True)
    updated = yaml.dump(updated).splitlines(keepends=True)
    result = list(d.compare(original, updated))
    sys.stdout.writelines(result)


def enrich_bot(cli_args: Namespace) -> None:
    if cli_args.input is not None:
        text = open(cli_args.input).read()
    else:
        text = sys.stdin.read()

    strategy = strats.get(cli_args.type)
    assert strategy, "Not a valid config's type"
    print("Start parsing...")
    elem = strategy()
    elem.parse(text)

    if not os.path.exists(config.ADBOT_CFG):
        cfg = {}
    else:
        cfg = yaml.safe_load(open(config.ADBOT_CFG, "r"))
    original = cfg.copy()

    elem.update_rule(cfg)
    yaml.safe_dump(cfg, open(config.ADBOT_CFG, "w+"))

    show_diff(original, cfg)
