# Упражнение 8. Стихии и их комбинации

class Element:
    def __add__(self, other):
        return None

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__


class Water(Element):
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        if isinstance(other, Fire):
            return Steam()
        if isinstance(other, Earth):
            return Mud()
        return None


class Air(Element):
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Earth):
            return Dust()
        return None


class Fire(Element):
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        if isinstance(other, Air):
            return Lightning()
        if isinstance(other, Earth):
            return Lava()
        return None


class Earth(Element):
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        if isinstance(other, Air):
            return Dust()
        if isinstance(other, Fire):
            return Lava()
        return None


class Storm(Element):
    pass


class Steam(Element):
    pass


class Mud(Element):
    pass


class Lightning(Element):
    pass


class Dust(Element):
    pass


class Lava(Element):
    pass


# Дополнительный элемент — Лёд
class Ice(Element):
    def __add__(self, other):
        if isinstance(other, Fire):
            return Water()
        if isinstance(other, Water):
            return Ice()
        if isinstance(other, Earth):
            return Mud()
        return None


if __name__ == "__main__":
    print(Water() + Air())        # Storm
    print(Water() + Fire())       # Steam
    print(Water() + Earth())      # Mud
    print(Air() + Fire())         # Lightning
    print(Air() + Earth())        # Dust
    print(Fire() + Earth())       # Lava
    print(Water() + Water())      # None
    print(Ice() + Fire())         # Water
    print(Ice() + Earth())        # Mud