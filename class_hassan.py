class ensan:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def moarefi(self):
        print(f"I man {self.name} and my age is {self.age} and my gender is {self.gender}")
    def eat(self, food):
        print(f"{self.name} eat {food}")
    def sleep(self):
        print(f"{self.name} is sleeping")

a1 = ensan("yasin", 23, "male")
a1.moarefi()
a1.sleep()
a1.eat("apple")