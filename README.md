# Bitcoin in Python

A pythonic implementation of bitcoin optimizing for pedagogy over practicality.


### 🤷🏼‍♀️ What is bitcoin? 🤷🏼‍♀️

As I chronicle my tour of web3 concepts, I think it makes sense to begin at the start, with Satoshi Nakamoto. 


### 🤔 What problem does bitcoin solve? 🤔

Bitcoin is a digital currency that attempts to turstlessly solve the double-spending problem. Digital currencies have existed before, for example Club Penguin coin, but Bitcoin is the first time a digitally transactable currency was provably unable to be double-spent without requiring a trusted third party. Physical gold and physical dollars both have the property where if given to one person, they must necessarily be taken from another person. Club Penguin could enforce the debiting of one account in equal amount to the credit applied to another account when performing a transfer, but who's to say Club Penguin couldn't credit themselves with as many CP coins as they'd like? This would be inflationary for all CP coin holders and the existence of this type of action breaks any legitimate exchange between Club Penguin coins and globally used currencies. 


### 🤯 How does bitcoin work? 🤯

Bitcoin is essentially a linked list of hashed “blocks” of transactions. These linked blocks form a “block chain”.

Appending a block to the chain requires a certain amount of computation. This proof-of-work system allows virtuous miners to prevent any set of attacking miners who control <50% of the total hashing power to append their own fraudulent blocks to the chain. Virtuous miners with >50% of the hashing power will be able to maintain the longest chain thereby keeping the network valid and secure.

Initially, anyone with a CPU could participate in keeping the network secure. Nowadays giant mining farms work around the clock to keep the network secure. 

In order to solve the double-spending problem without a trusted third party, we need a way to order transactions coming in from anywhere around the globe. If transactions can be uniquely timestamped, the second of a double-spend can be invalidated. This is done by publishing a hash of a newspaper post that would be impossible to create before a particular moment in time. Each subsequent timestamp includes the previous timestamp in its hash thereby creating a chain of timestamped blocks. 

By combining novel cryptographic primitives in this way, Satoshi Nakamoto was able to create the public distributed ledger that we now know today as bitcoin.


### 😔 What are bitcoin’s flaws? 😔

Bitcoin is not without its flaws. 

1. Volatility: Price volatility makes it suboptimal to transact in BTC. Imagine you run a pizza shop. You buy ingredients days in advance, negotiate contracts weeks in advance, and purchase your location months in advance before selling your pizza. You also have bills due in days, weeks, and months. You’re in a competitive market so your margins are razor-thin. You expect to make 1% in profit on each pizza sold. If customers pay in bitcoin and bitcoin’s average daily volatility is 5%, there’s a high probability that BTC moves against you and you can’t pay your debts denominated in your local currency. Because of your likely concave utility function, added volatility tends to make you unhappy. For this reason, stablecoins denominated in the users’ local currency are a good solution to the volatility issue. 
2. High transaction fees: This time last year the average BTC transaction fee was $20. For the average user, this is still prohibitive for small purchases and transfers. The avg tx fee has since been reduced to nearly $2.
3. Irreversibility: Once a transaction is performed, there's no guarantee that you'll be able to reverse it in the case of mistake or fraud. 
4. Privacy: All transactions are broadcast to the full network. While your public key might not be immediately known, the more transactions you perform the more info you leak about yourself as a user. Remember this is a public, immutable, unstoppable data structure. 
5. Settlement time: Bitcoin blocks take ~10 minutes to validate. This is far too long for any irl use case. You wouldn’t wait for 10 minutes at a grocery store to have your payment validated. This has since been relatively well solved by other L1s and some Ethereum scaling solutions. 


### 🧮 What is Hashing? 🧮

SHA-256 is a type of one-way cryptographic function which takes in arbitrary data and generates a corresponding almost-unique 256-bit signature.

Because of their one-way nature, they can be used to prove the authenticity of data without revealing any of that data’s underlying information.


### 💸 How is a bitcoin transaction created? 💸

Suppose Alice wants to pay Bob for a pizza. The slice costs $5 or 0.0001 BTC at the current BTC-USD exchange rate of $50,000. 

Each transaction contains sets of "inputs" and "outputs". These are the debits and credits of the transaction respectively. The miner takes an implicit transaction fee which is the sum of inputs minus the sum of outputs. 

Ownership of each input must be proven for the transaction to be valid. This is done cryptographically by __________

Alice simply chooses the destination (Bob's wallet) and the amount (0.0001 BTC) and her wallet will handle the rest. 

Well, how does her wallet construct the transaction?

Most full-node bitcoin wallets contain an up-to-date log of the unspent balances for all users. This allows the wallet to quickly find valid inputs to construct transactions, and it allows the wallet to efficiently verify that incoming transactions are valid. This is quite a lot of data for the wallet to store so in practice lightweight-nodes store only the transaction data of their particular user. 

If the correct data is not stored in the wallet, it's straight-forward to query the bitcoin network's API for all unspent transactons for a specified user. 

The inputs and their proof-of-ownership along with the outputs form the bitcoin transaction. To understand how a transaction gets added to the ledger, check out my next thread. 

You can also see more details on my github repo where I implement bitcoin's functionality in python. 


### How does a transaction get added to the ledger?

Here a transaction gets sent to the bitcoin network, the transcation gets added to a block, the block is mined, and once added to the blockchain the transaction becomes trusted and verifiable to all.

A transaction gets propogated to all nodes in the bitcoin network through the following mechanism. When a node receives a valid transaction is hasn't seen before, it broadcasts it out to other nodes in the network. This this process called flooding, all nodes are rapidly made aware of the particular transaction. 

Bob's wallet application will also receive the transaction within seconds, and he can verify himself that it's well formatted, includes his correct payment address, and uses inputs which have enough funds to pay him and the miner.


### ⛏ How does bitcoin mining work? ⛏

Bitcoin's proof-of-work system requires significant computational power to add a block to the chain but is extremely fast to validate. 

Miners must validate all transactions before adding them to a block. If a transaction is invalid, other nodes will consider this miner's block to be invalid and the chain will fork and continue to grow without the miners invalid block. 

Specifically, the computational puzzle that the miners compete to solve is hashing the header of the block and a random number called a nonce using SHA-256 until the value of the hash begins with a particular number of zeros. 

The difficulty of the computational puzzle that miners must solve to append a new block is adjusted regularly to ensure on average it takes roughly 10 minutes to mine a block. This is done by changing the specified number of zeroes the SHA-256 hash must begin with. 

Miners receive fees on each transaction as well as new bitcoin that's minted every block. Miners order transactions to add to their candidate blocks by a priority metric which is defined as the transaction fee multiplied by the age of the block divided by the size of the transaction. 


### My Questions
1. Why is SHA256 computed twice when hashing?