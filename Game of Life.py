from microbit import *
from random import randint
 
def draw_universe( universe ):
    for y in range(0, 5):
        for x in range(0, 5):
            display.set_pixel(x, y, universe[x + y * 5])
 
def evolve( universe ):
    next_universe = []
    for y in range(0, 5):
        for x in range(0, 5):
            cell_neighbours = count_neighbours(universe, x, y)
            cell_is_alive = (cell_state(universe, x, y) == 1)
            if cell_is_alive and cell_neighbours < 2:
                next_universe.append(0)
            elif cell_is_alive and (cell_neighbours == 2 or cell_neighbours == 3):
                next_universe.append(9)
            elif cell_is_alive and cell_neighbours > 3:
                next_universe.append(0)
            elif not cell_is_alive and cell_neighbours == 3:
                next_universe.append(9)
            else:
                next_universe.append(0)
    return next_universe
 
def cell_state(universe, x, y):
    state = 1
    if universe[x + 5 * y] == 0:
        state = 0
    return state
 
def count_neighbours(universe, x, y):
    neighbours = -cell_state(universe, x, y)
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            neighbours += cell_state(universe, (x + dx) % 5, (y + dy) % 5)
    return neighbours
 
 
current_universe = [ 0, 0 ,0 ,0 ,0,
                     0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0,]
 
 
mode = "CONFIG"
display.scroll(mode)
 
while True:
 
    if mode == "RUN":
        current_universe = evolve( current_universe )
 
        if button_b.is_pressed():
            mode = "REVISE"
            display.scroll(mode)

        if display.read_light_level() < 5:
            mode = "CONFIG"
            display.scroll(mode)            
 
 
    if mode == "CONFIG":
 
        is_shake = (accelerometer.current_gesture() == "shake")
         
        if is_shake:

            state = []
            while len(state) < 25:

                state.append(randint(0,1)*9)
                
            current_universe = state

        else:
            pass
        
        if button_b.is_pressed():
            mode = "RUN"
            display.scroll(mode)


    if mode == "REVISE":
        pass
 
    
    
    
    draw_universe( current_universe )
    
    sleep(1000)