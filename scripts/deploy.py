from brownie import Calculator, accounts, config

def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    print(f"La cuenta con la que vamos a trabajar es {account}")
    calculator = Calculator.deploy(5,4,{
        "from":account,
    },
        publish_source = True
    )


def main():
    deploy()