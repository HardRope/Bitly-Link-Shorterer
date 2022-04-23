# Bitly url shorterer
This programm use the [Bitly service](https://bitly.com/) to make a shortlink or return counts of clicks after get the short link.

## How it works

To run the programm turn into programm directory and write to the console `main.py link`

Examples:

Input
```
main.py https://www.google.com/
main.py https://bit.ly/38drUFA
```
Ouput
```
https://bit.ly/38drUFA
1
```

## How to install
To use the programm you need to create a '.env' file and add your Api-token here.

Format of token in '.env' file looks like: `API-TOKEN = '2baa700828b03db**********fa90c64ad748b69'`

You can get your Api-token after registration at [Bitly](https://bitly.com/). Link to create token: [link](https://app.bitly.com/settings/api/).

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```

## Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.
