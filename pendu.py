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

        text = pygame.font.Font(None, 80).render("Jeu du Pendu", True, (0, 0, 0))
        text_rect = text.get_rect(center=(W // 2, 55))
        Fenetre.blit(text, text_rect)

        play_text = pygame.font.SysFont(None, 50, italic=True).render("Jouer", True, (0, 0, 0))
        play_rect = play_text.get_rect(center=(W // 2, H // 2 -100))
        play_button_rect = pygame.Rect(W // 2- 150, play_rect.top - 25, 300, 80)

        if play_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), play_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), play_button_rect, 2)

        Fenetre.blit(play_text, play_rect)

        insert_text = pygame.font.SysFont(None, 50, italic=True).render("Insérer un mot", True, (0, 0, 0))
        insert_rect = insert_text.get_rect(center=(W // 2, H // 2 + 20))  
        insert_button_rect = pygame.Rect(W // 2 - 150, insert_rect.top - 25, 300, 80)

        if insert_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), insert_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), insert_button_rect, 2)

        Fenetre.blit(insert_text, insert_rect)

        score_text = pygame.font.SysFont(None, 50, italic=True).render("Score", True, (0, 0, 0))
        score_rect = play_text.get_rect(center=(W // 2, H // 2 + 140))
        score_button_rect = pygame.Rect(W // 2- 150, score_rect.top - 25, 300, 80)

        if score_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), score_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), score_button_rect, 2)

        Fenetre.blit(score_text, score_rect)

        if play_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            player_name, difficulty = username()
            if player_name and difficulty:
                play(player_name, difficulty)

        elif insert_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            insert_word()

        elif score_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            score_result = score()
            if score_result == "back":
                break

        pygame.display.flip()

def username():
    input_rect = pygame.Rect(W // 2 - 200, H // 2, 400, 80)
    font = pygame.font.Font(None, 60)
    user_input = ""
    input_active = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key == pygame.K_RETURN:
                    return user_input, difficulte()
                else:
                    user_input += event.unicode

        Fenetre.fill((255, 255, 255))

        text = pygame.font.SysFont(None, 80, italic=True).render("Entrer votre nom", True, (0, 0, 0))
        text_rect = text.get_rect(center=(W // 2, H // 3))
        Fenetre.blit(text, text_rect)

        pygame.draw.rect(Fenetre, (0, 0, 0), input_rect, 2) if input_active else None
        input_surface = font.render(user_input, True, (0, 0, 0))
        input_surface_rect = input_surface.get_rect(center=input_rect.center)
        Fenetre.blit(input_surface, (input_surface_rect.x + 5, input_surface_rect.y))
        pygame.display.flip()

def difficulte():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        Fenetre.fill((255, 255, 255))

        easy_text = pygame.font.Font(None, 36).render("Facile", True, (0, 0, 0))
        easy_rect = easy_text.get_rect(center=(200, H // 2 -100))
        easy_button_rect = pygame.Rect(50, easy_rect.top - 25, 300, 80)

        medium_text = pygame.font.Font(None, 36).render("Moyen", True, (0, 0, 0))
        medium_rect = medium_text.get_rect(center=(200, H // 2 ))
        medium_button_rect = pygame.Rect(50, medium_rect.top - 25, 300, 80)

        hard_text = pygame.font.Font(None, 36).render("Difficile", True, (0, 0, 0))
        hard_rect = hard_text.get_rect(center=(200, H // 2 + 100))
        hard_button_rect = pygame.Rect(50, hard_rect.top - 25, 300, 80)

        if easy_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), easy_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), easy_button_rect, 2)

        if medium_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), medium_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), medium_button_rect, 2)

        if hard_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), hard_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), hard_button_rect, 2)

        Fenetre.blit(easy_text, easy_rect)
        Fenetre.blit(medium_text, medium_rect)
        Fenetre.blit(hard_text, hard_rect)
    
        if easy_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return "facile"
        elif medium_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return "moyen"
        elif hard_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return "difficile"
        
        choisir = pygame.font.Font(None, 60).render("Choisir le niveau", True, (0, 0, 0))
        choisir_rect = choisir.get_rect(center=(W // 2 + 180, H//2 - 30))

        niveau = pygame.font.Font(None, 60).render("de difficulté", True, (0, 0, 0))
        niveau_rect = niveau.get_rect(center=(W // 2 + 180, H//2 + 30))

        Fenetre.blit(choisir, choisir_rect)
        Fenetre.blit(niveau, niveau_rect)

        
        pygame.display.flip()

def insert_word():
    input_width = 300
    input_height = 36
    input_rect = pygame.Rect((W - input_width) // 2, (H - input_height) // 2, input_width, input_height)
    user_input = ""
    input_active = True
    message_add = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_input.strip():
                        with open("moyen.txt", "a") as file:
                            file.write(user_input + "\n")
                        message_add = pygame.font.Font(None, 36).render(f"Le mot '{user_input}' a été ajouté à la liste", True, (50, 50, 255))
                        message_add_rect = message_add.get_rect(center=(W // 2, 180))
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
        save_button_rect = pygame.Rect(W // 2 - 125, (H - input_height) // 2 + 50, 250, 40)

        if save_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), save_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), save_button_rect, 2)

        save_text_rect = save_text.get_rect(center=save_button_rect.center)
        Fenetre.blit(save_text, save_text_rect)

        back_text = pygame.font.Font(None, 36).render("Retour au Menu", True, (0, 0, 0))
        back_button_rect = pygame.Rect(W // 2 - 125, H // 2 + 220, 250, 40)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)

        if back_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), back_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), back_button_rect, 2)

        Fenetre.blit(back_text, back_text_rect)

        if save_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            if user_input.strip():
                with open("moyen.txt", "a") as file:
                    file.write(user_input + "\n")
                message_add = pygame.font.Font(None, 36).render(f"Le mot '{user_input}' a été ajouté à la liste", True, (255, 0, 0))
                message_add_rect = message_add.get_rect(center=(W // 2, 100))
                user_input = ""
        elif back_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return "back"

        if message_add:
            Fenetre.blit(message_add, message_add_rect)

        pygame.display.flip()

def mots_alea(difficulty):
    global solution
    file_path = f"{difficulty}.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
        words = [line.strip() for line in lines if line.strip()]
    solution = random.choice(words)

def play(player_name, difficulty):
    global solution
    player_score = 0
    mots_alea(difficulty)

    guessed_letters = ['_' for _ in solution]
    attempts = 0
    pendu_images = [f"img/{i}.png" for i in range(1, 9)]
    lettres_utilisees = []
    mauvaises_lettres = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key in range(pygame.K_a, pygame.K_z + 1):
                    guessed_letter = chr(event.key).lower()

                    if guessed_letter not in lettres_utilisees:
                        lettres_utilisees.append(guessed_letter)

                        if guessed_letter in solution:
                            for i, letter in enumerate(solution):
                                if letter == guessed_letter:
                                    guessed_letters[i] = guessed_letter
                        else:
                            mauvaises_lettres.append(guessed_letter)
                            attempts += 1

        Fenetre.fill((255, 255, 255))

        mauvaises_lettres_text = pygame.font.Font(None, 36, ).render(f"Tentatives : {attempts}/7", True, (255, 0, 0))
        Fenetre.blit(mauvaises_lettres_text, (50, 150))

        for i, lettre in enumerate(mauvaises_lettres):
            lettre_text = pygame.font.Font(None, 50).render(lettre, True, (255, 0, 0))
            Fenetre.blit(lettre_text, (100, 200 + i * 45))

        game_title = pygame.font.Font(None, 36).render("Le Pendu", True, (0, 0, 0))
        game_title_rect = game_title.get_rect(center=(W // 2, 50))
        Fenetre.blit(game_title, game_title_rect)

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

        if return_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return "back"

        if attempts < len(pendu_images):
            pendu_image = pygame.image.load(pendu_images[attempts])
            Fenetre.blit(pendu_image, (W // 2 - pendu_image.get_width() // 2, 225))

        if '_' not in guessed_letters:
            win_img = pygame.image.load("img/9.png")
            Fenetre.blit(win_img, (W // 2 - win_img.get_width() // 2, 225))
            message_gagne = pygame.font.Font(None, 36).render("Bravo, vous avez trouvé le mot.", True, (0, 250, 0))
            message_gagne_rect = message_gagne.get_rect(center=(W // 2, 100))
            Fenetre.blit(message_gagne, message_gagne_rect)
            pygame.display.flip()

        if '_' not in guessed_letters and player_score == 0:
            player_score += 1
            update_scores(player_name, player_score)

        if attempts == 7:
            message_echec = pygame.font.Font(None, 36).render("Vous avez atteint le nombre maximum d'essais.", True, (255, 0, 0))
            solution_echec = pygame.font.Font(None, 32).render(f"Le mot était '{solution}'", True, (255, 0, 0))
            message_echec_rect = message_echec.get_rect(center=(W // 2, 100))
            solution_echec_rect = solution_echec.get_rect(center=(W // 2, 140))
            Fenetre.blit(message_echec, message_echec_rect)
            Fenetre.blit(solution_echec, solution_echec_rect)
            pygame.display.flip()

        pygame.display.flip()
    
def load_scores():
    scores = []
    try:
        with open("scores.txt", "r") as scores_file:
            for line in scores_file:
                data = line.strip().split()
                if len(data) == 2:
                    name, score = data
                    scores.append((name, int(score)))
    except FileNotFoundError:
        pass

    return scores

def score():
    scores = load_scores()
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        Fenetre.fill((255, 255, 255))

        back_text = pygame.font.Font(None, 36).render("Retour au Menu", True, (0, 0, 0))
        back_button_rect = pygame.Rect(W // 2 - 125, H // 2 + 220, 250, 40)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)

        if back_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), back_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), back_button_rect, 2)

        if back_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return "back"

        Fenetre.blit(back_text, back_text_rect)

        text = pygame.font.Font(None, 80).render("Tableau des scores", True, (0, 0, 0))
        text_rect = text.get_rect(center=(W // 2, 55))
        Fenetre.blit(text, text_rect)

        y_position = H // 4
        for name, score in scores:
            score_text = pygame.font.Font(None, 38).render(f"{name}: {score}", True, (0, 0, 0))
            score_rect = score_text.get_rect(center=(W // 2, y_position))
            Fenetre.blit(score_text, score_rect)
            y_position += 30

        pygame.display.flip()

def update_scores(player_name, player_score):
    scores = load_scores()

    player_exists = False
    for i, (name, score) in enumerate(scores):
        if name == player_name:
            scores[i] = (name, score + player_score)
            player_exists = True
            break

    if not player_exists:
        scores.append((player_name, player_score))

    with open("scores.txt", "w") as scores_file:
        for name, score in scores:
            scores_file.write(f"{name} {score}\n")

while True:
    main_menu()
