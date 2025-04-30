import os

from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = accounts[0]
    # account = accounts.load("freecodecamp-account")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    SimpleStorage.deploy({"from": account})
    stored_value = SimpleStorage[-1].retrieve()
    #print(stored_value)
    transaction = SimpleStorage[-1].store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = SimpleStorage[-1].retrieve()
    print(updated_stored_value)


    # print(account)



def main():
    deploy_simple_storage()