import pygame
import random

pygame.init()
W = 800
H = 600
Fenetre = pygame.display.set_mode((W, H))
pygame.display.set_caption("Jeu du Pendu")

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        Fenetre.fill((255, 255, 255))

        text = pygame.font.Font(None, 36).render("Jeu du Pendu", True, (0, 0, 0))
        text_rect = text.get_rect(center=(W // 2, H // 4))
        Fenetre.blit(text, text_rect)

        play_text = pygame.font.Font(None, 36).render("Jouer", True, (0, 0, 0))
        play_rect = play_text.get_rect(center=(W // 2, H // 2 - 50))
        play_button_rect = pygame.Rect(W // 2- 150, play_rect.top - 10, 300, play_rect.height + 20)

        if play_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), play_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), play_button_rect, 2)

        Fenetre.blit(play_text, play_rect)

        insert_text = pygame.font.Font(None, 36).render("Insérer un mot", True, (0, 0, 0))
        insert_rect = insert_text.get_rect(center=(W // 2, H // 2 + 30))  
        insert_button_rect = pygame.Rect(W // 2 - 150, insert_rect.top - 10, 300, insert_rect.height + 20)

        if insert_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), insert_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), insert_button_rect, 2)

        Fenetre.blit(insert_text, insert_rect)

        score_text = pygame.font.Font(None, 36).render("Score", True, (0, 0, 0))
        score_rect = play_text.get_rect(center=(W // 2, H // 2 + 100))
        score_button_rect = pygame.Rect(W // 2- 150, score_rect.top - 10, 300, score_rect.height + 20)

        if score_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), score_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), score_button_rect, 2)

        Fenetre.blit(score_text, score_rect)

        if play_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return play()
        elif insert_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return insert_word()

        pygame.display.flip()

def insert_word():
    input_width = 300
    input_height = 36
    input_rect = pygame.Rect((W - input_width) // 2, (H - input_height) // 2, input_width, input_height)
    user_input = ""
    input_active = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_input.strip():
                        with open("mots.txt", "a") as file:
                            file.write(user_input + "\n")
                            print(f"Le mot '{user_input}' a été ajouté à la liste")
                            user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        Fenetre.fill((255, 255, 255))

        titreAdd = pygame.font.Font(None, 36).render("Le Pendu : Ajouter un mot", True, (0, 0, 0))
        titreAdd_rect = titreAdd.get_rect(center=(W // 2, 50))
        Fenetre.blit(titreAdd, titreAdd_rect)

        titreInput = pygame.font.Font(None, 30).render("Insérer un mot ci-dessous", True, (0, 0, 0))
        titreInput_rect = titreInput.get_rect(center=(W // 2, (H - input_height) // 2 - 20))
        Fenetre.blit(titreInput, titreInput_rect)

        pygame.draw.rect(Fenetre, (0, 0, 0), input_rect, 2) if input_active else None
        input_surface = pygame.font.Font(None, 36).render(user_input, True, (0, 0, 0))
        input_surface_rect = input_surface.get_rect(center=input_rect.center)
        Fenetre.blit(input_surface, (input_surface_rect.x + 5, input_surface_rect.y))

        save_text = pygame.font.Font(None, 36).render("Enregistrer le mot", True, (0, 0, 0))
        save_button_rect = pygame.Rect(W // 2 - 125 , (H - input_height) // 2 + 50, 250, 40)

        if save_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), save_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), save_button_rect, 2)

        save_text_rect = save_text.get_rect(center=save_button_rect.center)
        Fenetre.blit(save_text, save_text_rect)

        back_text = pygame.font.Font(None, 36).render("Retour au Menu", True, (0, 0, 0))
        back_button_rect = pygame.Rect(W // 2 - 125, H  // 2 +220, 250, 40)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)

        if back_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), back_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), back_button_rect, 2)

        Fenetre.blit(back_text, back_text_rect)

        if save_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            if user_input.strip():  
                with open("mots.txt", "a") as file:
                    file.write(user_input + "\n")
                    print(f"Le mot '{user_input}' a été ajouté à la liste")
                    user_input = ""
        elif back_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return "back"

        pygame.display.flip()
def mots_alea():
    global solution
    with open("mots.txt", "r") as file:
        words = file.readlines()
        solution = random.choice(words).strip()
        print(f"Selected word: {solution}")
def play():
    global solution

    mots_alea()

    guessed_letters = ['_' for _ in solution]
    attempts = 0
    pendu_images = [f"img/{i}.png" for i in range(1, 9)]
    show_message = False
    lettres_utilisees = []
    mauvaises_lettres = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and not show_message:
                if event.key in range(pygame.K_a, pygame.K_z + 1):
                    guessed_letter = chr(event.key).lower()

                    if guessed_letter not in lettres_utilisees:
                        lettres_utilisees.append(guessed_letter)

                        if guessed_letter in solution:
                            for i, letter in enumerate(solution):
                                if letter == guessed_letter:
                                    guessed_letters[i] = guessed_letter

                            if '_' not in guessed_letters:
                                show_message = True
                                message_gagne = pygame.font.Font(None, 36).render("Bravo, vous avez trouvé le mot.", True, (0, 250, 0))
                                message_gagne_rect = message_gagne.get_rect(center=(W // 2, 100))
                                break
                        else:
                            mauvaises_lettres.append(guessed_letter)
                            attempts += 1

                            if attempts == 7:
                                show_message = True
                                message_echec = pygame.font.Font(None, 36).render("Vous avez atteint le nombre maximum d'essais.", True, (255, 0, 0))
                                solution_echec = pygame.font.Font(None, 32).render(f"Le mot était {solution}", True, (255, 0, 0))
                                message_echec_rect = message_echec.get_rect(center=(W // 2, 150))
                                solution_echec_rect = solution_echec.get_rect(center=(W // 2, 180))
                                break

        Fenetre.fill((255, 255, 255))

        mauvaises_lettres_text = pygame.font.Font(None, 36).render(f"Tentatives : {attempts}/7", True, (255, 0, 0))
        Fenetre.blit(mauvaises_lettres_text, (50, 100))

        for i, lettre in enumerate(mauvaises_lettres):
            lettre_text = pygame.font.Font(None, 36).render(lettre, True, (255, 0, 0))
            Fenetre.blit(lettre_text, (50, 180 + i * 40))

        game_title = pygame.font.Font(None, 36).render("Le Pendu", True, (0, 0, 0))
        game_title_rect = game_title.get_rect(center=(W // 2, 50))
        Fenetre.blit(game_title, game_title_rect)

        if attempts < len(pendu_images):
            pendu_image = pygame.image.load(pendu_images[attempts])
            Fenetre.blit(pendu_image, (W // 2 - pendu_image.get_width() // 2, 225))

        word_display = ' '.join(guessed_letters)
        word_display_text = pygame.font.Font(None, 60).render(word_display, True, (0, 0, 0))
        word_display_rect = word_display_text.get_rect(center=(W // 2, H // 2 + 180))
        Fenetre.blit(word_display_text, word_display_rect)

        return_button_rect = pygame.Rect(W // 2 - 125, H // 2 + 220, 250, 40)

        return_text = pygame.font.Font(None, 36).render("Retour au Menu", True, (0, 0, 0))
        if return_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), return_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), return_button_rect, 2)

        return_text_rect = return_text.get_rect(center=return_button_rect.center)
        Fenetre.blit(return_text, return_text_rect)

        if show_message:
            if attempts == 7:
                Fenetre.blit(message_echec, message_echec_rect)
                Fenetre.blit(solution_echec, solution_echec_rect)
            elif '_' not in guessed_letters:
                Fenetre.blit(message_gagne, message_gagne_rect)

        if return_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return

        pygame.display.flip()
# def score():
#     if 
while True:
    main_menu()
