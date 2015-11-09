'''
Created on Jun 30, 2015

@author: Joe DeBruycker
'''
import pygame

# ---CONSTANTS---

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
DIRT = (110, 80, 12)
DITCH = (69, 46, 9)

# Screen Size
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700



# ---CLASSES--- 

class Gator(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Image
        self.image = pygame.image.load("gator.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        
        # Position
        self.rect.x = 0
        self.rect.y = 0
        
        # Movement
        self.change_x = 0
        self.change_y = 0
        
    # Methods 
    def move(self, xspeed, yspeed):
        self.change_x = xspeed
        self.change_y = yspeed  
        
    def draw(self, screen):
        screen.blit(self.image, [self.rect.x,self.rect.y])
        
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
  
  
        
class Ditch(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.hasWater = False
        
        self.image = pygame.Surface([100, 100])
        self.image.fill(DITCH)
        
        self.rect = self.image.get_rect()
        
    # Methods



class Game(object):
    def __init__(self):
        # Create sprite lists
        self.ditch_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        
        #Create the gator
        self.al = Gator()
        self.all_sprites_list.add(self.al)
        
        #Create the ditches
        for i in range (5):
            ditch = Ditch()
            
            ditch.rect.x = 400
            ditch.rect.y = i * 100
            
            self.ditch_list.add(ditch)
            self.all_sprites_list.add(ditch)
            
            
    # --- Game Methods ---    
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.al.move(-5,0)
                if event.key == pygame.K_RIGHT:
                    self.al.move(5,0)
                if event.key == pygame.K_DOWN:
                    self.al.move(0,5)
                if event.key == pygame.K_UP:
                    self.al.move(0,-5)
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.al.move(0,0)
                if event.key == pygame.K_RIGHT:
                    self.al.move(0,0)
                if event.key == pygame.K_DOWN:
                    self.al.move(0,0)
                if event.key == pygame.K_UP:
                    self.al.move(0,0)
                    
    def run_logic(self):
        self.all_sprites_list.update()
                
    def display_frame(self, screen):   
        screen.fill(DIRT)
        
        self.all_sprites_list.draw(screen)
        
        pygame.display.flip()



# --- Main Program Loop ---
def main():  
    # Open a window
    pygame.init()
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)
    
    # Window Title
    pygame.display.set_caption("Irri-Gator")
    
    # Manage screen updates
    clock = pygame.time.Clock()

    # Create Game instance
    game = Game()
    
    # Game loop variable
    done = False

    # Main Game Loop
    while not done:
        
        done = game.process_events()
        
        game.run_logic()
        
        game.display_frame(screen)
        
        clock.tick(60)
        
    # Close Game
    pygame.quit()


    
if __name__ == "__main__":
    main()
    
