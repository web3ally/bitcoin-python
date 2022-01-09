# Bitcoin in Python

A pythonic implementation of bitcoin optimizing for pedagogy over practicality.


### 🤷🏼‍♀️ What is bitcoin? 🤷🏼‍♀️

As I chronicle my tour of web3 concepts, I think it makes sense to begin at the start, with Satoshi Nakamoto. 


### 🤔 What problem does bitcoin solve? 🤔

Bitcoin is a digital currency that attempts to turstlessly solve the double-spending problem. Digital currencies have existed before, for example Club Penguin coin, but Bitcoin is the first time a digitally transactable currency was provably unable to be double-spent without requiring a trusted third party. Physical gold and physical dollars both have the property where if given to one person, they must necessarily be taken from another person. Club Penguin could enforce the debiting of one account in equal amount to the credit applied to another account when performing a transfer, but who's to say Club Penguin couldn't credit themselves with as many CP coins as they'd like? This would be inflationary for all CP coin holders and the existence of this type of action breaks any legitimate exchange between Club Penguin coins and globally used currencies. 


### 😔 What are bitcoin’s flaws? 😔

Bitcoin is not without its flaws. 

1. Volatility: Price volatility makes it suboptimal to transact in BTC. Imagine you run a pizza shop. You buy ingredients days in advance, negotiate contracts weeks in advance, and purchase your location months in advance before selling your pizza. You also have bills due in days, weeks, and months. You’re in a competitive market so your margins are razor-thin. You expect to make 1% in profit on each pizza sold. If customers pay in bitcoin and bitcoin’s average daily volatility is 5%, there’s a high probability that BTC moves against you and you can’t pay your debts denominated in your local currency. Because of your likely concave utility function, added volatility tends to make you unhappy. For this reason, stablecoins denominated in the users’ local currency are a good solution to the volatility issue. 
2. High transaction fees: This time last year the average BTC transaction fee was $20. For the average user, this is still prohibitive for small purchases and transfers. The avg tx fee has since been reduced to nearly $2.
3. Irreversibility: Once a transaction is performed, there's no guarantee that you'll be able to reverse it in the case of mistake or fraud. 
4. Privacy: All transactions are broadcast to the full network. While your public key might not be immediately known, the more transactions you perform the more info you leak about yourself as a user. Remember this is a public, immutable, unstoppable data structure. 
5. Settlement time: Bitcoin blocks take ~10 minutes to validate. This is far too long for any irl use case. You wouldn’t wait for 10 minutes at a grocery store to have your payment validated. This has since been relatively well solved by other L1s and some Ethereum scaling solutions. 


### 🤯 How does bitcoin work? 🤯

Bitcoin is essentially a linked list of hashed “blocks” of transactions. These linked blocks form a “block chain”.

Appending a block to the chain requires an immense amount of computation. This proof-of-work system allows virtuous miners to prevent any set of attacking miners who control <50% of the total hashing power to append their own fraudulent blocks to the chain. Virtuous miners with >50% of the hashing power will be able to maintain the longest chain thereby keeping the network valid and secure.

Initially, anyone with a CPU could participate in keeping the network secure. Nowadays giant mining farms work around the clock to keep the network secure. 

In order to solve the double-spending problem without a trusted third party, we need a way to order transactions coming in from anywhere around the globe. If transactions can be uniquely timestamped, the second of a double-spend can be invalidated. This is done by publishing a hash of a newspaper post that would be impossible to create before a particular moment in time. Each subsequent timestamp includes the previous timestamp in its hash thereby creating a chain of timestamped blocks. 


### My Questions
1. Why is SHA256 computed twice when hashing?