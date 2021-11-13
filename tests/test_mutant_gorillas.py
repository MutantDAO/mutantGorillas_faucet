from brownie import MutantGorillas, accounts


def test_deploy():
    account = accounts[0]
    mutant_test_rillas = MutantGorillas.deploy(
        "MutantTestGorillase", "MTG", {"from": account}
    )
    initialGorillas = mutant_test_rillas.totalGorillas()
    assert initialGorillas == 0


def test_mint_single():
    times = 1
    account = accounts[0]
    mutant_test_rillas = MutantGorillas.deploy(
        "MutantTestGorillase", "MTG", {"from": account}
    )
    mutant_test_rillas.mint(times, {"from": accounts[1]}).wait(1)
    assert times == mutant_test_rillas.balanceOf(accounts[1])


def test_mint_multiple():
    times = 23
    account = accounts[0]
    mutant_test_rillas = MutantGorillas.deploy(
        "MutantTestCats", "MTC", {"from": account}
    )
    mutant_test_rillas.mint(times, {"from": accounts[1]}).wait(1)
    assert times == mutant_test_rillas.balanceOf(accounts[1])
