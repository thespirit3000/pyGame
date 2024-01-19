import pygame, os, time
from states.TitleScreenState import TitleScreenState

class Game():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.GAME_W,self.GAME_H = 480, 270
        self.SCREEN_W,self.SCREEN_H = 960, 540
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.running, self.playing = True, True
        self.dt,self.prev_time = 0,0
        self.state_stack = []
        self.load_assets()
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.quit()
                quit()
            elif self.current_state():
                self.current_state().handle_events(event)

    def update(self):
        if self.state_stack:
            self.state_stack[-1].update()
        pass

    def render(self):
        self.screen.fill((0, 0, 0))
        if self.state_stack:
            self.state_stack[-1].render()

    def run(self):
        while self.playing:
            self.handle_events()
            self.update()
            self.render()
            pygame.display.update()
            self.clock.tick(60)

    def push_state(self, state):
        self.state_stack.append(state)
        
    def pop_state(self):
        if self.state_stack:
            self.state_stack.pop()

    def current_state(self):
        if self.state_stack:
            return self.state_stack[-1]

    def exit_state(self):
        self.state_stack.pop()

    def load_assets(self):
            # Create pointers to directories 
            self.assets_dir = os.path.join("assets")
            self.sprite_dir = os.path.join(self.assets_dir, "sprites")
            self.font_dir = os.path.join(self.assets_dir, "font")
            self.font= pygame.font.Font(os.path.join(self.font_dir, "PressStart2P-vaV7.ttf"), 20)
            self.title_font =  pygame.font.Font(os.path.join(self.font_dir, "PressStart2P-vaV7.ttf"), 32)

if  __name__ == "__main__":
    game = Game()
    title_state = TitleScreenState(game)
    game.push_state(title_state)
    while game.running:
        game.run()
