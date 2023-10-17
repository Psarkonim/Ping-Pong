from pygame import *
from random import randint
import time as t

init()
mixer.init()
font.init()

window = display.set_mode((700, 500))
display.set_caption('Ping-pong')

clock = time.Clock()
bg = transform.scale(image.load('kort.png'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, img: str, speed: int):
        super().__init__()
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def is_collide(self, obj):
        return self.rect.colliderect(obj)



class Player(GameSprite):
    def update_2(self):
        key_pressed = key.get_pressed()
        
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed
    
    def update_1(self):
        key_pressed = key.get_pressed()
        
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 300:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, x: int, y: int, width: int, height: int, img: str, speed: int):
        super().__init__(x, y, width, height, img, speed)
        self.speed_x = speed
        self.speed_y = speed

    def update(self):
        ball.rect.x += self.speed_x
        ball.rect.y += self.speed_y
        
racket_1 = Player(50, 0, 50, 200, 'platf.png', 6)
racket_2 = Player(600, 0, 50, 200, 'platf.png', 6)
ball = Ball(250, 250, 50, 50, 'ball_1.png', 3)
font_1 = font.SysFont('Times New Roman', 40)
win_1_font = font_1.render('Первый игрок выиграл', True, (100, 100, 100))
win_2_font = font_1.render('Второй игрок выиграл', True, (100, 100, 100))

game = True
finish = False

while game:
    for evnt in event.get():
        if evnt.type == QUIT:
            game = False
    
    if not finish:
        window.blit(bg, (0, 0))

        racket_1.update_1()
        racket_2.update_2()
        ball.update()

        racket_1.draw()
        racket_2.draw()
        ball.draw()

        if ball.rect.y < 0:
            ball.speed_y *= -1
        elif ball.rect.y > 450:
            ball.speed_y *= -1
        elif ball.is_collide(racket_1.rect) or ball.is_collide(racket_2.rect):
            ball.speed_x *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(win_1_font, (130, 250))
        elif ball.rect.x > 650:
            finish = True
            window.blit(win_2_font, (130, 250))


    display.update()
    clock.tick(60)