from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280,1024

open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('walking_woman.png')

global running

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT and event.key == SDLK_UP:

            elif event.key == SDLK_RIGHT and event.key == SDLK_DOWN:

            elif event.key == SDLK_RIGHT:

            elif event.key == SDLK_LEFT and event.key == SDLK_UP:

            elif event.key == SDLK_LEFT and event.key == SDLK_DOWN:

            elif event.key == SDLK_LEFT:

            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT and event.key == SDLK_UP:

            elif event.key == SDLK_RIGHT and event.key == SDLK_DOWN:

            elif event.key == SDLK_RIGHT:

            elif event.key == SDLK_LEFT and event.key == SDLK_UP:

            elif event.key == SDLK_LEFT and event.key == SDLK_DOWN:

            elif event.key == SDLK_LEFT:

            elif event.key == SDLK_ESCAPE:
                running = False



