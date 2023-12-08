import pygame

pygame.init()
W = 800
H = 600
Fenetre = pygame.display.set_mode((W, H))
pygame.display.set_caption("Jeu du Pendu")

def main_menu():
    pendu = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        Fenetre.fill((255, 255, 255))

        font = pygame.font.Font(None, 36)
        text = font.render("Jeu du Pendu", True, (0, 0, 0))
        text_rect = text.get_rect(center=(W // 2, 50))
        Fenetre.blit(text, text_rect)

        play_text = font.render("Jouer", True, (0, 0, 0))
        play_rect = play_text.get_rect(center=(W // 2, H // 2 - 50))
        play_button_rect = pygame.Rect(play_rect.left - 10, play_rect.top - 10, play_rect.width + 20, play_rect.height + 20)


        insert_text = font.render("Insérer un mot", True, (0, 0, 0))
        insert_rect = insert_text.get_rect(center=(W // 2, H // 2 + 30))
        insert_button_rect = pygame.Rect(insert_rect.left - 10, insert_rect.top - 10, insert_rect.width + 20, insert_rect.height + 20)

        if play_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), play_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), play_button_rect, 2) 

        Fenetre.blit(play_text, play_rect)

        if insert_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), insert_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), insert_button_rect, 2)

        Fenetre.blit(insert_text, insert_rect)

        if play_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            pendu = True
            return "play"
        elif insert_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return "insert"

        pygame.display.flip()

if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == "play":
            print("Lancer le jeu...")
        elif choice == "insert":
            print("Insérer un mot...")
