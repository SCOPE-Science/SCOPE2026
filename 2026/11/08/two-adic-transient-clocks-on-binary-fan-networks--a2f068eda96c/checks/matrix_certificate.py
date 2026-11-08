"""Exact GF(2) checks for neighbor-parity iteration on the fan K_1 join P_n.

No floating-point computations or external dependencies.
"""
from collections import Counter


def adjacency(n):
    assert n >= 2
    rows = [(1 << (n + 1)) - 2]
    for i in range(n):
        row = 1
        if i > 0:
            row ^= 1 << i
        if i + 1 < n:
            row ^= 1 << (i + 2)
        rows.append(row)
    return rows


def multiply(A, B):
    result = []
    for row in A:
        bits = row
        value = 0
        while bits:
            bit = bits & -bits
            value ^= B[bit.bit_length() - 1]
            bits ^= bit
        result.append(value)
    return result


def rank(rows):
    pivots = {}
    for r in rows:
        while r:
            k = r.bit_length() - 1
            if k in pivots:
                r ^= pivots[k]
            else:
                pivots[k] = r
                break
    return len(pivots)


def path_polynomials(upto):
    f = [1, 2]
    for i in range(2, upto + 1):
        f.append((f[-1] << 1) ^ f[-2])
    return f


def determinant_poly(A):
    # Independent exact determinant computation by permutation subset DP;
    # in characteristic two, determinant and permanent are equal.
    N = len(A)
    dp = [0] * (1 << N)
    dp[0] = 1
    for mask in range((1 << N) - 1):
        p = dp[mask]
        if not p:
            continue
        i = mask.bit_count()
        for j in range(N):
            if mask & (1 << j):
                continue
            if i == j:
                dp[mask | (1 << j)] ^= p << 1
            elif A[i] & (1 << j):
                dp[mask | (1 << j)] ^= p
    return dp[-1]


def expected_nullity(n, t):
    if t == 0:
        return 0
    if n % 2 == 0:
        return 1
    if n % 4 == 1:
        return 0
    e = (n + 1) & -(n + 1)
    return min(t, 1) + min(t, e - 3)


def main():
    f = path_polynomials(110)
    for n in range(2, 15):
        A = adjacency(n)
        char = determinant_poly(A)
        target = (f[n] << 1) if n % 2 == 0 else 0
        if n % 2:
            # ((z+1)*f_k)^2 over GF(2): square by inserting zero bits.
            g = (f[(n - 1) // 2] << 1) ^ f[(n - 1) // 2]
            target = sum(1 << (2 * i) for i in range(g.bit_length()) if (g >> i) & 1)
        assert char == target, (n, bin(char), bin(target))
    print('CHAR_POLY_OK n=2..14: independent polynomial determinant')
    for n in range(2, 97):
        A = adjacency(n)
        N = n + 1
        P = [1 << i for i in range(N)]
        e = (n + 1) & -(n + 1)
        deadline = max(3, e - 3 if n % 4 == 3 else 1) + 1
        for t in range(deadline + 1):
            assert N - rank(P) == expected_nullity(n, t), (n, t)
            P = multiply(A, P)
    print('ITERATE_NULLITIES_OK n=2..96 at every transient layer and beyond')
    for s in (2, 3, 4, 5, 6):
        n = (1 << s) - 1
        A = adjacency(n)
        N = n + 1
        plus_I = [A[i] ^ (1 << i) for i in range(N)]
        assert N - rank(plus_I) == 1
    print('SPECIAL_EIGENVALUE_ONE_OK n=3,7,15,31,63')


if __name__ == '__main__':
    main()
