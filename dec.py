#!/usr/bin/env python

import pyperclip
import vigenereCipher
import sys, getopt

def main(argv):
  password = ''
  try:
    opts, args = getopt.getopt(argv,"hp:",["pword="])
  except getopt.GetoptError:
    print ('dec.py -p <password>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print ('dec.py -p <password>')
      sys.exit()
    elif opt in ("-p", "--pword"):
      password = arg
  if password != '':
    myMessage = ''
    translated = ''
    myMessage = pyperclip.paste()
    translated = vigenereCipher.decryptMessage(password, myMessage)
    pyperclip.copy(translated)
    print('done.')
    
if __name__ == "__main__":
  main(sys.argv[1:])