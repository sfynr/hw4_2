class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} TL yatırıldı. Yeni bakiye: {self.balance} TL")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} TL çekildi. Yeni bakiye: {self.balance} TL")
        else:
            print("Yetersiz bakiye. İşlem gerçekleştirilemedi.")

    def get_balance(self):
        return f"{self.account_holder}'in bakiyesi: {self.balance} TL"


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print(f"Faiz eklendi. Yeni bakiye: {self.balance} TL")