# template for "Stopwatch: The Game"
import simplegui

# define global variables
t=0 # stores time
time='' # stores time in string
suc = 0 # number of successes
alle = 0 # total number of presses


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t // 600
    B = t % 600 // 100
    C = t % 100 // 10 
    D = t % 10
    tmp = str(A) + ":" + str(B) + str(C) + "." + str(D)
    return tmp 
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
    
def stop_handler():
    global alle, suc
    if not timer.is_running():
        return
    timer.stop()
    alle += 1
    # increment only if stopped in +/- 0.1 of time 
    if str(t)[-1] in ['9','0','1'] and str(t)[-2] in ['4','0','5']:
        suc += 1

def reset_handler():
    global t, suc, alle
    t=0
    suc=0
    alle=0


# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t+=1

    
# define draw handler
def draw(c):
    time = format(t)
    c.draw_text(time, (120, 180), 96, "White")
    c.draw_text(str(suc)+' / '+str(alle), (400, 50), 36, "Aqua")
    c.draw_text("+/- 0.1 Stopping error is acceptable", (115, 270), 18, "Aqua")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 500, 300,100)


# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
frame.add_button('Start', start_handler, 100)
frame.add_button('Stop', stop_handler, 100)
frame.add_button('Reset', reset_handler, 100)


# start frame
frame.start()


# Please remember to review the grading rubric

