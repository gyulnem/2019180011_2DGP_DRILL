from pico2d import *

open_canvas()

character = load_image('character.png')

x = 0
frame = 0
while(x <800):
    clear_canvas()
    character.clip_draw(frame*82,0,82,100,x,90)
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.05)
    get_events()



close_canvas()