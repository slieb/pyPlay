import itertools, random
import numpy as np
import pandas as pd

# basic use of itertools to make and shuffle a deck of cards
print ("Playing with a deck of cards...")
deck = list(itertools.product(['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                               'Jack', 'Queen', 'King'],
                              ['Spades', 'Hearts', 'Clubs', 'Diamonds']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print ("You got:")
for i in range(5):
    print "\t %s of %s" % (deck[i][0], deck[i][1])


# playing around with pandas
print ("\n\n\nPlaying with pandas...")
data = {
    'Name': ["John", "Paul", "George", "Ringo"],
    'Location': ["NY", "LN", "HK", "TK"],
    'Age': [22, 23, 24, 25]
}

dp = pd.DataFrame(data)
print dp