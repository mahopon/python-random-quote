import random

def primary():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  lastNum = len(quotes) - 1
  rndNum = random.randint(0, lastNum)
  print(quotes[rndNum])

if __name__== "__main__":
  primary()
