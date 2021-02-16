import tetris
import pygame as pg
import scoring


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
    grid.blit(font.render('SCORE:', True, (255, 255, 255)), (20, 60))
    grid.blit(font.render(str(instance.score),
                          True, (255, 255, 255)), (20, 100))
    grid.blit(font.render('Player:', True, (255, 255, 255)), (20, 160))
    grid.blit(font.render(str(new_score.name),
                          True, (255, 255, 255)), (20, 200))
    for square in instance.blocks[instance.que].values():
        grid.blit(cube, (square[0]*40-30, 220+square[1]*40))
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


def pre():
    grid = pg.display.set_mode((w, h))
    run = True
    hs = new_score.quarry()
    name = ''
    while run:
        klok.tick(30)
        grid.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    new_score.name = name
                    run = False
                    pg.display.quit()
                    main()
                elif event.key == pg.K_ESCAPE:
                    run = False
                elif event.key == pg.K_BACKSPACE:
                    name = name[:-1]
                else:
                    if len(name) < 20:
                        name += event.unicode
        grid.blit(font.render('Player name:', True, (255, 255, 255)), (20, 20))
        grid.blit(font.render(str(name), True, (255, 255, 255)), (20, 60))
        grid.blit(font.render('HIGH SCORES:', True, (255, 255, 255)), (20, 100))
        if hs:
            for position, score in enumerate(hs[:10 if len(hs) > 10 else len(hs)]):
                grid.blit(font.render(str(position+1), True,
                                      (255, 255, 255)), (20, 160+position*40))
                grid.blit(font.render(score[0], True,
                                      (255, 255, 255)), (70, 160+position*40))
                grid.blit(font.render(str(score[1]), True,
                                      (255, 255, 255)), (420, 160+position*40))

        pg.display.update()


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
            if event.type == pg.QUIT or event.type == pg.K_ESCAPE:
                run = False
            controls(tet)
        draw(tet, grid)
        if not tet.alive:
            new_score.new_score(tet.score)
            run = False
        pg.display.update()
    pre()


if __name__ == '__main__':
    pg.init()
    klok = pg.time.Clock()
    font = pg.font.SysFont('Times New Roman', 33)
    w = 600
    h = 850
    pad_w = 190
    cube = pg.image.load('res\\cube.jpg')
    pg.mixer.music.load('res\\tet.mp3')
    pg.mixer.music.play(-1)
    new_score = scoring.highscore('res\\save')
    pre()
    pg.quit()
