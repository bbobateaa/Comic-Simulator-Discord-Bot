from comic_bar import ComicBarLevel

class ComicHungerLevel(ComicBarLevel):
    def __init__(self) -> None:
        super().__init__()
        self.hunger = True
        self.food_amount = 0

    def feed_food(self, food):
        if self.food_amount >= 100:
            self.hunger = False
            return "Comic is not hungry! But he tries to eat it anyways"
        else:
            self.hunger = True
        if self.hunger:
            if food == "meat" or food == "cheese":
                amount = self.__getbar__() * 0.30
                print(f"first bar: {self.__getbar__()}")
                self.__incrementbar__(amount)
                self.food_amount += 20
                print(f"bar: {self.__getbar__()}")
                return "*CHOMP*\n WOOF!\n *looks at you with 30% more satisfied*"

            elif food == "in n out" or food == "poop":
                amount = self.__getbar__() * 0.50
                self.__incrementbar__(amount)
                self.food_amount += 40
                return "*CHOMP*\n WOOF!\n *looks at you with 50% more satisfied*"

            elif food != "vegetables" and food != "kibble":
                amount = self.__getbar__() * 0.10
                self.__incrementbar__(amount)
                self.food_amount += 10
                return "*CHOMP*\n WOOF!\n *looks at you with 10% more satisfied*"

            else:
                amount = self.__getbar__() * 0.10
                self.__decrementbar__(amount)
                self.food_amount -= 10
                return f"*side eyes you harder* {amount} of satisfaction lost!"
