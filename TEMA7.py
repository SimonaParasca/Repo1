from abc import abstractmethod, ABC


class FormaGeometrica(ABC):
    PI = 3.14

    # @abstractmethod
    # def aria(self):
    #     raise NotImplementedError


    @abstractmethod
    def descrie(self):
        raise NotImplementedError

class Cub(FormaGeometrica):
    def descrie(self):
        print("Cel mai probabil am colturi")
cub = Cub()
cub.descrie()





# inheritance

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.latura= latura

# encapsulation

    __latura = 14

    def get_latura(self):
        return self.__latura
    def set_color(self, dimenisune_latura):
        self.__latura = dimenisune_latura
    def __hidden(self):
        pass

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.raza = raza
    __raza = 10
    def get_raza(self):
        return self.__raza
    def set_raza(self, dimensiune_raza):
        self.__raza = dimensiune_raza
    def __hidden(self):
        pass
# polymorphism
    def descrie(self):
        print("eu nu am colturi")

patrat = Cub()
print(patrat.descrie())
cerc = Cerc(10)
print(cerc.descrie())
print(cerc.get_raza())
print(cerc.set_raza(11))
print(cerc.get_raza())
