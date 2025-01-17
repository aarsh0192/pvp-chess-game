import pygame

class Sound:

    def __init__(self, path):
        self.path = path
        self.sound = pygame.mixer.Sound(path)          #creates the pygame sound

    def play(self):                   #plays the pyagme sound
        pygame.mixer.Sound.play(self.sound)