from pygame import *

class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class rocket1 (GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if kyes[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[k_s] and self.rect.y <5:
            self.rect.y -= self.speed
    
class rocket2(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if kyes[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[k_DOWN] and self.rect.y <5:
            self.rect.y -= self.speed





clock = time.Clock()
FPS = 60
#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-pong")
background = transform.scale(image.load("space.png"), (win_width, win_height))


roc1 = rocket1('zhongli.png', 5, win_height - 80, 4)
roc2 = rocket2('diluc.png', win_width - 80, 280, 2)
ball = ball('wish.png', 0, 0)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

display.update()
clock.tick(FPS)