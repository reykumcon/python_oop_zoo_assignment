class Animal:
    def __init__(self, name, health_level=0, happiness_level=0):
        self.name = name
        self.health_level = health_level
        self.happiness_level = happiness_level
    def display_info(self):
        print("Name:", self.name, "\nHealth Level:", self.health_level, "\nHappiness Level", self.happiness_level)
        return self
    def feed_animal(self):
        self.health_level += 10
        self.happiness_level += 10
        return self

class Lion(Animal):
    def __init__(self, name, health_level=5, happiness_level=5):
        super().__init__(name, health_level, happiness_level)
    def feed_animal(self):
        self.health_level += 5
        self.happiness_level += 5
        return self

class Bear(Animal):
    def __init__(self, name, type, health_level=10, happiness_level=10):
        super().__init__(name, health_level, happiness_level)
        self.type = type
    def display_info(self):
        print("Name:", self.type, self.name, "\nHealth Level:", self.health_level, "\nHappiness Level", self.happiness_level)

class Tiger(Animal):
    def __init__(self, name, health_level=15, happiness_level=15):
        super().__init__(name, health_level, happiness_level)
    def feed_animal(self):
        self.health_level += 15
        self.happiness_level += 15
        return self

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append(Lion(name))
        return self
    def add_tiger(self, name):
        self.animals.append(Tiger(name))
        return self
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
        return self

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()