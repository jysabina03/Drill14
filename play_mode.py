from pico2d import *
import game_framework

import game_world
from bird import Bird
from grass import Grass
from boy import Boy

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global grass
    global boy
    global bird
    running = True

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)


    for i in range(0, 10):
        if i<5:
            bird = Bird(400+(i)*50, 400+(5-i)*20, 1)
        else:
            bird = Bird(400+(i-6)*50, 320+(i-5)*20, 1)

        game_world.add_object(bird)

def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    #delay(1)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

