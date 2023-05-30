
#------Morese alphabet
#rules: space between 2 words: 7 spaces

alphabet={
'a': ".-",
'b': "-...",
'c': "-.-.",
'd':"-..",
'e':".",
'f':"..-.",
'g':"--.",
'h':"....",
'i':"..",
'j':".---",
'k':"-.-",
'l':".-..",
'm':"--",
'n':"-.",
'o':"---",
'p':".--.",
'q':"--.-",
'r':".-.",
's':"...",
't':"-",
'u':"..-",
'v':"...-",
'w':".--",
'x':"-..-",
'y':"-.--",
'z':"--..",
'0':'-----',
'1':'.----',
'2':'..---',
'3':'...--',
'4':'....-',
'5':'.....',
'6':'-....',
'7':'--...',
'8':'---..',
'9':'----.',

}

user_word=input("Type in your word/ word group or sentence and/or numbers: ").lower()
try:
    for letter in user_word:
        if letter in alphabet:
            key = letter
            value = alphabet[letter]
        elif letter ==" ":
            value="   "
        elif letter not in alphabet:
            print("Please do not use special characters like 'ß' or 'ã'")
        print(value)
except:
    print("Upsi, Something went wrong :(")
