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
    input_file = config.get('Settings', 'input')
    outputs = config.get('Settings', 'outputs').split(',')
    ratios = [float(r) for r in config.get('Settings', 'ratios').split(',')]
    shuffle = config.getboolean('Settings', 'shuffle')
    seed = config.getint('Settings', 'seed')

    if len(ratios) != len(outputs):
        raise RuntimeError(f"Invalid outputs specified: {outputs} and {ratios}")

    random.seed(seed)

    games = GamesFile(input_file)
    game_strs = []
    for i, (d, l) in enumerate(games):
        game_strs.append(l)
        if i % 10000 == 0:
            logging.info(f"{i} done from {input_file}")

    logging.info(f"{i} done total from {input_file}")

    if shuffle:
        random.shuffle(game_strs)

    split_indices = [int(r * len(game_strs) / sum(ratios)) for r in ratios]
    # Correction for rounding, not very precise
    split_indices[0] += len(game_strs) - sum(split_indices)

    for p, c in zip(outputs, split_indices):
        logging.info(f"Writing {c} games to: {p}")
        with bz2.open(p, 'wt') as f:
            f.write(''.join(
                [game_strs.pop() for i in range(c)]
            ))

    logging.info("done")

if __name__ == '__main__':
    main()