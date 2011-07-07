#!/usr/bin/python

# "_why the lucky swordfight" by Natan Yellin
# inspired by _why's presentation at Carnegie Melon: http://vimeo.com/5047563
# some comments written by kids

# you can write whatever you want after #blahblahBLAH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import os
import sys
import time

phrases = ["Your father\n was a hamster!",
		"You smell like\n socks!",
		"My grandmother\ncan fight better!",
		"No, YOUR father\nwas a hamster!"]

head 	=  r" ~O  O~ "

waists	= [r" <|/\|> ",
	   r" <|--|> ",
           r" <|\/|> ",
           r" <|--|> "]

legs 	= [r" /\  |\ ",
	   r" /\  /\  ",
	   r" /|  /\ ",
	   r" /\ /\  "]

spaces 	= ["  ",
	   "     ",
	   "    ",
	   "   "]

def clear_screen ():
	if sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")
	return

i = 0
# do stuff forever
while 1:
	# clear the screen
	clear_screen()
	
	s = spaces[i]
	print ""
	print phrases[i]
	print ""
	print s + head
	print s + waists[i]
	print s + legs[i]
	
	# wait one second
	time.sleep(1.0)
	
	i = i + 1
	if i == 4:
		i = 0
