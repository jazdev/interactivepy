# implementation of card game - Memory

import simplegui
import random

#variables
c = [i % 8 for i in range(16)]
state = 0 
cardone = 0
cardtwo = 1
moves = 0

# helper function to initialize globals
def init():
    global state, deck_cards, moves
    deck_cards = [[c[0], False],[c[1], False],[c[2], False],[c[3], False],
    [c[4], False],[c[5], False],[c[6], False],[c[7], False],
    [c[8], False],[c[9], False],[c[10], False],[c[11], False],
    [c[12], False],[c[13], False],[c[14], False],[c[15], False]]
    
    # randomly shuffle
    random.shuffle(deck_cards)

    state = 0 
    moves = 0

     
# define event handlers
def mouseclick(pos):
    global state, deck_cards, cardone, cardtwo, moves

    if 0 <= pos[1] <= 100 and deck_cards[pos[0] // 50][1] == False: 
        # if the pos-y is within frame & card is down
        if state == 0:
            state = 1
            cardone = pos[0] // 50
            deck_cards[(pos[0] // 50)][1] = True
        elif state == 1:
            state = 2
            cardtwo = pos[0] // 50
            deck_cards[(pos[0] // 50)][1] = True
            moves += 1
        elif state == 2:
            state = 1
            if deck_cards[cardone][0] != deck_cards[cardtwo][0] :
                deck_cards[cardone][1] = False
                deck_cards[cardtwo][1] = False
            cardone = pos[0] // 50
            deck_cards[pos[0] // 50][1] = True    
          
            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck_cards, state
    l.set_text("Moves = " + str(moves))
    for c in range(len(deck_cards)):
        if deck_cards[c][1] == True:
            #draw card front
            canvas.draw_polygon([(c*50, 0), ((c+1)*50, 0), ((c+1)*50, 100), (c*50, 100)], 2,"White", "Orange")
            canvas.draw_polygon([(c*50+5, 10), ((c+1)*50-5, 10), ((c+1)*50-5, 90), (c*50+5, 90)], 2,"Black", "Silver")
            canvas.draw_text(str(deck_cards[c][0]), (c*50 + 10, 67), 50, "Black")
        elif deck_cards[c][1] == False:
            #draw card back
            canvas.draw_polygon([(c*50, 0), ((c+1)*50, 0), ((c+1)*50, 100), (c*50, 100)], 2,"White", "Teal")
            canvas.draw_polygon([(c*50+10, 20), ((c+1)*50-10, 20), ((c+1)*50-10, 80), (c*50+10, 80)], 2,"Silver", "Orange")
            canvas.draw_circle((c*50+25, 50), 8, 2, 'Blue', 'Red')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()

