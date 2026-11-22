#!/usr/bin/env python3
"""Finite exact checks for the cyclic power-GCD Smith theorem.

Python 3 standard library only. Does not certify the universal assertion;
the mathematical proof covers all odd primes and all positive exponents.
"""
from math import gcd, prod


def predicted(p, a):
    A = p ** a
    v = A - 1
    u = A * v
    c = A + p
    alpha = v * c
    beta = alpha + p*p
    d = [1] + [v]*(p-1) + [u]*(p*(p-2)) + [p*u] + [u*c]*(p-2) + [(A//p)*alpha*beta]
    assert len(d) == p*p
    assert all(d[i+1] % d[i] == 0 for i in range(len(d)-1))
    assert prod(d) == u ** (p*p-p) * alpha ** (p-1) * beta
    return d


def factor(n):
    f = {}
    q = 2
    while q*q <= n:
        while n % q == 0:
            f[q] = f.get(q, 0) + 1
            n //= q
        q = 3 if q == 2 else q + 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def valuation(n, ell, bound):
    if n == 0:
        return bound
    k = 0
    while k < bound and n % ell == 0:
        k += 1
        n //= ell
    return k


def modular_smith_valuations(matrix, ell, precision):
    """Independent elementary row and column operations modulo ell^precision.
    This produces truncated local Smith valuations, not determinants/eigenvalues.
    """
    n = len(matrix)
    mod = ell ** precision
    M = [[x % mod for x in row] for row in matrix]
    exponents = []
    for k in range(n):
        best = precision
        pi = pj = -1
        for i in range(k, n):
            for j in range(k, n):
                z = valuation(M[i][j], ell, precision)
                if z < best:
                    pi, pj, best = i, j, z
                    if z == 0:
                        break
            if best == 0:
                break
        if pi < 0:
            exponents.extend([precision]*(n-k))
            break
        M[k], M[pi] = M[pi], M[k]
        for row in M:
            row[k], row[pj] = row[pj], row[k]
        q = ell ** best
        assert M[k][k] % q == 0
        inverse = pow((M[k][k]//q) % (mod//q), -1, mod//q)
        for i in range(k+1, n):
            assert M[i][k] % q == 0
            coefficient = ((M[i][k]//q) * inverse) % (mod//q)
            if coefficient:
                for j in range(k, n):
                    M[i][j] = (M[i][j]-coefficient*M[k][j]) % mod
            assert M[i][k] == 0
        for j in range(k+1, n):
            assert M[k][j] % q == 0
            coefficient = ((M[k][j]//q) * inverse) % (mod//q)
            if coefficient:
                for i in range(k, n):
                    M[i][j] = (M[i][j]-coefficient*M[i][k]) % mod
            assert M[k][j] == 0
        exponents.append(best)
    return exponents


def gcd_power_circulant(p, a):
    n = p*p
    return [[gcd((x-y) % n, n)**a for y in range(n)] for x in range(n)]


def run():
    total = 0
    for p, a in [(3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(7,1)]:
        d = predicted(p, a)
        G = gcd_power_circulant(p, a)
        n = p*p
        A=p**a
        u=A*(A-1)
        v=A-1
        # exact matrix identity: uI+v(block-constant)+J
        for i in range(n):
            for j in range(n):
                expect = u*(i==j) + v*(i%p==j%p) + 1
                assert G[i][j] == expect
                total+=1
        F = factor(d[-1])
        for ell in F:
            maxv = valuation(d[-1], ell, 1000)
            obtained = modular_smith_valuations(G, ell, maxv+2)
            expected = [valuation(x,ell,maxv+2) for x in d]
            assert obtained == expected, (p,a,ell,obtained,expected)
            total += len(d)
        print('PASS p={}, a={}, size={}, checked primes={}, max factor={}'.format(p,a,n,sorted(F),d[-1]))
    print('PASS: {} exact assertions, local Smith factors and all entry identities'.format(total))


if __name__ == '__main__':
    run()
