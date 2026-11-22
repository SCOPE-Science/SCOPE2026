"""Independent exact integer tests for polynomial-value unitary-divisor matrices.

Run with Python 3 only; no nonstandard packages. Finite checks support,
but do not replace, the all-modulus Smith-form proof.
"""
from itertools import product
from math import gcd, prod


def smith(A):
    """Exact Euclidean integer Smith reductions, returning all diagonal factors."""
    A = [list(row) for row in A]
    n = len(A)
    m = len(A[0]) if n else 0
    k = 0
    while k < min(n, m):
        nz = [(abs(A[i][j]), i, j) for i in range(k, n)
              for j in range(k, m) if A[i][j]]
        if not nz:
            break
        _, i, j = min(nz)
        A[k], A[i] = A[i], A[k]
        for row in A:
            row[k], row[j] = row[j], row[k]
        for _ in range(10000):
            changed = False
            for i in range(k + 1, n):
                if A[i][k]:
                    q = A[i][k] // A[k][k]
                    A[i] = [u - q*v for u, v in zip(A[i], A[k])]
                    if A[i][k]:
                        A[k], A[i] = A[i], A[k]
                    changed = True
                    break
            if changed:
                continue
            for j in range(k + 1, m):
                if A[k][j]:
                    q = A[k][j] // A[k][k]
                    for row in A:
                        row[j] -= q * row[k]
                    if A[k][j]:
                        for row in A:
                            row[k], row[j] = row[j], row[k]
                    changed = True
                    break
            if changed:
                continue
            notdiv = next(((i, j) for i in range(k + 1, n)
                           for j in range(k + 1, m) if A[i][j] % A[k][k]), None)
            if notdiv is None:
                if A[k][k] < 0:
                    A[k] = [-x for x in A[k]]
                break
            i, _ = notdiv
            A[k] = [x + y for x, y in zip(A[k], A[i])]
        else:
            raise AssertionError('Integer Smith reductions exceeded bound')
        k += 1
    return [abs(A[i][i]) for i in range(min(n, m))]


def prime_power_factors(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            q = 1
            while n % d == 0:
                q *= d
                n //= d
            ans.append(q)
        d += 1
    if n > 1:
        ans.append(n)
    return ans


def factor_integer(n):
    ret = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            ret[d] = ret.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        ret[n] = ret.get(n, 0) + 1
    return ret


def smith_predicted(n, P):
    if n == 1:
        return [1]
    lists = []
    rank = 1
    for q in prime_power_factors(n):
        s = len({P(x) % q for x in range(q)})
        rank *= s
        if s == 1:
            lists.append([q])
        else:
            lists.append([1] + [q - 1] * (s - 2) + [(q - 1) * (q - 1 + s)])
    raw = [prod(row) for row in product(*lists)]
    primes = sorted({p for v in raw for p in factor_integer(v)})
    valuations = {p: sorted(factor_integer(v).get(p, 0) for v in raw) for p in primes}
    factors = [prod(p ** valuations[p][j] for p in primes) for j in range(rank)]
    return factors + [0] * (n - rank)


def smith_direct(n, P):
    qs = prime_power_factors(n)
    matrix = [[prod(q if (P(i) - P(j)) % q == 0 else 1 for q in qs)
               for j in range(n)] for i in range(n)]
    return smith(matrix)


def square_count_formula(p, a):
    if p == 2:
        return 1 + sum(1 if h in (1, 2) else 2 ** (h - 3)
                       for h in range(a, 0, -2))
    return 1 + (p - 1) * sum(p ** (a - 2*j - 1)
                             for j in range((a - 1)//2 + 1)) // 2


def run():
    P_list = [lambda x: x, lambda x: x*x, lambda x: x*x+x,
              lambda x: x*x*x-3*x, lambda x: 7]
    inputs = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,18,20,21,24]
    assertions = 0
    for P in P_list:
        for n in inputs:
            got = smith_direct(n, P)
            expected = smith_predicted(n, P)
            assert got == expected, (n, got, expected)
            assertions += 1
    for p, amax in [(2,10), (3,7), (5,5), (7,4), (11,3)]:
        for a in range(1, amax + 1):
            q = p**a
            got = len({(i*i) % q for i in range(q)})
            expected = square_count_formula(p, a)
            assert got == expected, (p, a, got, expected)
            assertions += 1
    assert smith_predicted(15, lambda x:x*x) == [1,4,4,8,224,224] + [0]*9
    assertions += 1
    assert smith_predicted(9, lambda x:x*x) == [1,8,8,96]+[0]*5
    assertions += 1
    print('PASS:', assertions, 'exact grouped tests (including all direct Smith forms and square images)')

if __name__ == '__main__':
    run()
