from Drink import Drink

class Inventary:
    def __init__(
            self,
            ingredients: list,
            drinks: Drink      
    ) -> None:
        self.ingredients = ingredients
        self.drinks = drinks