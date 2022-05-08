import Employee

class Cash_Register:
    def __init__(
            self,
            balance: str,
            admin: Employee,
            id_admin: str        
    ) -> None:
        self.balance = balance
        self.admin = admin
        self.id_admin = id_admin