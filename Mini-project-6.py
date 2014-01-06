# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand=[]	# create Hand object

    def __str__(self):
        # return a string representation of a hand
        s = 'Hand contains '
        for card in self.hand:
            s = s + str(card) + ' '
        return s

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        for card in self.hand:
            rank = card.get_rank()
            hand_value += VALUES[rank]
            
        for card in self.hand: 
            rank = card.get_rank()
            if rank == 'A' and hand_value <= 11:
                hand_value += 10
                
        return hand_value
  
    def draw(self, canvas, p):
        #draw's on canvas
        pos = p
        for card in self.hand:
            card.draw(canvas, p)
            pos[0] = pos[0] + 90
        if in_play == True:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [115.5,184], CARD_BACK_SIZE)     

        
# define deck class 
class Deck:
    def __init__(self):
        deal = []
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.shuffle()
        
    def __str__(self):
        s = 'Deck contains '
        for c in self.cards:
            s = s + str(c) + ' '
        return s

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        deal = self.cards.pop(0)
        return deal



#define event handlers for buttons
def deal():
    # deals player a new hand & ends hand if it causes a bust.
    global outcome, in_play
    global in_play, player, dealer, deck, message, score, outcome
    if in_play == True:
        # if player clicks Deal button during a hand, player loses hand in progress
        message = "Here is the new hand"
        score -= 1
        deck = Deck()
        player = Hand()
        dealer = Hand()
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
    if in_play == False:
        # starts a new hand
        deck = Deck()
        player = Hand()
        dealer = Hand()
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        message = "New Hand. Hit or Stand?"
    in_play = True
    outcome = ""


def hit():
    # hits dealer until >=17 or busts. 
    global in_play, score, message
    if in_play == True:
        player.add_card(deck.deal_card())
        message = "Hit or Stand?"
        if player.get_value() > 21:
            in_play = False
            message = "Player busted! You Lose! Play again?"
            score -= 1
            outcome = "Dealer: " + str(dealer.get_value()) + "  Player: " + str(player.get_value())

       
def stand():
    global in_play, score, message, outcome
    if in_play == False:
        message = "The hand is already over. Deal again."
    else:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            message = "Dealer busted. You win! Play again?"
            score += 1
            in_play = False
            
        elif dealer.get_value() > player.get_value():
            message = "Dealer wins! Play again?"
            score -= 1
            in_play = False
        
        elif dealer.get_value() == player.get_value():
            message = "Tie! Dealer wins! Play again?"
            score -= 1
            in_play = False
        
        elif dealer.get_value() < player.get_value():
            message = "You win! Play again?"
            score += 1
            in_play = False
            
        outcome = "Dealer: " + str(dealer.get_value()) + "  Player: " + str(player.get_value())
        
def exit():
    #exit's frame
    frame.stop()
    
    
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", [220,50], 48, "Yellow")
    canvas.draw_text("Score : " + str(score), [80,530], 36, "Orange")
    canvas.draw_text("Dealer :", [80,110], 30, "LightGray")
    canvas.draw_text("Player :", [80,300], 30, "LightGray")
    canvas.draw_text(message, [200,480], 26, "LightGray")
    canvas.draw_text(outcome, [80,560], 28, "White")
    dealer.draw(canvas, [80,135])
    player.draw(canvas, [80,325])



# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.add_button("Exit", exit, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
