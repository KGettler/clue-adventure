#for clear function
from os import system, name

#for any timely pauses
from time import sleep

#clears console
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#creates scrolling effect while printing text
def scroll(x):
    text = ''
    for i in x:
        clear()
        
        #uses '%' to create longer breaks between sentences or phrases
        if i == '%':
            text += ' '
            print(text)
            sleep(0.5)
        else:
            text += i
            print(text)
            sleep(0.02)

scroll('You awake in a strange room.%Something appears off.')
