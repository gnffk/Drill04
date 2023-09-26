from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280,1024

open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('walking_woman.png')

global running,x_dir,y_dir, walking_motion

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT and event.key == SDLK_UP:
                x_dir = 1
                y_dir = 1
                walking_motion = 2
            elif event.key == SDLK_RIGHT and event.key == SDLK_DOWN:
                x_dir = 1
                y_dir = -1
                walking_motion = 0
            elif event.key == SDLK_RIGHT:
                x_dir = 1
                y_dir = 0
                walking_motion = 1
            elif event.key == SDLK_LEFT and event.key == SDLK_UP:
                x_dir = -1
                y_dir = 1
                walking_motion = 4
            elif event.key == SDLK_LEFT and event.key == SDLK_DOWN:
                x_dir = -1
                y_dir = -1
                walking_motion = 6
            elif event.key == SDLK_LEFT:
                x_dir = -1
                y_dir = 0
                walking_motion = 5
            elif event.key == SDLK_UP:
                x_dir = 0
                y_dir = 1
                walking_motion = 3
            elif event.key == SDLK_DOWN:
                x_dir = 0
                y_dir = -1
                walking_motion = 7
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            x_dir = 0
            y_dir = 0
            walking_motion = 0
            if event.key == SDLK_ESCAPE:
                running = False
pass

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
walking_motion = 0
dir =0
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame*100,walking_motion*187,100, 187,x,y)
    update_canvas()
    handle_events()
    frame = (frame+1)%13
    x += dir*5
    y += dir*5
    delay(0.05)




