import pygame as pg

class Sound: 

# Initialize the mixer module
pg.mixer.init()

# Load sound effects
pop_sound = pg.mixer.Sound("./sound_effect/pop-39222.mp3")
collect_sound = pg.mixer.Sound("./sound_effects/cereal-pouring-in-bowl-265404.mp3")
complete_sound = pg.mixer.Sound("./sound_effects/level-win-6416.mp3")

# Add more sounds as needed
def load_sounds():
    # Here we can load additional sounds if needed in the future
    pass

def play_explosion_sound():
    pop_sound.play()

def play_collect_sound():
    collect_sound.play()

def win_sound():
    complete_sound.play()