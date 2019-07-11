#! /usr/bin/env python
import argparse
import pandas as pd
from lambdata_richmondtest import DataFrameWithHelpers

def run(args):
    filepath = args.input  # these match the "dest": dest="input"
    format = args.format
    df = pd.read_csv(filepath)
    df = DataFrameWithHelpers(df)
    out = df.tabulate(headers='keys', tablefmt=format, max_rows=9999999, max_cols=9999999)
    print(out)

def main():
    parser = argparse.ArgumentParser(description="Format csv")
    parser.add_argument("-i", help="input csv file.",
                        dest="input", type=str, required=True)
    parser.add_argument("--format",  choices=[
        "plain",
        "simple",
        "github",
        "grid",
        "fancy_grid",
        "pipe",
        "orgtbl",
        "jira",
        "presto",
        "psql",
        "rst",
        "mediawiki",
        "moinmoin",
        "youtrack",
        "html",
        "latex",
        "latex_raw",
        "latex_booktabs",
        "textile",
        ],
        
        help="format",
                        dest="format", type=str, default='')
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
