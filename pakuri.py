import math


class Pakuri:

    def __init__(self, species, level):
        self.__species = species
        self.__level = level
        self.__attack = (len(self.__species) * 7 + 11) % 16
        self.__defense = ((len(self.__species) * 5) + 17) % 16
        self.__stamina = (len(self.__species) * 6 + 13) % 16

    def get_species(self):
        return self.__species

    def get_attack(self):
        return self.__attack

    def get_defense(self):
        return self.__defense

    def get_stamina(self):
        return self.__stamina

    def set_attack(self, new_attack):
        self.__attack = new_attack

    @property
    def cp(self):
        self.__cp = math.floor(self.__attack*math.sqrt(self.__defense)*math.sqrt(self.__stamina)*self.__level*.08)
        return self.__cp

    @property
    def hp(self):
        self.__hp = math.floor(self.__stamina*self.__level/6)
        return self.__hp

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, new_level):
        self.__level = new_level