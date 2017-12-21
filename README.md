# rand-word-python

Retrieves a random word and it's definitions.

## Installation

Just clone this repository and run `sudo ./setup.sh`, then you can use it by running `rand-word` in a terminal. You'll need to add in an API key from [developer.wordnik.com](https://developer.wordnik.com) in order to use this script, just replace the line that has `YOUR API KEY HERE` with your API key.

## Usage

The script can either be run by itself or with a single argument; the directory of the file `words_alpha.txt`, which is included in this repository. It contains the word list. The setup script copies the list to the same location as the script so it can be in the same directory, however if you would like to move that file to a different directory you'll have to pass the new directory in as the argument:

```
# without argument
 rand-word
```

```
# with argument
 rand-word foo/
```