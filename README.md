# Scrabble-Telegram-Bot
 Telegram Bot for basic Scrabble needs, using Python-Telegram-Bot library.
 
 Dictionary Used: CSW21, can be changed by uploading a new dictionary (txt format, separated by \n) and changing the path in main.py
 
# Functions
 Unscramble
 
 Unscrambles the letters provided to find all possible Bingos
 
 Usage: /unscramble *insert 7 letters*
 
 E.g.: /unscramble etrials returns a list of possible Bingos, e.g. retails
 
 
 Dict
 
 Lists all possible words of length provided and starting with the letter provided
 
 Usage: /dict *insert letter* *insert number*
 
 E.g.: /dict q 4 returns a list of all words of length 4, that starts with the letter q
 
 
 Check
 
 Checks all words provided to see if they're valid plays.
 
 Usage: /check *insert words separated by spaces (up to 50)*
 
 E.g.: /check qua qaid quit ashdja
 
 Random and Retire
 
 Try it out yourselves :)

# References
Python-Telegram-Bot: https://github.com/python-telegram-bot/python-telegram-bot\

Resource for /retire: https://github.com/ShatteredDisk/ (Not gonna ruin the surprise by including the specific library)

Resource for /random: https://thecatapi.com/

Originally done on Replit.com
