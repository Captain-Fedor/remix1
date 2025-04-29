from solcx import compile_standard, install_solc

import json
from web3 import Web3
import os
from dotenv import load_dotenv
from web3.datastructures import AttributeDict


load_dotenv()

install_solc("0.8.0")

with open("./contracts/SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()


compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.8.0",
)
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# connection to ganache
# w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
# chain_id = 1337
# my_address = "0xB2f876D62742b8ACE5C70F2D435527b51273A997"

# connection to infura
w3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/709971e5b336419da2fd37d21a67b0ad"))
chain_id = 11155111
# address from metamask
my_address = "0x4eF361D07ac68618A7854EF0F022A3A81fc1ad82"





# private_key = "0x5ac65577243c715055692e5573bd57989208f2d0e5cd2a3016235c0d169f731c"
private_key = os.getenv("PRIVATE_KEY")
other_var = os.getenv("OTHER_VAR")

SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# print(SimpleStorage)
# get latest transaction
nonce = w3.eth.get_transaction_count(my_address)

# create transactions
transaction = SimpleStorage.constructor().build_transaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce}
)


# First sign the transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# Send the signed transaction
send_store_txn = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_txn)


# WORKING WITH CONTRACT

simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
# call
# transact
print(simple_storage.functions.retrieve().call())
# print(simple_storage.functions.store(15).call())

store_transaction = simple_storage.functions.store(15).build_transaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce + 1}
)
signed_store_txn = w3.eth.account.sign_transaction(store_transaction, private_key=private_key)
send_store_txn = w3.eth.send_raw_transaction(signed_store_txn.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_txn)
print(simple_storage.functions.retrieve().call())




# creating a json file from the transaction receipt

def attribute_dict_to_dict(attr_dict):
    if isinstance(attr_dict, AttributeDict):
        return {key: attribute_dict_to_dict(value) for key, value in attr_dict.items()}
    elif isinstance(attr_dict, list):
        return [attribute_dict_to_dict(item) for item in attr_dict]
    elif isinstance(attr_dict, (bytes, bytearray)):
        return attr_dict.hex()
    return attr_dict
with open('tx_receipt.json', 'w') as file:
    json.dump(attribute_dict_to_dict(tx_receipt), file, indent=4)


