class Bird:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        return f"The {self.species} makes a {self.sound} sound!"

# Create Bird objects
bird1 = Bird("sparrow", "chirping")
bird2 = Bird("parrot", "squawking")

# Make sounds
print(bird1.make_sound())
print(bird2.make_sound())
