import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
szybkosc = 1000
dt = 0
ruch_pilki_x = -szybkosc
ruch_pilki_y = -szybkosc

player_rect1 = pygame.Rect(0, screen.get_height() / 2 - 85, 40, 170)
player_rect2 = pygame.Rect(screen.get_width() - 40, screen.get_height() / 2 - 85, 40, 170)
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

player1_score = 0
player2_score = 0
max_score = 20  # Maksymalny wynik, po którym gra się kończy

font = pygame.font.Font(None, 36)  # Tworzenie obiektu czcionki
font.render("Przykładowy tekst", True, (255, 0, 0))
#-------------------------------------------------------------
# glowna petla programu

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    ball_rect = pygame.Rect(ball_pos.x - 40, ball_pos.y - 40, 80, 80)

    pygame.draw.rect(screen, "red", player_rect1)
    pygame.draw.rect(screen, "blue", player_rect2)
    pygame.draw.circle(screen, "red", ball_pos, 40)

    # Rysowanie napisów z wynikami
    score_text1 = font.render("Gracz 1: " + str(player1_score), True, (0, 0, 0))
    score_text2 = font.render("Gracz 2: " + str(player2_score), True, (0, 0, 0))
    screen.blit(score_text1, (20, 20))
    screen.blit(score_text2, (screen.get_width() - score_text2.get_width() - 20, 20))

# -------------------------------------------------------------
# poruszanie
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if (player_rect1.y > 0):
            player_rect1.y -= szybkosc * dt
    if keys[pygame.K_s]:
        if (player_rect1.y < 550):
            player_rect1.y += szybkosc * dt


    if keys[pygame.K_k]:
        if (player_rect2.y > 0):
            player_rect2.y -= szybkosc * dt
    if keys[pygame.K_m]:
        if (player_rect2.y < 550):
            player_rect2.y += szybkosc * dt



    ball_pos.x += ruch_pilki_x * dt
    ball_pos.y += ruch_pilki_y * dt
   #player_rect2.y = ball_pos.y - 80

    if ball_pos.y < 40:
        ruch_pilki_y = szybkosc

    if ball_pos.y > 680:
        ruch_pilki_y = -szybkosc

# -------------------------------------------------------------
# odbicie paletka

    if player_rect1.colliderect(ball_rect):
        if ruch_pilki_y > 0:
            ruch_pilki_x = szybkosc
        elif ruch_pilki_y < 0:
            ruch_pilki_x = szybkosc

    if player_rect2.colliderect(ball_rect):
        if ruch_pilki_y > 0:
            ruch_pilki_x = -szybkosc
        elif ruch_pilki_y < 0:
            ruch_pilki_x = -szybkosc
#-------------------------------------------------------------
#bramka

    if ball_pos.x < 0:
        player2_score += 1
        if player2_score >= max_score:
            running = False
        else:
            ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
            ruch_pilki_x = -szybkosc
            ruch_pilki_y = -szybkosc

    if ball_pos.x > 1285:
        player1_score += 1
        if player1_score >= max_score:
            running = False
        else:
            ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
            ruch_pilki_x = -szybkosc
            ruch_pilki_y = -szybkosc
# -------------------------------------------------------------
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
