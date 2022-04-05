class Pet:
    def __init__(self, name = "temp", type = "dog", tricks = "roll over", health = 0, energy = 0):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    
    def sleep(self):
        self.energy += 25
        print(f"My energy is {self.energy}")
        return self
    
    def eat(self):
        self.health += 10
        self.energy += 5
        print(f"My energy is {self.energy}")
        print(f"My health is {self.health}")
        return self
    
    def play(self):
        self.health += 5
        print(f"My health is {self.health}")
        return self

    def noise(self):
        print("Woof")
