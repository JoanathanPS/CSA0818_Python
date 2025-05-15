accounts = {'user1': {'pin': '1234', 'balance': 1000}}

def check_balance(user):
    return accounts[user]['balance']

def withdraw(user, amount):
    if amount > accounts[user]['balance']:
        return "Insufficient funds"
    accounts[user]['balance'] -= amount
    return f"Withdrawn {amount}. New balance: {accounts[user]['balance']}"

def security_check(pin):
    for user, info in accounts.items():
        if info['pin'] == pin:
            return user
    return None

pin = input("Enter PIN: ")
user = security_check(pin)
if user:
    print(withdraw(user, 500))
else:
    print("Invalid PIN")