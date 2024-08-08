# icanhazdadjoke

A simple script to query https://icanhazdadjoke.com/api every 15 seconds for 60 seconds

## Setup

Run the following commands to set up a local virtual environment for Python

```
pip3 install -U virtualenv      # Install virtualenv if it isn't already
virtualenv venv                 # Setup virtual environment
source venv/bin/activate        # Activate virtual environment
pip install -r requirements.txt # Install requirements
```

To get out of the virtual environment, just run `deactivate`

## Usage

To run the script, do either `./dad_joke.py` or `python3 dad_joke.py`

```
❯ ./dad_joke.py -h
usage: dad_joke.py [-h] [-n NUMBER] [-s SEARCH]

options:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        The number of dad jokes to return in each set. Default is 1. Must be between 1 and 40.
  -s SEARCH, --search SEARCH
                        A search term to look up
```
