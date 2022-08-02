from brownie import Calculator, accounts, config

def sumar():
    print("voy a sumar")
    account = accounts.add(config["wallets"]["from_key"])
    calculator = Calculator[0]
    calculator.sumar
    print("Sumé")

def main():
    sumar()