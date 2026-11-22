#!/usr/bin/env python3
"""Standard-library, exact-integer reconstruction of two-boson characteristic polynomials.
Public reproducibility code for finite checks; the infinite claim follows from the proof.
"""
from itertools import combinations_with_replacement

def hamiltonian(m, n, u):
    assert m >= 2 and n >= 2 and isinstance(u, int)
    s = list(combinations_with_replacement(range(m+n), 2))
    at = {v: i for i, v in enumerate(s)}
    h = [[0 for _ in s] for _ in s]
    for i, (a, b) in enumerate(s):
        if a == b:
            h[i][i] = u
        for k in (0, 1):
            x = (a, b)[k]
            for y in (range(m, m+n) if x < m else range(m)):
                t = tuple(sorted((y, b) if k == 0 else (a, y)))
                h[at[t]][i] -= 1
    # This integer matrix is similar to the physical Hermitian matrix:
    # doublon columns / rows are rescaled by sqrt(2) and its inverse.
    return h

def polynomial_product(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i+j] += v*w
    return c

def predicted(m, n, u):
    z = 1 + (m-1)*(n-1)
    if m >= 4: z += m*(m-3)//2
    if n >= 4: z += n*(n-3)//2
    # Coefficients in ascending order of x.
    p = polynomial_product([-u,1], [0]*z+[1])
    p = polynomial_product(p,[2*u*(2*m*n-m-n),-4*m*n,-u,1])
    a = [n*(m-2)*u,-m*n,-u,1] if m >= 3 else [-2*n,-u,1]
    b = [m*(n-2)*u,-m*n,-u,1] if n >= 3 else [-2*m,-u,1]
    for _ in range(m-1): p = polynomial_product(p,a)
    for _ in range(n-1): p = polynomial_product(p,b)
    return list(reversed(p))

def characteristic_via_newton(h):
    d = len(h)
    # Polynomial x^d + c[1] x^(d-1) + ... + c[d].
    c, traces = [1], [0]
    powers = [[int(i==j) for j in range(d)] for i in range(d)]
    nonzero = [[(j,v) for j,v in enumerate(row) if v] for row in h]
    for k in range(1,d+1):
        nxt = [[0]*d for _ in range(d)]
        for i in range(d):
            for l, val in nonzero[i]:
                q = powers[l]
                row = nxt[i]
                for j in range(d): row[j] += val*q[j]
        powers = nxt
        traces.append(sum(powers[i][i] for i in range(d)))
        numerator = sum(c[k-i]*traces[i] for i in range(1,k+1))
        assert numerator % k == 0
        c.append(-numerator//k)
    return c

def main():
    cases = [(2,2,1),(2,3,2),(3,3,3),(2,5,1),(3,4,2),(4,4,3)]
    for m,n,u in cases:
        got = characteristic_via_newton(hamiltonian(m,n,u))
        target = predicted(m,n,u)
        assert got == target, (m,n,u,got,target)
        print('PASS',m,n,u,'degree',len(got)-1)
    print('All exact finite characteristic-polynomial checks passed.')

if __name__=='__main__': main()
