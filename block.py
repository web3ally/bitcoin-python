class Block:

    def __init__(self, version, prevBlockHash, merkleRoot, timestamp, transactions, bits, nonce):
        self.version = version
        self.prevBlockHash = prevBlockHash
        self.merkleRoot = merkleRoot
        self.timestamp = timestamp
        self.transactions = transactions
        self.bits = bits
        self.nonce = nonce

    def getHeader(self, nonce):
        header = str(self.version) + \
                 str(self.prevBlock) + \
                 str(self.merkleRoot) + \
                 str(self.timestamp) + \
                 str(self.bits) + \
                 str(nonce)

        return header