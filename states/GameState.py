import pygame, time
from states.Level import Level

class GameState:
    def __init__(self, game):
        self.game = game
        self.level = 1
        self.score = 0
        self.level = Level(self.level) 

    def handle_events(self, event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.pop_state()

    def update(self):
        pass

    def render(self):
        screen = self.game.screen
        font = self.game.font
        title_font = self.game.title_font
        screen.fill((0, 0, 0))  # Fill the screen with black
        title_text = title_font.render("Level", True, (255, 255, 0))
        title_rect = title_text.get_rect(center = (screen.get_width()/2, 50)) 
        if time.time() % 1 > 0.5:
            title_text.set_alpha(100)
        else:
            title_text.set_alpha(255)
        screen.blit(title_text, title_rect)
        self.level.render()
