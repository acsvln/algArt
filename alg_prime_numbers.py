from math import sqrt


def bruteforce(N):
    result = []
    for k in range(2, N + 1):
        flag = True
        for j in range(2, int(sqrt(k)) + 1):
            if k % j == 0:
                flag = False
        if flag:
            result.append(k)

    return result


def eratosthenes(N):
    result = list(range(2, N + 1))

    for k in range(0, len(result)):
        if result[k] != 0:
            for j in range(k + 1, len(result)):
                if result[j] % result[k] == 0:
                    result[j] = 0
    return filter(lambda x: x != 0, result)


# TODO: we used here some weird version of algo, but it works.
# TODO: need to check original version and implement it correctly
def sundaram(N):
    result = list(range(1, N + 1))
    # Border
    for i in range(1, N/3):
        for j in range(1, (N - i)/(2*i + 1)):
            # m=2*i*j + i + j
            m = (2 * i + 1) * (2 * j + 1)
            if m < N:
                result[m - 1] = 0
    return filter(lambda x: x >= 2 and ((x == 2) or (x % 2 != 0)), result)


def atkin(limit):
    sqr_lim = int(sqrt(limit))
    simples = [False] * limit
    simples[2] = True
    simples[3] = True
    x2 = 0
    for i in range(1, sqr_lim + 1):
        x2 = x2 + 2 * i - 1
        y2 = 0
        for j in range(1, sqr_lim + 1):
            y2 = y2 + 2 * j - 1
            n = 4 * x2 + y2
            if (n < limit) and (((n % 12) == 1) or ((n % 12) == 5 )):
                simples[n] = not simples[n]
            n = n - x2
            if (n <= limit) and ((n % 12) == 7):
                simples[n] = not simples[n]
            n = n - 2 * y2

            if (i > j) and (n < limit) and ((n % 12) == 11):
                simples[n] = not simples[n]

    for i in range(5, sqr_lim + 1):
        if simples[i]:
            n = i * i
            j = n
            while j <= limit:
                simples[j] = False
                j = j + limit

    result = []
    for index, element in enumerate(simples):
        if element:
            result.append(index)
    return result
