def caesar_encrypt(content, cypher_value):
  encryptedWord = []
  cypher = ord(cypher_value) - ord('a')
  for x in content:
    if((ord(x) >= 97 and ord(x) <= 122)): # Verifies if the letter is in between a-z and A-Z
      list_value = ord(x) + cypher
      if list_value > 122:
          list_value = list_value - 122
          list_value = 96 + list_value 
      encryptedWord += [chr(list_value)]
    elif (ord(x) >= 65 and ord(x) <= 90):
      list_value = ord(x) + cypher
      if list_value > 90:
        list_value = list_value - 90
        list_value = 64 + list_value
      encryptedWord += [chr(list_value)]
    else:
      encryptedWord += x
    
  word = ""
  for x in encryptedWord:
      word += x
  return word

def caesar_decrypt(content, cypher_value):
  encryptedWord = []
  cypher = ord(cypher_value) - ord('a')
  for x in content:
    if(ord(x) >= 97 and ord(x) <= 122): # Verifies if the letter is in between a-z and A-Z
      list_value = ord(x) - cypher
      if list_value < 97:
          list_value = list_value + 122
          list_value = list_value - 96 
      encryptedWord += [chr(list_value)]
    elif (ord(x) >= 65 and ord(x) <= 90):
      list_value = ord(x) - cypher
      if list_value < 65:
        list_value = list_value + 90
        list_value = list_value - 64
      encryptedWord += [chr(list_value)]
      #i += 1
    else:
      encryptedWord += x
      #i += 1
    
  word = ""
  for x in encryptedWord:
      word += x
  return word
##
def morse_encrypt(content):
  morseCode = ""
  for x in content:
    if(x == 'A' or x == 'a'):
      morseCode += "•-"
    if(x == 'B' or x == 'b'):
      morseCode += "-•••"
    if(x == 'C' or x == 'c'):
      morseCode += "-•••"
    if(x == 'D' or x == 'd'):
      morseCode += "-••"
    if(x == 'E' or x == 'e'):
      morseCode += "•"
    if(x == 'F' or x == 'f'):
      morseCode += "••-•"
    if(x == 'G' or x == 'g'):
      morseCode += "--•"
    if(x == 'H' or x == 'h'):
      morseCode += "••••"
    if(x == 'I' or x == 'i'):
      morseCode += "••"
    if(x == 'J' or x == 'j'):
      morseCode += "•---" 
    if(x == 'K' or x == 'k'):
      morseCode += "-•-"
    if(x == 'L' or x == 'l'):
      morseCode += "•-••"
    if(x == 'M' or x == 'm'):
      morseCode += "--"
    if(x == 'N' or x == 'n'):
      morseCode += "-•"
    if(x == 'O' or x == 'o'):
      morseCode += "---"
    if(x == 'P' or x == 'p'):
      morseCode += "•--•"
    if(x == 'Q' or x == 'q'):
      morseCode += "--•-"
    if(x == 'R' or x == 'r'):
      morseCode += "•-•"
    if(x == 'S' or x == 's'):
      morseCode += "•••"
    if(x == 'T' or x == 't'):
      morseCode += "-"
    if(x == 'U' or x == 'u'):
      morseCode += "••-"
    if(x == 'V' or x == 'v'):
      morseCode += "•••-"
    if(x == 'W' or x == 'w'):
      morseCode += "•--"
    if(x == 'X' or x == 'x'):
      morseCode += "-••-"
    if(x == 'Y' or x == 'y'):
      morseCode += "-•--"
    if(x == 'Z' or x == 'z'):
      morseCode += "--••"
  return morseCode
def help():
  definitions = "Commands: **/cencrypt**, **/cdecrypt**, **/mencrypt**, **/help** \n **/cencrypt** - encrypts the message in Caesar Shift Cypher - **/cencrypt** Caeser Cypher Letter Message (/cencrpyt h I am the Senate)\n **/cdecrypt** - decrypts the message in Caesar Shift Cypher- **/cdecrypt** Caeser Cypher Letter Message (/cdecrypt h I am the Senate) \n **/mencrypt** - encrypts the message in Morse Code - **/mencrypt** message(/mencrpyt I am the Senate) \n **/help** - prints all of the actions and how to do it \n"
  return definitions
