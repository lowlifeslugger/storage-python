import random
import string
# but lowlife slugger what if-
# lowlifeslugger : nothing ever happens

symbols = string.punctuation + string.ascii_letters + string.digits + " "
symbols = list(symbols)
symbolsencrypted = symbols.copy()
# jkw - just keep watching - tate mcrae, great song

jkw = random.shuffle(symbolsencrypted)
    
while 1:

    message = input(": ")
    messageencrypted = ""


    for letter in message:\
    # kachow you got indexed or sm
        index = message.index(letter)
        messageencrypted +=symbolsencrypted[index]
    print(f"{message} - original\n {messageencrypted} - encrypted")  
    print(f"{jkw}")
    
    continue