from pet import Pet

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print("Walking Pet")
        self.pet.play()
        return self

    def feed(self):
        print("Feeding pet")
        self.pet.eat()
        return self

    def bathe(self):
        print("Bathing Pet")
        self.pet.noise()

myNinja = Ninja("Michael", "Mason", "Pizza", "kibble", Pet("Fido","dog","Paw", 100, 20))
myNinja.feed()
myNinja.walk()
myNinja.bathe()

