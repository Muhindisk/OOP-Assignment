class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move() method")
    
    def describe(self):
        return f"I am a {self.name} and I live in {self.habitat}."


class Bird(Animal):
    def __init__(self, name, habitat, wingspan):
        super().__init__(name, habitat)
        self.wingspan = wingspan
    
    def move(self):
        return f"{self.name} is flying through the air with its {self.wingspan}cm wingspan! 🕊️"
    
    def chirp(self):
        return f"{self.name} says: Tweet tweet! 🎵"


class Fish(Animal):
    def __init__(self, name, habitat, fin_count):
        super().__init__(name, habitat)
        self.fin_count = fin_count
    
    def move(self):
        return f"{self.name} is swimming gracefully with its {self.fin_count} fins! 🐟"
    
    def bubble(self):
        return f"{self.name} blows bubbles! 💦"


class Snake(Animal):
    def __init__(self, name, habitat, length):
        super().__init__(name, habitat)
        self.length = length
    
    def move(self):
        return f"{self.name} is slithering silently along the ground! 🐍"
    
    def hiss(self):
        return f"{self.name} says: Hisssss! 🐍"


class Kangaroo(Animal):
    def __init__(self, name, habitat, jump_height):
        super().__init__(name, habitat)
        self.jump_height = jump_height
    
    def move(self):
        return f"{self.name} is hopping {self.jump_height} meters high! 🦘"
    
    def box(self):
        return f"{self.name} starts boxing! 🥊"


class Cheetah(Animal):
    def __init__(self, name, habitat, top_speed):
        super().__init__(name, habitat)
        self.top_speed = top_speed
    
    def move(self):
        return f"{self.name} is running at {self.top_speed} km/h! 🐆"
    
    def roar(self):
        return f"{self.name} says: Roar! 🦁"


# Let's create a function that demonstrates polymorphism
def animal_parade(animals):
    print("=== ANIMAL PARADE === 🎪")
    for animal in animals:
        print(animal.describe())
        print(animal.move())
        
        # Demonstrate some unique methods
        if isinstance(animal, Bird):
            print(animal.chirp())
        elif isinstance(animal, Fish):
            print(animal.bubble())
        elif isinstance(animal, Snake):
            print(animal.hiss())
        elif isinstance(animal, Kangaroo):
            print(animal.box())
        elif isinstance(animal, Cheetah):
            print(animal.roar())
        
        print()  # Empty line for readability


# Create some animals
eagle = Bird("Eddie the Eagle", "mountains", 200)
salmon = Fish("Sally the Salmon", "rivers", 7)
cobra = Snake("Carl the Cobra", "deserts", 2.5)
roo = Kangaroo("Ricky the Roo", "grasslands", 3)
cheetah = Cheetah("Chase the Cheetah", "savannah", 120)

# Put them in a list
animals = [eagle, salmon, cobra, roo, cheetah]

# Demonstrate polymorphism
animal_parade(animals)

# Additional demonstration: same method, different behaviors
print("=== MOVEMENT DEMONSTRATION ===")
for animal in animals:
    print(animal.move())