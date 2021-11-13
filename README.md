# DEPLOY INFINITE MUTANT GORILLAS

## Usage

Deployed address on Ropsten: [0x7139C189785e0bB8391b7e76A2EF89691D4DebD5](https://ropsten.etherscan.io/address/0x7139C189785e0bB8391b7e76A2EF89691D4DebD5)

Head to etherscan and mint a gorilla!

https://ropsten.etherscan.io/address/0x7139C189785e0bB8391b7e76A2EF89691D4DebD5#writeContract

![image](https://user-images.githubusercontent.com/93621943/141387626-404ba46c-4f11-474c-b591-3b772fca23c4.png)

Connect your wallet, number of gorillas and mint a gorilla!

## Deployment (brownie)

Clone this repo

Create an env file with the deatils of your accounts:

.env file required to look something like this:

```
export WEB3_INFURA_PROJECT_ID=928374....
export PRIVATE_KEY="0xf938r...."
export ETHERSCAN_TOKEN=ZPXODL...
```

Install dependencies

```
Brownie v1.17.0
```
Compile project

```
brownie compile
```

Test the project
```
brownie test
```

Deploy contract

```
brownie run scripts/deploy.py --networks ropsten
```

Verify on etherscan

```
Verification commands are automatically included when passing the networks option ropsten (in scripts/deploy.py)
```
