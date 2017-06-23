#!/usr/bin/python
import random
fruits=[]
def get_random_word():
	fruits=["apple", "orange", "banana", "grapes", "strawberry", "blackberry", "blueberry", "kiwi", "cranberry", "fig", "raspberry"] 
	fruit=fruits[random.randint(0, len(fruits) - 1 )]
   	return fruit
def print_clue (random_fruit):
	for char in random_fruit:
		r_fruit[
def play_word_game ():
    strikes=0
    max_strikes=3
    playing= True
    random_word=get_random_word()
    while playing:
	print ("Enter a Fruit Name:")
	user_word=raw_input()
	if user_word == random_word:
	  print "Great Guess!!!"
	  break
	else:
	  print ("Didnt work. Try again!")
	strikes+=1
	if strikes >= max_strikes:
		playing=False
    if strikes >=max_strikes:
	print ("The Fruit is " + random_word)
	print ("Loser!")
    else:
	print ("Winner!!!")

    

###Main

print ("Welcome to the Word Game")
play_word_game()
print ("Thank you")
