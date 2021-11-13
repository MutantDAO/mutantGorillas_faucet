from brownie import accounts, config, MutantGorillas, network
import os

# import /.helpful_scripts as utils


def get_active_network():
    return network.show_active()


def get_account():
    if network.show_active() == "development":
        print(accounts.add(config["wallets"]["from_key"]))
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    account = get_account()
    print(account)
    if get_active_network == "development":
        mutant_gorillas = MutantGorillas.deploy(
            "TestGorillas", "TGOR", {"from": account}
        )
    else:
        mutant_gorillas = MutantGorillas.deploy(
            "TestGorillas", "TGOR", {"from": account}, publish_source=True
        )
    pass
