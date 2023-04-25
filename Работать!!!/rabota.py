class Rabotyaga:
    def __init__(self, name, age, zarplata):
        self.name = name
        self.age = age
        self.zarplata = zarplata
    def rabotaaaa(self):
        print(self.name, "работает за", self.zarplata, "в месяц")


class Meneger(Rabotyaga):
    def __init__(self, name, age, zarplata, kolvo_podchinnenih, koef):
        super().__init__(name, age, zarplata)
        self.kolvo_podchinnenih = kolvo_podchinnenih
        self.koef = koef
    def rabotaaaa(self):
        print(self.name, "работает за", (self.zarplata + self.kolvo_podchinnenih * self.koef), "в месяц" )

bob = Meneger("Боб", 30, 1000000, 40, 10000)

bob.rabotaaaa()