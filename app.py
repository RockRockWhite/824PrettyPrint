import os
import re
import sys

import typer
from rich import print
from rich.columns import Columns
from rich.console import Console

TOPICS = {
    "TIMR": "#9a9a99",
    "Leader election": "#67a0b2",
    "Log": "#67a0b2",
    "Persistence": "#d0b343",
    "Snapshot": "#70c43f",
    "LEAD": "#d0b343",
    "TERM": "#70c43f",
    "LOG1": "#4878bc",
    "LOG2": "#398280",
    "CMIT": "#98719f",
    "PERS": "#d08341",
    "SNAP": "#FD971F",
    "DROP": "#ff615c",
    "CLNT": "#00813c",
    "TEST": "#fe2c79",
    "INFO": "#ffffff",
    "WARN": "#d08341",
    "ERRO": "#fe2626",
    "TRCE": "#fe2626",
}


def main():
    input_ = sys.stdin
    console = Console()
    width = console.size.width
    n_columns = 3

    for line in input_:
        res = re.findall(r"(.*) \[(.*)] \[(.*)] term: (\d+), id: (\d+): (.*)", line)[0]
        datetime = res[0]
        module = res[1]
        topic = res[2]
        term = int(res[3])
        id = int(res[4])
        msg = "S{0} T{1}: ".format(id, term) + res[5]

        color = TOPICS[topic]
        msg = f"[{color}]{msg}[/{color}]"

        cols = ["" for _ in range(n_columns)]
        cols[id] = msg
        col_width = int(width / n_columns)
        cols = Columns(cols, width=col_width - 1, equal=True, expand=True)
        print(cols)
        # print(res)


if __name__ == '__main__':
    main()
