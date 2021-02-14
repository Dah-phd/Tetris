import tetris
import pygame as pg

pg.init()
klok = pg.time.Clock()

w = 400
h = 850


def draw(instance, grid):
    grid.fill((0, 0, 0))
    for num_row, row in enumerate(instance.board[4:]):
        for num_sq, sq in enumerate(row):
            if sq == 1:
                pg.draw.rect(grid, (200, 20, 20),
                             ((40*num_sq, 40*num_row), (40, 40)))


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
