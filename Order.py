class Order:
    def __init__(
            self,
            plates: list,
            drinks: list,
            order_status: bool,
            table: int      
    ) -> None:
        self.plates = plates
        self.drinks = drinks
        self.order_status = order_status
        self.table = table