#print "Welcome to Hangman!!! Prepare to die"
# variables lives, word , guess

# hello _ _ _ _ _
'''
while(lives>0)
    guess =input("Enter a letter")
    guess ka list
    if(guess not in word):
        lives-=1

    for (Its part of the length of word)
        if iterator in guess
            print guess
        else:
            print "_"


 lives=6
 hello _ _ _ _ _
 h _ _ _ _
 3

'''
'''
Samarth and Sparsh's Hangman

print "hangman game"
lives=6
word="github"
n="_"
l=list(n*len(word))
print "\n",l,
count=0
while(lives>0):
    guess=raw_input("\n enter the guess")
    if guess not in word:
        lives=lives-1
        print "now lives are =",lives
    for i in word:
        if(guess==i):
            print guess
            l[word.index(guess)]=guess
            print l
            count=count+1
    if count==len(word):
        print "you win"
        break
if(lives==0):
    print "you lose"

'''

'''
Anjali's Hangman

import random

user = input("Enter username:  ")

print('welcome ' + user)

print('Let\'s play Hangman')

print("Start.....")

a = ["python", "hello", "welcome", "nice"]

w = random.choice(a)

word = list(w)

list1 = []

# print(word)

lives = 5

length = 0

print('_ ' * len(w))

print('Guess letters to find the word')

while (lives > 0 and len(w) != length):

    guess = input()

    if guess not in list1:

        if (guess in word):

            n = word.count(guess)

            length = length + n

            list1.append(guess)

            print('spaces left=>')

            print('_ ' * (len(w) - length))

        else:

            lives = lives - 1

            print("left lives: ", lives)

    else:

        print('You have already choose letter ' + guess + ' choose different letter')

if (lives == 0):

    print("You Loss")

    print("word was: " + w)

else:

    print("You win")

'''



    
