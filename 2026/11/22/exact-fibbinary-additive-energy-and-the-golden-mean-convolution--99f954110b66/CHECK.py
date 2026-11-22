#!/usr/bin/env python3
"""Exact standard-library checks for the fibbinary additive-energy theorem."""
from collections import Counter, defaultdict
from math import comb

P = (1, -2, -6, 1, 4, -2)

def is_allowed(n):
    return (n & (n << 1)) == 0

def edges(state):
    mask, carry = state
    for newmask in range(16):
        if newmask & mask:
            continue
        a, b, c, d = ((newmask >> i) & 1 for i in range(4))
        t = a + b - c - d + carry
        if t % 2 == 0 and abs(t // 2) <= 1:
            yield newmask, t // 2

def make_matrix():
    initial = (0, 0)
    reachable = {initial}
    while True:
        new = reachable | {s2 for s in reachable for s2 in edges(s)}
        if new == reachable:
            break
        reachable = new
    states = sorted(reachable)
    pos = {s: i for i, s in enumerate(states)}
    mat = [[0] * len(states) for _ in states]
    for i, state in enumerate(states):
        for neighbor in edges(state):
            mat[i][pos[neighbor]] += 1
    return states, mat, pos[initial]

def mv(mat, vec):
    return [sum(a * b for a, b in zip(row, vec)) for row in mat]

def vm(vec, mat):
    return [sum(vec[i] * mat[i][j] for i in range(len(vec)))
            for j in range(len(vec))]

def energy_bruteforce(depth):
    vals = [n for n in range(1 << depth) if is_allowed(n)]
    counts = Counter(a+b for a in vals for b in vals)
    return sum(t*t for t in counts.values())

def matrix_mul(left, right):
    n=len(left)
    return [[sum(left[i][k]*right[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]

def characteristic_coeffs(mat):
    n=len(mat)
    b=[[int(i==j) for j in range(n)] for i in range(n)]
    coeff=[1]
    for k in range(1,n+1):
        product=matrix_mul(mat,b)
        tr=sum(product[i][i] for i in range(n))
        assert tr%k==0
        c=-tr//k
        coeff.append(c)
        b=[[product[i][j]+(c if i==j else 0) for j in range(n)]
           for i in range(n)]
    return coeff

def poly_product(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def main():
    checks = 0
    states, mat, start = make_matrix()
    assert len(states) == 12
    checks += 1
    assert all(abs(c) <= 1 for m,c in states)
    checks += 1
    expected=[1]
    for factor in ([0,0,1],[-1,1],[1,1],[1,1],[-2,0,1],[-2,4,1,-6,-2,1]):
        expected=poly_product(expected, factor)
    assert characteristic_coeffs(mat)==list(reversed(expected))
    checks += 1
    term = [int(c == 0) for m,c in states]
    powers = [term]
    for _ in range(5):
        powers.append(mv(mat, powers[-1]))
    # (M^5 - 2 M^4 - 6 M^3 + M^2 + 4M - 2I) t = 0.
    for j in range(len(states)):
        assert sum(P[k]*powers[5-k][j] for k in range(6)) == 0
        checks += 1
    v = [int(i == start) for i in range(len(states))]
    energies=[]
    for r in range(48):
        energies.append(sum(v[j]*term[j] for j in range(len(states))))
        v = vm(v, mat)
    assert energies[:12] == [1, 6, 19, 69, 244, 861, 3053, 10790,
                             38199, 135129, 478172, 1691865]
    checks += 12
    for r in range(5,48):
        assert sum(P[k]*energies[r-k] for k in range(6)) == 0
        checks += 1
    for r in range(0,12):
        assert energy_bruteforce(r) == energies[r]
        checks += 1
    for n in range(0,257):
        assert (comb(3*n,n) % 2 == 1) == is_allowed(n)
        checks += 1
    # Strong connectivity and a self-loop certify primitive nonnegative M.
    for k in range(len(states)):
        seen={k}; frontier={k}
        while frontier:
            frontier={j for i in frontier for j,multiplicity in enumerate(mat[i])
                      if multiplicity and j not in seen}
            seen.update(frontier)
        assert len(seen)==len(states)
        checks+=1
    assert any(mat[j][j] > 0 for j in range(len(states)))
    checks+=1
    # Rational, exact sign enclosure for Perron root > 7/2.
    def poly(x):
        return x**5-2*x**4-6*x**3+x*x+4*x-2
    from fractions import Fraction
    assert poly(Fraction(7,2)) < 0 < poly(Fraction(18,5))
    checks+=1
    print('CHECK_OK', checks, 'assertions; 12 reachable states; E_0..E_11 verified')

if __name__ == '__main__':
    main()
