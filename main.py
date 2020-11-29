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
    global text
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

#prints room header, and description on first entry
def rm():
    scroll(rmName[rmID] + '\n')
    if rmDesc[rmID][1] == 1:
        rmDesc[rmID][1] = 0
        lk()

#prints room description
def lk():
    scroll(rmDesc[rmID][0] + '\n')

#moves player in desired direction if possible
def mov():
    global plyrCom, rmID, text
    if any(i in plyrCom for i in north):
        ID = rmMap[rmID][0]
    elif any(i in plyrCom for i in south):
        ID = rmMap[rmID][1]
    elif any(i in plyrCom for i in east):
        ID = rmMap[rmID][2]
    elif any(i in plyrCom for i in west):
        ID = rmMap[rmID][3]
    
    #only permits movement is room index is integer (if room exists)
    try:
        rmID = ID + 0
        rm()
    except:
        
        #flavor text based on where invalid move occurs
        if rmID == 0:
            print('While you could simply leave the area, that would defeat both the purpose of the investigation and me coding this entire thing.\n')
        else:
            print('Unfortunately, your inability to permeate solid matter prevents you from moving.\n')

#main function - asks player for input, and acts accordingly
def com():
    global plyrCom, text
    plyrCom = input('> ').lower()
    text += '\n> ' + plyrCom + '\n\n'
    plyrCom = plyrCom.split()
    if any(i in plyrCom for i in move):
        mov()
    elif any(i in plyrCom for i in look):
        lk()
    else:
        print('I beg your pardon?\n')

#room header prints when player enters; order determines associated with each room
rmName = ['Entrance', 'Hall', 'Kitchen', 'Dining Room', 'Lounge', 'Billiard Room','Library', 'Study', 'Gallery']

#room description prints when player first enters room, and when player looks around
rmDesc = [['This is the entrance', 1], ['This is the hall', 1], ['This is the kitchen', 1], ['This is the dining room', 1], ['This is the lounge', 1], ['This is the billiard room', 1], ['This is the library', 1], ['This is the study', 1], ['This is the gallery', 1]]

#indicates how rooms connect to each other [north, south, east, west]
rmMap = [[1, None, None, None], [8, 0, 6, 3], [None, 3, None, None], [2, 4, 1, None], [3, None, None, None], [None, 6, None, None], [5, 7, None, 1], [6, None, None, None], [None, 1, None, None]]

#divide possible inputs based on command type
north = ['north', 'n']
south = ['south', 's']
east = ['east', 'e']
west = ['west', 'w']
move = ['go'] + north + south + east + west
look = ['look', 'l']

#necessary presets; command input, game text, and initial room
plyrCom = None
text = ''
rmID = 0

def game():
    rm()
    while True:
        com()

game()
