from math import sqrt


def ferm(A):
    def findB(delta):
        is_perfect = False
        while is_perfect is False:
            B = sqrt(A) + delta
            C = sqrt(pow(B, 2) - A)
            delta += 1
            is_perfect = C.is_integer
        return (delta, B)

    def isTrivial(first, second):
        return (first == A) and (second == 1)

    doing = True
    delta = 1
    while doing:
        res = findB(delta)
        delta = res[0]
        B = res[1]

        left = (B - sqrt(pow(B, 2) - A))
        right = (B + sqrt(pow(B, 2) - A))

        trivial = isTrivial(right, left) or isTrivial(left, right)

        if not trivial:
            doing = False
        else:
            delta += 1
    return (left, right)
