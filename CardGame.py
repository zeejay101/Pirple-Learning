import random
from itertools import product
class Deck():
    suit = ('hearts', 'spades', 'diamond', 'clubs')
    ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight',
             'nine', 'ten', 'jack', 'queen', 'king', 'ace')
    values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7,
             'eight':8,'nine':9, 'ten':10, 'jack':11,
             'queen':12, 'king':13, 'ace':1,}
    def __init__(self):
        self.deck1 = list(product(Deck.suit,Deck.ranks))
        random.shuffle(self.deck1)
    def draw_card(self):
        if len(self.deck1) == 0:
            return 0
        else:
            return self.deck1.pop()
    def shuffle_deck(self):
        random.shuffle(self.deck1)
    def __str__(self):
        return str(self.deck1)

class Card(Deck):
    def __init__(self,deck):
        self.card = deck.draw_card()
        if self.card == 0:
            raise Exception('All card Dealt')
        self.suit = self.card[0]
        self.rank = self.card[1]
        self.value = self.values[self.rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    def getval(self):
        return self.value  
    
def sel_val():
    a = int(input('enter your number: \n'))
    if not a in range(1,201):
        print('enter number in 1 and 200')
        exit()
    b = random.randint(1,200)
    return a,b

def game(lst,deck):
    lst.append(Card(deck))
    return lst[-1].value

player,computer = sel_val()
pcount,ccount = 0,0

pllst = []
cmplst = []
dec = Deck()

while True:
    try:
        pcount += game(pllst,dec)
        if pcount == player:
            print(f'You Won!!!!')
            break
        ccount += game(cmplst,dec)
        if ccount == computer:
            print(f'You Lost, computer number was {computer}')
            break
 #       if pcount > player and ccount > computer:
            #raise Exception('No win possible')
    except Exception:
        print('It was a tie')
        if pcount > ccount:
            print(f'You won by tiebreaker, your score {pcount} was \
higher than computer {ccount}')
        else:
            print(f'You lost by tiebreaker, your score {pcount} was \
lower than computer {ccount}')
        break