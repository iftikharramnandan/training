# Chess Game Data Processing

This repository contains a set of Python scripts and a bash script for processing chess game data in PGN format. The scripts allow you to split games by player, split games into training and validation sets, and convert PGN files into a format suitable for training chess engines.

## Prerequisites

Before running the scripts, make sure you have the following:

- Python 3.x installed
- `chess` library installed (`pip install chess`)
- `pgn-extract` tool installed (download from [https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/))
- `trainingdata-tool` installed (download from [https://github.com/DanielUranga/trainingdata-tool](https://github.com/DanielUranga/trainingdata-tool))

## Configuration

Before running the scripts, you need to configure the `config.ini` file with the necessary information. 

Here's an example of the expected format:

```ini
[Settings]
input = input.pgn
outputs = output1.pgn.bz2, output2.pgn.bz2
ratios = 0.8, 0.2
shuffle = True
seed = 1

[SplitByPlayer]
input = input.pgn
player = PlayerName
output = output_prefix
shuffle = True
seed = 1

[PGNToTrainingData]
player_file = /path/to/input/pgn/file
output_directory = /path/to/output/directory
player_name = PlayerName
```

Open the `config.ini` file and update the following sections:

### [SplitByPlayer]

- `input`: Path to the input PGN file containing chess games.
- `player`: Name of the player to split the games for.
- `output`: Path to the output directory where the split PGN files will be saved.

### [Settings]

- `input`: Path to the input PGN file containing chess games.
- `outputs`: Comma-separated list of output PGN files for splitting the games into training and validation sets.
- `ratios`: Comma-separated list of ratios for splitting the games into training and validation sets.

### [PGNToTrainingData]

- `player_file`: Path to the input PGN file containing chess games.
- `output_directory`: Path to the output directory where the processed files will be saved.
- `player_name`: Name of the player.

Make sure to provide the correct paths and player name in the configuration file.

## Configuration

The `config.ini` file contains the necessary configuration settings for the scripts. Here's an example of the expected format:

```ini
[Settings]
input = input.pgn
outputs = output1.pgn.bz2, output2.pgn.bz2
ratios = 0.8, 0.2
shuffle = True
seed = 1

[SplitByPlayer]
input = input.pgn
player = PlayerName
output = output_prefix
shuffle = True
seed = 1

[PGNToTrainingData]
player_file = /path/to/input/pgn/file
output_directory = /path/to/output/directory
player_name = PlayerName
```

## Usage

1. Place your input PGN file in the specified location according to the `config.ini` file.

2. Open a terminal or command prompt and navigate to the directory containing the scripts.

3. Run the bash script `pgn_to_training_data.sh` by executing the following command:
   ```
   ./pgn_to_training_data.sh
   ```

   The script will read the configuration from `config.ini` and process the PGN files accordingly.

4. The processed files will be saved in the specified output directory according to the configuration.

## Script Details

- `gamesfile.py`: Contains the `GamesFile` class for reading and parsing chess game data from PGN files.
- `pgn_fractional_split.py`: Splits the input PGN file into training and validation sets based on the specified ratios.
- `split_by_player.py`: Splits the input PGN file into separate files for games where the specified player is playing as white or black.
- `pgn_to_training_data.sh`: The main bash script that orchestrates the execution of the Python scripts and external tools to process the PGN files.

The scripts use the `chess` library for handling PGN files and the `pgn-extract` and `trainingdata-tool` tools for processing and converting the PGN files into a suitable format for training chess engines.

The `pgn-extract` tool is used for preprocessing the PGN files, while the `trainingdata-tool` is used for converting the PGN files into a format suitable for training chess engines.

## Contributing

Contributions to this project are welcome! If you encounter any issues, have suggestions for improvements, or want to add new features, please open an issue or submit a pull request on the GitHub repository. Specific areas where contributions are appreciated include:

- Bug fixes
- Performance optimizations
- Documentation enhancements
- New features or functionalities

## Contact

If you have any questions or need further assistance, feel free to reach out to the project maintainer at [n4k3dwaffles@outlook.com].

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize the scripts and configuration according to your specific requirements. If you have any questions or encounter any issues, please open an issue in the repository.


