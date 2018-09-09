# Reddit DataViz Battle September 2018

Code for the Reddit dataisbeautiful [DataViz Battle for the Month of September 2018](https://www.reddit.com/r/dataisbeautiful/comments/9cuzs3/battle_dataviz_battle_for_the_month_of_september/)

Analysis and visual exploration of the [Pokemon dataset](https://www.kaggle.com/rounakbanik/pokemon): 800 Pokemons from all 7 generations.


## Installation

This repository uses pipenv. If you need to install it you can follow the [documentation](https://pipenv.readthedocs.io/en/latest/).

```sh
git clone git@github.com:jackdbd/reddit-dataviz-battle-2018-09.git
cd reddit-dataviz-battle-2018-09
pipenv install --dev
```


## Data

The script `make_db.py` create a SQLite database from the original CSV file.

```sh
cd src
pipenv run python make_db.py
```


## Usage

Launch a Jupyter notebook and explore the data:

```sh
cd notebooks
pipenv run jupyter notebook
```
