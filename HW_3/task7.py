# Упражнение 7. Травоядное животное и трава

class Grass:
    def __init__(self, nutrition):
        self.nutrition = nutrition


class Herbivore:
    def __init__(self, name, hunger=10):
        self.name = name
        self.hunger = hunger  # чем больше, тем голоднее

    def eat(self, grass):
        if self.hunger <= 0:
            print(f"{self.name} не голоден и отказывается от травы.")
            return
        self.hunger -= grass.nutrition
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} съел траву и насытился. Голод: {self.hunger}")


if __name__ == "__main__":
    cow = Herbivore("Корова", hunger=5)
    grass = Grass(nutrition=3)
    cow.eat(grass)  # насытился, голод 2
    cow.eat(grass)  # насытился, голод 0
    cow.eat(grass)  # отказ