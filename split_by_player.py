import configparser
import logging
import bz2
import random
from gamesfile import GamesFile

def main():
    # Read the configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # Get the configuration values
    input_file = config.get('SplitByPlayer', 'input')
    player = config.get('SplitByPlayer', 'player')
    output_prefix = config.get('SplitByPlayer', 'output')
    shuffle = config.getboolean('SplitByPlayer', 'shuffle')
    seed = config.getint('SplitByPlayer', 'seed')

    random.seed(seed)

    games = GamesFile(input_file)
    outputs_white = []
    outputs_black = []

    for i, (d, l) in enumerate(games):
        if d['White'] == player:
            outputs_white.append(l)
        elif d['Black'] == player:
            outputs_black.append(l)
        else:
            raise ValueError(f"{player} not found in game {i}:\n{l}")

        if i % 10000 == 0:
            logging.info(f"{i} done with {len(outputs_white)}:{len(outputs_black)} players from {input_file}")

    logging.info(f"{i} found totals of {len(outputs_white)}:{len(outputs_black)} players from {input_file}")

    logging.info("Writing white")
    with bz2.open(f"{output_prefix}_white.pgn.bz2", 'wt') as f:
        if shuffle:
            random.shuffle(outputs_white)
        f.write(''.join(outputs_white))

    logging.info("Writing black")
    with bz2.open(f"{output_prefix}_black.pgn.bz2", 'wt') as f:
        if shuffle:
            random.shuffle(outputs_black)
        f.write(''.join(outputs_black))

    logging.info("done")

if __name__ == '__main__':
    main()