import telegram.ext
import os
import keep_alive
import urllib
import json


## To Split Word List by Letter
def splitLst(x):
    dictionary = dict()
    for word in x:
        f = word[0]
        if f in dictionary.keys():
            dictionary[f].append(word)
        else:
            dictionary[f] = [word]
    return dictionary

def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]
  


## To open Word bank. To update the dictionary, download the next word bank and update path below (In the form of txt file only)
f = open('CSW21.txt', 'r')
tempString = f.read().upper()
wordList = tempString.split()
f.close()

letterDict = splitLst(wordList)

Token = os.environ['Token']

updater = telegram.ext.Updater(Token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    update.message.reply_text(
        "Welcome to Hall X Word Games Bot created by a useless guy")


def help(update, context):
    update.message.reply_text("To use our bot, choose from one of the following commands:\n\n /check : Input your words, separated by a space to check if they're valid words\n\n /unscramble : Input your characters, separated by a space to see if you can form a valid word\n\n /dict : Input a character, with a space and an integer representing the length of word to find all valid words starting with the letter, with represented integer length \n\n /random : Get a random cat pic")


def check(update, context):
    checkList = update.message.text.upper().split()
    checkList = checkList[1:]
    if len(checkList) == 0:
      update.message.reply_text("Please input words for me to check.")
      return
    elif len(checkList) > 50:
      update.message.reply_text("I can't process so many words. Please limit it to 50 per request.")
      return

    valid = ""
    invalid = ""
    for i in checkList:
        if i in wordList:
            if valid != "":
              valid = valid + ", " + i
            else:
              valid = i
        else:
            if invalid != "":
              invalid = invalid + ", " + i
            else:
              invalid = i
    str = "Valid: " + valid + "\n" + "Invalid: " + invalid
    update.message.reply_text(str)


def unscramble(update, context):
    possibleBingo = list()
    letterList = update.message.text.upper().split()
    letterList = letterList[1:]
    if len(letterList) == 1:
        letterList = list(letterList[0])

    if len(letterList) != 7:
      update.message.reply_text("Please provide a valid Scrabble hand")
      return
    
    for i in letterList:
        if i == "?":
            letterList.remove("?")
    for i in letterList:
        tempList = letterList.copy()
        tempList.remove(i)
        tempWordList = letterDict.get(i)
        for j in tempWordList:
            letters = list(j)
            if len(letters) == 7:
                letters = letters[1:]
                success = True
                for k in tempList:
                    if k in letters:
                        letters.remove(k)
                    else:
                        success = False
                        break
                if success:
                    possibleBingo.append(j)
            else:
                continue
    possibleBingo = list(split(possibleBingo, 300))
    for i in range(len(possibleBingo)):
      str = ""
      printList = possibleBingo[i]
      for i in printList:
        if str == '':
          str = i
        else:
          str = str + ", " + i
      if i == 0:
        update.message.reply_text("Possible Bingos: " + str)
      else:
        update.message.reply_text(str)


def dict(update, context):
    dictList = list()
    letter = update.message.text.upper().split()
    letter = letter[1:]
    possibleWords = letterDict.get(letter[0])
    for i in possibleWords:
        if len(i) == int(letter[1]):
            dictList.append(i)
    
    dictList = list(split(dictList, 300))
    for i in range(len(dictList)):
      str = ""
      printList = dictList[i]
      for i in printList:
        if str == '':
          str = i
        else:
          str = str + ", " + i
      if i == 0:
        update.message.reply_text("List of words starting with " + letter[0] + "and length " + letter[1] + ": " + str)
      else:
        update.message.reply_text(str)


def random(update, context):
  catapi = urllib.request.urlopen("https://api.thecatapi.com/v1/images/search")
  catjson = catapi.read()
  catapi.close()

  catDict = json.loads(catjson)[0]
  catUrl = catDict.get("url")

  update.message.reply_photo(catUrl)


def retire(update, context):
  update.message.reply_video("https://github.com/Beanorockz/Scrabble-Telegram-Bot/blob/main/imptvid.mp4")
      


dispatcher.add_handler(telegram.ext.CommandHandler("start", start))
dispatcher.add_handler(telegram.ext.CommandHandler("help", help))
dispatcher.add_handler(telegram.ext.CommandHandler("dict", dict))
dispatcher.add_handler(telegram.ext.CommandHandler("unscramble", unscramble))
dispatcher.add_handler(telegram.ext.CommandHandler("check", check))
dispatcher.add_handler(telegram.ext.CommandHandler("random", random))
dispatcher.add_handler(telegram.ext.CommandHandler("retire", retire))

keep_alive.keep_alive()
updater.start_polling()
updater.idle()
