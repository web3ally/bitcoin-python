def getAttackerSuccessProbability(q, z):
    p = 1 - q
    Lambda = z * (q / p)
    Sum = 1
    for k in range(z):
        poisson = exp(-lambda)
        for i in range(k):
            poisson *= Lambda / i
            Sum -= poisson * (1-pow(q / p, z - k))
    return Sum
