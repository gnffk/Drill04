from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280,1024

open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('walking_woman.png')

global running,x_dir,y_dir

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT and event.key == SDLK_UP:
                x_dir = 1
                y_dir = 1
            elif event.key == SDLK_RIGHT and event.key == SDLK_DOWN:
                x_dir = 1
                y_dir = -1
            elif event.key == SDLK_RIGHT:
                x_dir = 1
                y_dir = 0
            elif event.key == SDLK_LEFT and event.key == SDLK_UP:
                x_dir = -1
                y_dir = 1
            elif event.key == SDLK_LEFT and event.key == SDLK_DOWN:
                x_dir = -1
                y_dir = -1
            elif event.key == SDLK_LEFT:
                x_dir = -1
                y_dir = 0
            elif event.key == SDLK_UP:
                x_dir = 0
                y_dir = 1
            elif event.key == SDLK_DOWN:
                x_dir = 0
                y_dir = -1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            x_dir = 0
            y_dir = 0
            if event.key == SDLK_ESCAPE:
                running = False
pass




