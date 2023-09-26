from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('womanSprite.png')

def handle_events():
    global running, x_dir, y_dir, walking_motion
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                x_dir = -1
                walking_motion = 5
            elif event.key == SDLK_RIGHT:
                x_dir = 1
                walking_motion = 1
            elif event.key == SDLK_UP:
                y_dir = 1
                walking_motion = 3
            elif event.key == SDLK_DOWN:
                y_dir = -1
                walking_motion = 7

            if x_dir == 1 and y_dir == 1:
                walking_motion = 2
            elif x_dir == -1 and y_dir == 1:
                walking_motion = 4
            elif x_dir == 1 and y_dir == -1:
                walking_motion =0
            elif x_dir == -1 and y_dir == -1:
                walking_motion = 6
        elif event.type == SDL_KEYUP:
            x_dir = 0
            y_dir = 0

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
walking_motion = 0
x_dir = 0
y_dir = 0
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 48, walking_motion * 92, 48, 92, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 13
    x += x_dir * 5
    y += y_dir * 5

    if x < 0:
        x = 0
    elif x > TUK_WIDTH:
        x = TUK_WIDTH
    if y < 0:
        y = 0
    elif y > TUK_HEIGHT:
        y = TUK_HEIGHT

    delay(0.05)
