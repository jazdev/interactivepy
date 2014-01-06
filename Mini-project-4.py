# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0.0, 0.0]


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2] 
    # random velocities
    rand_x = random.randrange(120, 240)/60.0
    rand_y = random.randrange(60, 180)/60.0
    if direction == LEFT:
        ball_vel = [-rand_x, -rand_y]
    else:
        ball_vel = [ rand_x, -rand_y]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = HEIGHT / 2  
    paddle2_pos = HEIGHT / 2  
    paddle1_vel = 0  
    paddle2_vel = 0  
    score1 = 0  
    score2 = 0  
    if score1 >= score2:  
        spawn_ball(LEFT)  
    else:  
        spawn_ball(RIGHT)
    

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0] 
    ball_pos[1] += ball_vel[1] 
    
    # top and bottom checking
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= HEIGHT - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
        
    # left and right checking
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:    
        if paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1]<=paddle1_pos + HALF_PAD_HEIGHT:    
            ball_vel[0] = -ball_vel[0]    
            ball_vel[0] = ball_vel[0] * 1.1    
            ball_vel[1] = ball_vel[1] * 1.1    
        else:    
            spawn_ball(RIGHT)    
            score2 += 1
            
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:    
        if paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:    
            ball_vel[0] = -ball_vel[0]    
            ball_vel[0] = ball_vel[0] * 1.1    
            ball_vel[1] = ball_vel[1] * 1.1    
        else:    
            spawn_ball(LEFT)    
            score1 += 1    
            
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 3, 'White', 'Gray')
    
    # update paddle's vertical position, keep paddle on the screen
    if HALF_PAD_HEIGHT <= paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT:  
        paddle1_pos += paddle1_vel 
        
    if HALF_PAD_HEIGHT <= paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT:  
        paddle2_pos += paddle2_vel
    
    # draw paddles
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "White")     
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],  PAD_WIDTH, "White")
    
    # draw scores
    c.draw_text(str(score1)+"  |  "+str(score2), (WIDTH / 2 - 40, 40), 36, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 4  
    if key == simplegui.KEY_MAP['s']:    
        paddle1_vel = vel    
    elif key == simplegui.KEY_MAP['w']:    
        paddle1_vel = -vel    
    elif key == simplegui.KEY_MAP['up']:    
        paddle2_vel = -vel    
    elif key == simplegui.KEY_MAP['down']:    
        paddle2_vel = vel   
     
def keyup(key):  
    global paddle1_vel, paddle2_vel  
    if key == simplegui.KEY_MAP['s']:    
        paddle1_vel = 0    
    elif key == simplegui.KEY_MAP['w']:    
        paddle1_vel = 0    
    elif key == simplegui.KEY_MAP['up']:    
        paddle2_vel = 0    
    elif key == simplegui.KEY_MAP['down']:    
        paddle2_vel = 0  

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
# reset game
frame.add_button("Reset Game", new_game)

# start frame
new_game()
frame.start()

