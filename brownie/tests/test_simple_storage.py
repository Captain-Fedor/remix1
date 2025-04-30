from brownie import accounts, SimpleStorage

def test_deploy():
    # arranging
    account = accounts[0]
    # acting
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    # asserting
    expected = 0
    actual = simple_storage.retrieve()
    assert expected == starting_value

def test_updating_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    expected = 15
    simple_storage.store(expected, {"from": account})
    actual = simple_storage.retrieve()
    assert expected == actual
