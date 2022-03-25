def monnaie(m):
    S1 = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    S2 = [1000, 100, 10, 1]
    T = []
    while m != 0:
        for i in S1: #S1 can be changed into S2 or S3
            while m >= i:
                T.append(i)
                m -= i
    return T
# print(monnaie(1647))
