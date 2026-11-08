"""Independent small-field enumeration for the radius-four flag-rank sphere.

Requires Python 3.10+ (standard library only). Run: python3 checker.py
All matrices are enumerated, not sampled, for each indicated small parameter.
"""
from itertools import product
from math import comb


def operations(q):
    if q == 4:
        # Represent F_4 = F_2[t]/(t^2+t+1) by a+b*t, a,b in {0,1}.
        def add(a, b):
            return a ^ b
        def mul(a, b):
            a0, a1 = a & 1, (a >> 1) & 1
            b0, b1 = b & 1, (b >> 1) & 1
            return (a0*b0 ^ a1*b1) | ((a0*b1 ^ a1*b0 ^ a1*b1) << 1)
        invs = {1: 1, 2: 3, 3: 2}
        return add, lambda a,b:a^b, mul, lambda a:invs[a]
    if q not in (2, 3, 5):
        raise ValueError('Only F_2,F_3,F_4,F_5 are used in the exhaustive test')
    return (lambda a,b:(a+b)%q, lambda a,b:(a-b)%q,
            lambda a,b:a*b%q, lambda a:pow(a,-1,q))


def rank(rows, q, ops):
    add, sub, mul, inverse = ops
    arr = [list(row) for row in rows]
    m = len(arr)
    if m == 0:
        return 0
    ncols = len(arr[0])
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, m) if arr[i][c] != 0), None)
        if pivot is None:
            continue
        arr[r], arr[pivot] = arr[pivot], arr[r]
        inv = inverse(arr[r][c])
        arr[r] = [mul(v, inv) for v in arr[r]]
        for i in range(r+1, m):
            factor = arr[i][c]
            if factor:
                arr[i] = [sub(a, mul(factor, b)) for a,b in zip(arr[i], arr[r])]
        r += 1
        if r == m:
            break
    return r


def sphere4_formula(n, q):
    assert n >= 3 and q >= 2
    u = q-1
    t = q*q + q - 1
    c = lambda k: comb(n-3,k) if n-3 >= k else 0
    return ((n-3)*u*t**3 + 3*c(2)*u*u*t*t +
            3*c(3)*u**3*t + c(4)*u**4 +
            (n-2)*q**3*u*u*(q+1))


def exhaustive(n, q):
    positions = [(i,j) for i in range(n) for j in range(i,n)]
    ops = operations(q)
    count = 0
    full_one = 0
    triple_121 = 0
    total = 0
    for vals in product(range(q),repeat=len(positions)):
        A = [[0]*n for _ in range(n)]
        for (i,j), val in zip(positions, vals):
            A[i][j] = val
        ranks = tuple(rank([row[i:] for row in A[:i+1]],q,ops)
                      for i in range(n))
        if sum(ranks) == 4:
            count += 1
            if n == 3 and ranks == (1,2,1):
                triple_121 += 1
        if all(k == 1 for k in ranks):
            full_one += 1
        total += 1
    return count, full_one, triple_121, total


def main():
    configurations = [(3,2), (3,3), (3,4), (3,5),
                      (4,2), (4,3), (5,2)]
    for n,q in configurations:
        actual, all_one, triple_121, total = exhaustive(n,q)
        expected = sphere4_formula(n,q)
        assert actual == expected, (n,q,actual,expected)
        if n in (3,4):
            expected_ones = (q-1)*(q*q+q-1)**(n-1)
            assert all_one == expected_ones, (n,q,all_one,expected_ones)
        if n == 3:
            assert triple_121 == q*q*(q*q-1)*(q*q-q)
        print(f'n={n} q={q} matrices={total} sphere4={actual} : PASS')
    print('ALL_CHECKS_PASSED')

if __name__ == '__main__':
    main()
