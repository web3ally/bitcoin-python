class Transaction:

    def __init__(self):
        self.fee = fee
        self.hash = hash
        self.status = status
        self.receivedTime = receivedTime
        self.size = size
        self.weight = weight
        self.blockNum = blockNum
        self.confirmations = self.getConfirmations()
        self.totalInput = totalInput
        self.totalOutput = totalOutput
        self.fees = fees
        self.valueWhenTransacted = valueWhenTransacted
        self.inputs = [{
            'index': 0,
            'address': inputAddress,
            'pkscript': pkscript,
            'sigscript': sigscript,
            'witness': witness
        }]
        self.outputs = [{
            'index': 0,
            'address': outputAddress1,
            'pkscript': pkscript
        }, {
            'index': 1,
            'address': outputAddress2,
            'pkscript': pkscript
        }]