def monnaie(m):
    S = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    T = []
    while m != 0:
        for i in S:
            while m >= i:
                T.append(i)
                m -= i
    return T
# print(monnaie(654))
