"""Defines all the parser commands"""
from typing import Any
from argparse import Namespace, _SubParsersAction
from fuzz_utils.parsing.commands.generate import generate_command, generate_flags
from fuzz_utils.parsing.commands.template import template_command, template_flags
from fuzz_utils.parsing.commands.init import init_command, init_flags

parsers: dict[str, dict[str, Any]] = {
    "init": {
        "command": init_command,
        "help": "Generate an initial configuration file.",
        "flags": init_flags,
        "subparser": None,
    },
    "template": {
        "command": template_command,
        "help": "Generate an initial configuration file.",
        "flags": template_flags,
        "subparser": None,
    },
    "generate": {
        "command": generate_command,
        "help": "Generate unit tests from fuzzer corpora sequences.",
        "flags": generate_flags,
        "subparser": None,
    },
}


def define_subparsers(subparser: _SubParsersAction) -> None:
    """Defines the subparser flags and commands"""

    for key, value in parsers.items():
        # Initialize subparser
        help_str: str = value["help"]
        parser = subparser.add_parser(key, help=help_str)
        value["subparser"] = parser
        # Initialize subparser flags
        value["flags"](parser)


def run_command(args: Namespace) -> bool:
    """Runs the command associated with a particular subparser"""
    if args.command in parsers:
        parsers[args.command]["command"](args)
        return True

    return False
