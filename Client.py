import Order
import Invoice
class Client:
    def __init__(
            self,
            order: Order,
            bill: Invoice,
            bill_status: bool       
    ) -> None:
        self.order = order
        self.bill = bill
        self.bill_status = bill_status