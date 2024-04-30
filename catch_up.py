from pygame import *

window  = display.set_mode((700, 500))
display.set_caption('Dogonyalki')
background = transform.scale(image.load('background.png'), (700,500))

game = True
clock = time.Clock()
FPS = 144
x1 = 100
y1 = 200
x2 = 300
y2 = 400
sprite1 = transform.scale(image.load('sprite1.png'), (100,100))
sprite2 = transform.scale(image.load('sprite2.png'), (100,100))
while game:
    window.blit(background, (0,0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            game = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_s] and y2 < 600:
        y1 += 10

    if keys_pressed[K_a] and x1 > 0:
        x1 -= 10

    if keys_pressed[K_w] and y1 > 0:
        y1 -= 10

    if keys_pressed[K_d] and x2 < 600:
        x1 += 10

    if keys_pressed[K_UP]:
        y2 -= 10

    if keys_pressed[K_DOWN]:
        y2 += 10

    if keys_pressed[K_RIGHT]:
        x2 += 10
    
    if keys_pressed[K_LEFT]:
        x2 -= 10
    
    clock.tick(FPS)
    display.update()