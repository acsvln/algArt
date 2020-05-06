# Generic Euclid algorithm
def euclid(a, q0):
    q1 = a % q0
    while q1 != 0:
        c = q1
        q1 = q0 % q1
        q0 = c
    return q0


# Mutally substracted Euclid algorithm
def euclidMutualSubst(a, q0):
    q1 = a - q0
    while q0 != q1:
        c = q1
        q1 = q1 - q0
        if q1 <= 0:
            q1 = q0
            q0 = c
        pass
    return q0
