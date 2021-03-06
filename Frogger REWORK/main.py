import pygame
import os
import sys
from os import path
from data.settings import *
from data.sprites import *
        
class Game():
    def __init__(self):
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.img_dir = path.join(path.dirname(__file__), 'img')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Frogger")
        self.clock = pygame.time.Clock()
        self.running = True
        
    def load(self):
        # load game images 
        self.dir = path.dirname(__file__)
        self.img_dir = path.join(self.dir, 'img')
        self.player_img = pygame.image.load(path.join(self.img_dir, "frog.png")).convert()
        self.car00_img = pygame.image.load(path.join(self.img_dir, "car_image00.png")).convert()
        self.truck_img = pygame.image.load(path.join(self.img_dir, "truck_image.png")).convert()
        self.log_img = pygame.image.load(path.join(self.img_dir, "log_image.png")).convert()
        self.saved_img = pygame.image.load(path.join(self.img_dir, "saved_image.png")).convert()
        self.center_img = pygame.image.load(path.join(self.img_dir, "centerwall_image.png")).convert()
        self.end_img = pygame.image.load(path.join(self.img_dir, "end_image.png")).convert()
        self.end_img2 = pygame.image.load(path.join(self.img_dir, "end_image2.png")).convert()

        # player lives
        self.life_1 = PlayerLife(self, 15)
        self.all_sprites.add(self.life_1)
        self.life_2 = PlayerLife(self, 45)
        self.all_sprites.add(self.life_2)
        self.life_3 = PlayerLife(self, 75)
        self.all_sprites.add(self.life_3)

        # top wall piece
        self.grassobj_1 = GrassObj(self, self.end_img2, 0, 0, 480, 15)
        self.all_sprites.add(self.grassobj_1)
        self.grassobj.add(self.grassobj_1)

        # end wall pieces
        self.grassobj_1 = GrassObj(self, self.end_img2, 0, 15, 30, 30)
        self.all_sprites.add(self.grassobj_1)
        self.grassobj.add(self.grassobj_1)

        self.grassobj_1 = GrassObj(self, self.end_img, 450, 15, 30, 30)
        self.all_sprites.add(self.grassobj_1)
        self.grassobj.add(self.grassobj_1)

        # center wall peices
        self.centerwall = GrassObj(self, self.center_img, 90, 15, 30, 30)
        self.all_sprites.add(self.centerwall)
        self.grassobj.add(self.centerwall)
         
        self.centerwall = GrassObj(self, self.center_img, 180, 15, 30, 30)
        self.all_sprites.add(self.centerwall)
        self.grassobj.add(self.centerwall)

        self.centerwall = GrassObj(self, self.center_img, 270, 15, 30, 30)
        self.all_sprites.add(self.centerwall)
        self.grassobj.add(self.centerwall)

        self.centerwall = GrassObj(self, self.center_img, 360, 15, 30, 30)
        self.all_sprites.add(self.centerwall)
        self.grassobj.add(self.centerwall)

        # empty objects top
        self.emptyobj_1 = EmptyObj(self, pygame.Surface((60, 30)), 30, 15)
        self.all_sprites.add(self.emptyobj_1)
        self.emptyobj.add(self.emptyobj_1)

        self.emptyobj_1 = EmptyObj(self, pygame.Surface((60, 30)), 120, 15)
        self.all_sprites.add(self.emptyobj_1)
        self.emptyobj.add(self.emptyobj_1)

        self.emptyobj_1 = EmptyObj(self, pygame.Surface((60, 30)), 210, 15)
        self.all_sprites.add(self.emptyobj_1)
        self.emptyobj.add(self.emptyobj_1)

        self.emptyobj_1 = EmptyObj(self, pygame.Surface((60, 30)), 300, 15)
        self.all_sprites.add(self.emptyobj_1)
        self.emptyobj.add(self.emptyobj_1)

        self.emptyobj_1 = EmptyObj(self, pygame.Surface((60, 30)), 390, 15)
        self.all_sprites.add(self.emptyobj_1)
        self.emptyobj.add(self.emptyobj_1)

        # saved objects top test case!
        self.capturedobj_1 = EmptyObj(self, pygame.transform.scale(self.saved_img,(60, 30)), 30, 15)
        #all_sprites.add(savedobj)
        self.capturedobj.add(self.capturedobj_1)

        self.capturedobj_2 = EmptyObj(self, pygame.transform.scale(self.saved_img,(60, 30)), 120, 15)
        #all_sprites.add(savedobj)
        self.capturedobj.add(self.capturedobj_2)

        self.capturedobj_3 = EmptyObj(self, pygame.transform.scale(self.saved_img,(60, 30)), 210, 15)
        #all_sprites.add(savedobj)
        self.capturedobj.add(self.capturedobj_3)

        self.capturedobj_4 = EmptyObj(self, pygame.transform.scale(self.saved_img,(60, 30)), 300, 15)
        #all_sprites.add(savedobj)
        self.capturedobj.add(self.capturedobj_4)

        self.capturedobj_5 = EmptyObj(self, pygame.transform.scale(self.saved_img,(60, 30)), 390, 15)
        #all_sprites.add(savedobj)
        self.capturedobj.add(self.capturedobj_5)
        
        #### Spawn the Logs for Rows 1,3,4,5
        for i in range(2):
            # Logs on Row 1
            self.logs_1 = Vehicles(self, self.log_img, False, NEG_LOGSPEED, SPACING_3, i+1, 288, LOG_WIDTH)
            self.all_sprites.add(self.logs_1)
            self.logsleft.add(self.logs_1)
            # Logs on Row 3 
            self.logs_3 = Vehicles(self, pygame.transform.scale(self.log_img, (LOG_WIDTH2, 30)), False, FAST_LOGSPEED, SPACING_4, i+1, 192, LOG_WIDTH2)
            self.all_sprites.add(self.logs_3)
            self.logsfast.add(self.logs_3)
            # Logs on Row 4 
            self.logs_4 = Vehicles(self, self.log_img, False, NEG_LOGSPEED, SPACING_2, i+1, 144, LOG_WIDTH)
            self.all_sprites.add(self.logs_4)
            self.logsleft.add(self.logs_4)    
            # Logs on Row 5
            self.logs_5 = Vehicles(self, pygame.transform.scale(self.log_img, (LOG_WIDTH2, 30)), False, POS_LOGSPEED, SPACING_2, i+1, 96, LOG_WIDTH2)
            self.all_sprites.add(self.logs_5)
            self.logsright.add(self.logs_5)

        #### Spawn the Logs for Row 2
        for i in range(3):
            self.logs_2 = Vehicles(self, self.log_img, False, POS_LOGSPEED, SPACING_3, i+1, 240, LOG_WIDTH)
            self.all_sprites.add(self.logs_2)
            self.logsright.add(self.logs_2)

        # Draw Player Sprite
        self.player = Player(self)
        self.all_sprites.add(self.player)

        #### Spawn the vehicles for each row
        for i in range(3):
            # Cars on Row 1
            self.vehicle_1 = Vehicles(self, pygame.transform.rotate(self.car00_img, 180), 5, POS_CARSPEED, SPACING, i+1, 576, BOX_WIDTH)
            self.all_sprites.add(self.vehicle_1)
            self.vehicles.add(self.vehicle_1)
            # Cars on Row 2
            self.vehicle_2 = Vehicles(self, self.car00_img, 5, NEG_CARSPEED, SPACING, i+1, 528, BOX_WIDTH)
            self.all_sprites.add(self.vehicle_2)
            self.vehicles.add(self.vehicle_2)
            # Truck on Row 5
            self.vehicle_5 = Vehicles(self, self.truck_img, 25, NEG_CARSPEED, SPACING_2, i+1, 384, 90)
            self.all_sprites.add(self.vehicle_5)
            self.vehicles.add(self.vehicle_5)
            print(i)
            print(self.vehicle_1.rect.x)
            
        for i in range(4):
            # Cars on Row 3
            self.vehicle_3 = Vehicles(self, pygame.transform.rotate(self.car00_img, 180), 5, POS_CARSPEED, SPACING, i+1, 480, BOX_WIDTH)
            self.all_sprites.add(self.vehicle_3)
            self.vehicles.add(self.vehicle_3)
        
        # Car single on Row 4
        self.vehicle_4 = Vehicles(self, self.car00_img, 5, -2, SPACING, i, 432, 30)
        self.vehicles.add(self.vehicle_4)
        self.all_sprites.add(self.vehicle_4)

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.vehicles = pygame.sprite.Group()

        self.logsleft = pygame.sprite.Group()
        self.logsright = pygame.sprite.Group()
        self.logsfast = pygame.sprite.Group()

        self.grassobj = pygame.sprite.Group()
        self.emptyobj = pygame.sprite.Group()
        self.capturedobj = pygame.sprite.Group()

        # load game graphics 
        self.background = pygame.image.load(path.join(self.img_dir, "background.png")).convert()
        self.background_rect = self.background.get_rect()
        self.gameover_img = pygame.image.load(path.join(self.img_dir, "gameover_image.png")).convert()
        self.player_img = pygame.image.load(path.join(self.img_dir, "frog.png")).convert()
        self.load()
        self.run()
        
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            
    def update(self):
        self.all_sprites.update()
        self.vehicles.update()
        
        # collision when the player goes off the screen
        if self.player.rect.left <= 0:
            self.player.rect.left = 0
        if self.player.rect.right >= 480:
            self.player.rect.right = 480
        if self.player.rect.bottom >= HEIGHT - 96:
            self.player.rect.bottom = HEIGHT - 96
        if self.player.rect.bottom <= 45:
            self.player.rect.centerx = WIDTH / 2
            self.player.rect.bottom = HEIGHT - 96

         # collision when the player hits a log going left
        self.logsleft_hit = pygame.sprite.spritecollide(self.player, self.logsleft, False, pygame.sprite.collide_rect_ratio(0.8))
        if len(self.logsleft_hit) != 0:
            self.player.onLogLeft = True
        if len(self.logsleft_hit) == 0:
            self.player.onLogLeft = False

        # collision when the player hits a log going right
        self.logsright_hit = pygame.sprite.spritecollide(self.player, self.logsright, False, pygame.sprite.collide_rect_ratio(0.8)) 
        if len(self.logsright_hit) != 0:
            self.player.onLogRight = True
        if len(self.logsright_hit) == 0:
            self.player.onLogRight = False

        # collision when the player hits a log going fast
        self.logsfast_hit = pygame.sprite.spritecollide(self.player, self.logsfast, False, pygame.sprite.collide_rect_ratio(0.8)) 
        if len(self.logsfast_hit) != 0:
            self.player.onLogFast = True
        if len(self.logsfast_hit) == 0:
            self.player.onLogFast = False
        
        # collision when the player hits a car
        self.vehicles_hit = pygame.sprite.spritecollide(self.player, self.vehicles, False, pygame.sprite.collide_circle)
        for hit in self.vehicles_hit:
            PlayerHit.objectHit(self)

        # collision when the player is in the water
        if self.player.onLogLeft == False and self.player.onLogRight == False and self.player.onLogFast == False and self.player.rect.bottom <= 288 and self.player.rect.bottom != 48:
            PlayerHit.objectHit(self)
        
        # collision when the player hits grass object
        self.grassobj_hit = pygame.sprite.spritecollide(self.player, self.grassobj, False, pygame.sprite.collide_rect)
        for hit in self.grassobj_hit:
            PlayerHit.objectHit(self)
            
        # check if player has used all available lives
        if pygame.sprite.Sprite.alive(self.life_1) != True and self.player.life_count == 1:
            pygame.sprite.Sprite.kill(self.life_2)
        if pygame.sprite.Sprite.alive(self.life_2) != True and self.player.life_count == 0:
            pygame.sprite.Sprite.kill(self.life_3)
        if pygame.sprite.Sprite.alive(self.life_3) != True and self.player.life_count <= -1:
            self.playing = False

        # collision when the player captures a frog
        self.emptyobj_hit = pygame.sprite.spritecollide(self.player, self.emptyobj, False, pygame.sprite.collide_rect)
        for hit in self.emptyobj_hit:

            if self.player.rect.left >= 30 and self.player.rect.right <= 90 and self.player.rect.bottom <= 48:            
                self.all_sprites.add(self.capturedobj_1)
                self.capturedobj.remove(self.capturedobj_1)
                PlayerHit.addScore(self)

            if self.player.rect.left >= 120 and self.player.rect.right <= 180 and self.player.rect.bottom <= 48:            
                self.all_sprites.add(self.capturedobj_2)
                self.capturedobj.remove(self.capturedobj_2)
                PlayerHit.addScore(self)

            if self.player.rect.left >= 210 and self.player.rect.right <= 270 and self.player.rect.bottom <= 48:            
                self.all_sprites.add(self.capturedobj_3)
                self.capturedobj.remove(self.capturedobj_3)
                PlayerHit.addScore(self)

            if self.player.rect.left >= 300 and self.player.rect.right <= 360 and self.player.rect.bottom <= 48:            
                self.all_sprites.add(self.capturedobj_4)
                self.capturedobj.remove(self.capturedobj_4)
                PlayerHit.addScore(self)

            if self.player.rect.left >= 390 and self.player.rect.right <= 450 and self.player.rect.bottom <= 48:            
                self.all_sprites.add(self.capturedobj_5)
                self.capturedobj.remove(self.capturedobj_5)
                PlayerHit.addScore(self)

        # check to see if player has captured all frogs and won
        if len(self.capturedobj) == 0:
            self.playing = False

        if self.player.time == 0:
            self.playing = False
        
    def events(self):
        # Game Loop - events
        self.MousePos = pygame.mouse.get_focused() 
        if self.MousePos != 0:
            self.player.speedx = 0
            self.player.speedy = 0
            
        for event in pygame.event.get():
            # Checking for Player events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.speedx = -48
                if event.key == pygame.K_RIGHT:
                    self.player.speedx = 48
                if event.key == pygame.K_UP:
                    self.player.speedy = -48
                if event.key == pygame.K_DOWN:
                    self.player.speedy = 48

            if event.type == pygame.KEYUP and self.player.onLogLeft == False and self.player.onLogRight == False and self.player.onLogFast == False:
                if event.key == pygame.K_LEFT:
                    self.player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    self.player.speedx = 0
                if event.key == pygame.K_UP:
                    self.player.speedy = 0
                if event.key == pygame.K_DOWN:
                    self.player.speedy = 0

            self.player.rect.x += self.player.speedx
            self.player.rect.y += self.player.speedy
            
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        #self.all_sprites.update()
        self.screen.fill(WHITE)
        self.screen.blit(self.background, self.background_rect)
        self.all_sprites.draw(self.screen)
        #pygame.draw.rect(self.screen, RED,(90, 546, 30, 30))
        self.player.draw_shield_bar(self.screen, 200, 700, self.player.time)
        draw_text(self.screen, str(self.player.score), 18, 375, 624)
        pygame.display.update()

    def show_go_screen(self):
        if not self.playing or self.running:
            self.screen.blit(self.gameover_img, [175, HEIGHT / 2])
            pygame.display.update()
            self.wait_for_key()

    def wait_for_key(self):          
        self.last_update = pygame.time.get_ticks()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            now = pygame.time.get_ticks()
            if now - self.last_update > 1500:
                holding = True
                self.last_update = now
                while holding:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            holding = False
                            waiting = False
                            self.playing = False
                            self.running = False
                        if event.type == pygame.KEYUP:
                            holding = False
                            waiting = False
                            return

g = Game()
while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()
