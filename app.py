import pygame, os, time

class Game():
    def __init__(self):
        pygame.init()
        self.GAME_W,self.GAME_H = 480, 270
        self.SCREEN_W,self.SCREEN_H = 960, 540
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.running, self.playing = True, True
        self.actions = {"left" : False, "right" : False, "up" : False,"down" : False,"action1" : False,"action2" : False,"start" : False}
        self.dt,self.prev_time = 0,0
        self.state_stack = []
        self.load_assets()

    def get_events(self):
       for event in pygame.event.get():
           if event == pygame.QUIT:
               self.playing = False
               self.running = False
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   self.playing = False
                   self.running = False
               if event.key == pygame.K_a:
                   self.actions['left'] = True
               if event.key == pygame.K_d:
                   self.actions['right'] = True
               if event.key == pygame.K_w:
                   self.actions['up'] = True
               if event.key == pygame.K_s:
                   self.actions['down'] = True
               if event.key == pygame.K_p:
                   self.actions['action1'] = True
               if event.key == pygame.K_o:
                   self.actions['action2'] = True
               if event.key == pygame.K_RETURN:
                   self.actions['start'] = True
            
        










