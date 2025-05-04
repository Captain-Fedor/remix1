from web3 import Web3
import os
from dotenv import load_dotenv
import json


def test_infura():
    load_dotenv()

    # Get the Infura Project ID
    infura_project_id = os.getenv('WEB3_INFURA_PROJECT_ID')
    if not infura_project_id:
        print("ERROR: WEB3_INFURA_PROJECT_ID not found in .env file")
        return

    print(f"Using Infura Project ID: {infura_project_id[:6]}...")

    # Construct the Infura URL
    infura_url = f"https://sepolia.infura.io/v3/{infura_project_id}"
    print(f"Connecting to: {infura_url[:45]}...")

    # Try to connect
    w3 = Web3(Web3.HTTPProvider(infura_url))

    try:
        # Test connection by requesting block number
        block_number = w3.eth.block_number
        print(f"✓ Connection successful!")
        print(f"✓ Current block number: {block_number}")

        # Get chain ID
        chain_id = w3.eth.chain_id
        print(f"✓ Chain ID: {chain_id}")

        # Get gas price
        gas_price = w3.eth.gas_price
        print(f"✓ Current gas price: {gas_price}")

        return True

    except Exception as e:
        print(f"✗ Connection failed with error: {str(e)}")
        print("\nTroubleshooting steps:")
        print("1. Verify your Infura Project ID is correct")
        print("2. Check if Sepolia is enabled in your Infura project settings")
        print("3. Try creating a new project in Infura")
        print("4. Check your internet connection")
        return False


def deploy_simple_storage():
    # First test the connection
    if not test_infura():
        print("Aborting deployment due to connection issues")
        return

    account = get_account()
    print(f"Deploying from account: {account.address}")

    # Deploy with explicit gas settings
    simple_storage = SimpleStorage.deploy(
        {"from": account,
         "gas_limit": 2000000,  # Explicit gas limit
         "gas_price": Web3.to_wei('50', 'gwei'),  # Explicit gas price
         "allow_revert": True},
        publish_source=False
    )
    return simple_storage


def main():
    deploy_simple_storage()


if __name__ == "__main__":
    test_infura()