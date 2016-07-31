import itertools, random

# make a deck of cards
deck = list(itertools.product(['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                               'Jack', 'Queen', 'King'],
                              ['Spades', 'Hearts', 'Clubs', 'Diamonds']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print ("You got:")
for i in range(5):
    print "%s of %s" % (deck[i][0], deck[i][1])
