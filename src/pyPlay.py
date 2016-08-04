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


# playing around with data containers
print ("\n\n\nPlaying with data containers...")
student_data = [
    {'name': 'Bob', 'id':0, 'scores':[68,75,56,81]},
    {'name': 'Alice', 'id':1,  'scores':[75, 90, 64, 88]},
    {'name': 'Carol', 'id':2, 'scores':[59, 74, 71, 68]},
    {'name': 'Dan', 'id':3, 'scores':[64, 58, 53, 62]},
]

def process_student_data (data, pass_threshold=60, merit_threshold=75):
    for sdata in data:
        av = sum(sdata['scores']) / float(len(sdata['scores']))
        sdata['average'] = av
        if av > merit_threshold:
            sdata['assessment'] = 'passed with merit'
        elif av > pass_threshold:
            sdata['assessment'] = 'passed'
        else:
            sdata['assessment'] = 'failed'
        print("%s's (id: %d) final assessment is: %s" % (sdata['name'], sdata['id'], sdata['assessment'].upper()))

process_student_data (student_data)