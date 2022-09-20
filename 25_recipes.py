class Recipe():
    # def __new__(cls: type[self]) -> Self:
    #     pass
    # def__init__(self) -> None:
    #     pass

    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
    
    def content(self):
        print("The " + self.dish + " has " + str(self.items) + \
            " and takes " + str(self.time) + " mins to prepare.")

pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["penne", "sauce"], 55)

print(pizza.items)
print(pasta.items)

print(pizza.content())