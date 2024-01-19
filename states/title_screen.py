from states.state import State

class TitleScreenState(State):
    def __init__(self, game):
        super.__init__(self, game)

    def update(self, delta_time, actions):
        self.game.reset_keys()

    def render(self, display):
        display.fill((255,255,255))
        self.game.draw_text(display, "Game States Demo", (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2)
