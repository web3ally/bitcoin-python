from block import Block
from hasher import Hasher

class Miner:

    def __init__(self, hashpwoer, curBlock):
        self.hashpower = hashpower
        self.curBlock = curBlock
        self.hasher = Hasher()

    def mine(self):
        nonces = []
        for nonce in nonces:
            hasher.doubleSHA256(curBlock.getHeader(nonce))