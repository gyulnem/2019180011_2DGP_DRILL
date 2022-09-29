from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
def handle_events():
    global running
    global dir_x
    global dir_y
    global on

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                on = 1
                dir_x += 1
            elif event.key == SDLK_LEFT:
                on = 0
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir_x = 0
dir_y = 0
on = 0

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if on == 1:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif on == 0:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    if x >= 0 and x <= KPU_WIDTH and y >= 0 and y<= KPU_HEIGHT:
        x += dir_x * 5
        y += dir_y * 5



close_canvas()
