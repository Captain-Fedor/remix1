import os

from brownie import accounts, config, SimpleStorage, network
import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()


def deploy_simple_storage():
    test_infura()
    verify_setup()
    account = get_account()

    # account = accounts.load("freecodecamp-account")
    # account = accounts.add(os.getenv(b"PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    SimpleStorage.deploy({"from": account})
    stored_value = SimpleStorage[-1].retrieve()
    #print(stored_value)
    transaction = SimpleStorage[-1].store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = SimpleStorage[-1].retrieve()
    # print(updated_stored_value)


def get_account():


    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

    # print(account)


def test_infura():
    load_dotenv()

    # Get the Infura Project ID
    infura_project_id = os.getenv('WEB3_INFURA_PROJECT_ID')
    if not infura_project_id:
        print("ERROR: WEB3_INFURA_PROJECT_ID not found in .env file")
        return

    # Construct the Infura URL
    infura_url = f"https://sepolia.infura.io/v3/{infura_project_id}"

    # Try to connect
    w3 = Web3(Web3.HTTPProvider(infura_url))

    try:
        # Test basic connection
        is_connected = w3.is_connected()
        print(f"Connection test: {'SUCCESS' if is_connected else 'FAILED'}")

        if is_connected:
            # Get some basic network info
            block_number = w3.eth.block_number
            print(f"Current block number: {block_number}")

            # Try to get gas price
            gas_price = w3.eth.gas_price
            print(f"Current gas price: {gas_price}")
    except Exception as e:
        print(f"Error during connection test: {str(e)}")
        print("\nPlease verify:")
        print("1. Your Infura Project ID is correct")
        print("2. Sepolia network is enabled in your Infura project")
        print("3. Your Project ID has not expired")
        print("4. There are no spaces or quotes in your .env file")


def verify_setup():
    # Check if environment variables are loaded
    infura_id = os.getenv('WEB3_INFURA_PROJECT_ID')
    print(f"Infura Project ID present: {'Yes' if infura_id else 'No'}")
    if infura_id:
        print(f"Project ID length: {len(infura_id)}")
        print(f"First few chars: {infura_id[:6]}...")

    # Check network configuration
    print(f"Active network: {network.show_active()}")



def main():
    deploy_simple_storage()