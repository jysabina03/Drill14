from pico2d import *

import game_framework
import game_world


# bird Run Speed
PIXEL_PER_METER = (10.0/ 0.3) # 10 pixel = 30 cm
FLY_SPEED_KMPH = 40.0 # Km/Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH*1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)


# bird Action Speed

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0
        self.dir = 0

    def draw(self):
        now_frame = int(self.frame)
        if self.dir>0:
            if now_frame < 5:
                self.image.clip_composite_draw(int(self.frame)%5 * 183, 0, 183,168, 0,'', self.x, self.y,183,168)
            elif now_frame < 10:
                self.image.clip_composite_draw(int(self.frame)%5 * 183, 168, 183,168, 0,'', self.x, self.y,183,168)
            else:
                self.image.clip_composite_draw(int(self.frame)%5 * 183, 168*2, 183,168, 0,'', self.x, self.y,183,168)
        else:
            if now_frame < 5:
                self.image.clip_composite_draw(int(self.frame)%5 * 183, 0, 183,168, 0,'v', self.x, self.y,183,168)
            elif now_frame < 10:
                self.image.clip_composite_draw(int(self.frame)%5 * 183, 168, 183,168, 0,'v', self.x, self.y,183,168)
            else:
                self.image.clip_composite_draw(int(self.frame)%5 * 183, 168*2, 183,168, 0,'v', self.x, self.y,183,168)



    def update(self):

        self.frame = (self.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time)%14
        self.x+=self.dir*FLY_SPEED_PPS*game_framework.frame_time

        if self.x < 25 or self.x > 1600 - 25:
            self.dir*=-1
