class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'잔액: {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'잔액이 부족합니다 현재 잔액: {self.balance}')
        elif amount <= self.balance:
            print(f'출금되었습니다 현재 잔액: {int(self.balance) - int(amount)}')
        else:
            print(f'잔액이 부족합니다 현재 잔액: {self.balance}')

    def get_balance(self):
        return self.balance





# 사용 예시
if __name__ == "__main__":
    my_account = BankAccount("123-456-789", "김철수", 100000)
    my_account.deposit(50000)
    my_account.withdraw(20000)
    print(f"현재 잔액: {my_account.get_balance()}원")