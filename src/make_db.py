"""Store the data in a SQLite database.

Usage:
    $ python make_db.py

    # Drop DB and verbose output
    $ python make_db.py -d -v
"""
import os
import time
import logging
import argparse
import pandas as pd
import sqlalchemy as sa
from argparse import RawDescriptionHelpFormatter


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter_str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
formatter = logging.Formatter(formatter_str)
sh = logging.StreamHandler()
sh.setFormatter(formatter)

HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
DATA_DIR = os.path.abspath(os.path.join(ROOT, "data"))
DB_NAME = "Pokemon.db"
DB_PATH = os.path.abspath(os.path.join(ROOT, DB_NAME))
TABLE_NAME = "pokemons"

# TODO: abilities table


def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="If set, drop the database at startup",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="If set, increase output verbosity"
    )
    return parser.parse_args()


def main():
    t0 = time.time()
    args = parse_args()
    if args.verbose:
        sh.setLevel(logging.DEBUG)
    else:
        sh.setLevel(logging.INFO)
    logger.addHandler(sh)

    if args.debug:
        try:
            os.unlink(DB_PATH)
        except FileNotFoundError:
            pass

    file_path = os.path.abspath(os.path.join(DATA_DIR, "pokemon.csv"))
    df = pd.read_csv(file_path)
    logger.debug(f"DataFrame: {df.shape}")
    logger.debug(df.columns)
    engine = sa.create_engine(f"sqlite:///{DB_PATH}")
    df.to_sql(TABLE_NAME, con=engine, if_exists="append", index=False)

    t1 = time.time()
    logger.info(f"Done in: {(t1 - t0):.2f} seconds")


if __name__ == "__main__":
    main()
