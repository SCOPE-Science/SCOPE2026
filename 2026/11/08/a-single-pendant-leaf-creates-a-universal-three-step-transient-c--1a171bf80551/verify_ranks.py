"""Exact GF(2) matrix replay for neighbor-parity on a pendant hypercube.
Run with Python 3, no dependencies.
"""

def rows(n):
    V = 1 << n
    a = []
    for v in range(V):
        row = 0
        for bit in range(n):
            row ^= 1 << (v ^ (1 << bit))
        if v == 0:
            row ^= 1 << V
        a.append(row)
    a.append(1)
    return a


def mm(a, b):
    out = []
    for mask in a:
        v = 0
        while mask:
            low = mask & -mask
            v ^= b[low.bit_length() - 1]
            mask ^= low
        out.append(v)
    return out


def rank(rows_):
    pivots = {}
    for row in rows_:
        while row:
            j = row.bit_length() - 1
            if j not in pivots:
                pivots[j] = row
                break
            row ^= pivots[j]
    return len(pivots)


def expected(n):
    V = 1 << n
    if n % 2:
        return [V, V - 1, V - 2, V - 2, V - 2]
    return [V // 2 + 2, 3, 2, 2, 2]


def check():
    for n in range(1, 9):
        a = rows(n)
        power = a
        actual = []
        powers = []
        for t in range(1, 6):
            actual.append(rank(power))
            powers.append(power)
            power = mm(a, power)
        assert actual == expected(n), (n, actual, expected(n))
        assert powers[2] == powers[4], f'F^3 != F^5 for n={n}'
        I = [1 << j for j in range(len(a))]
        assert rank([a[j] ^ I[j] for j in range(len(a))]) == len(a) - (1 if n % 2 == 0 else ((1 << n) - 2) // 2)
        print(f'n={n} vertices={len(a)} ranks={actual} F3=F5 fixed_subspace_verified')
    print('PASS: all exact GF(2) ranks, fixed-space dimensions and F^5=F^3 for n=1..8')

if __name__ == '__main__':
    check()
