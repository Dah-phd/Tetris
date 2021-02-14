import tetris
import pygame as pg
import scoreing

pg.init()
klok = pg.time.Clock()

w = 600
h = 850
pad_w = 190
cube = pg.image.load('res\\cube.jpg')
pg.mixer.music.load('res\\tet.mp3')
pg.mixer.music.play(-1)


def draw(instance, grid):
    grid.fill((135, 206, 235))
    pg.draw.rect(grid, (0, 0, 0), (pad_w-10, 0, 10, h))
    pg.draw.rect(grid, (100, 100, 50), (pad_w-9, 0, 8, h))
    pg.draw.rect(grid, (0, 0, 0), (w-11, 0, 11, h))
    pg.draw.rect(grid, (100, 100, 50), (w-10, 0, 9, h))
    pg.draw.rect(grid, (100, 100, 50), (w-10, 0, 9, h))
    pg.draw.rect(grid, (0, 0, 0), (0, h-10, w, 1))
    pg.draw.rect(grid, (100, 100, 50), (0, h-9, w, 9))
    pg.draw.rect(grid, (0, 0, 0), (0, 0, pad_w-10, h-10))
    for num_row, row in enumerate(instance.board[4:]):
        for num_sq, sq in enumerate(row):
            if sq == 1:
                grid.blit(cube, (pad_w + 40*num_sq, 40*num_row))


def controls(instance):
    if pg.key.get_pressed()[pg.K_RIGHT]:
        instance.move_right()
    if pg.key.get_pressed()[pg.K_LEFT]:
        instance.move_left()
    if pg.key.get_pressed()[pg.K_DOWN]:
        instance.motion()
    if pg.key.get_pressed()[pg.K_UP] or pg.key.get_pressed()[pg.K_SPACE]:
        instance.flip()
    if pg.key.get_pressed()[pg.K_F4]:
        instance.prb()


def main():
    tet = tetris.engine()
    tet.start()
    grid = pg.display.set_mode((w, h))
    run = True
    move = 0
    while run:
        klok.tick(30)
        if move == 10:
            move = 0
            tet.motion()
        else:
            move += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            controls(tet)
        draw(tet, grid)
        pg.display.update()


if __name__ == '__main__':
    main()
    pg.quit()
