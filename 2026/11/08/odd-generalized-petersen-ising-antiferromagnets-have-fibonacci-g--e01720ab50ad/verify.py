#!/usr/bin/env python3
"""Reproduce exact odd generalized-Petersen Ising counts and transfer identities.

Requires Python 3 and SymPy (tested with SymPy 1.13). All arithmetic exact.
Run: python3 verify.py
"""
from itertools import product
from sympy import Matrix, eye, symbols, expand, Poly, factor, fibonacci

STATES = list(product((-1, 1), repeat=3))

def transfer_polynomial():
    x, z, y, t = symbols('x z y t')
    T = Matrix(8, 8, lambda i, j: 0)
    transitions = []
    for i, (a,b,c) in enumerate(STATES):
        for j, (u,v,d) in enumerate(STATES):
            if d != b:
                continue
            f = (3+a*u+c*v+u*v)//2
            T[i,j] = x**f
            transitions.append((i,j,f))
    # The coefficient of y^j in det(wI - T(y^2)/y) controls all n.
    w = symbols('w')
    lam = symbols('lambda')
    char = T.charpoly(lam).as_expr()
    scaled = expand(char.subs({lam:y*w,x:y**2}) / y**8)
    p = Poly(scaled,y)
    d0 = expand(p.nth(0))
    d1 = expand(p.nth(1))
    d2 = expand(p.nth(2))
    assert expand(d0 - (w**8-3*w**4+1)) == 0
    assert expand(d1 - (-2*(w**5+w**3))) == 0
    assert expand(d2 - (-(w**6+6*w**4+w**2))) == 0
    assert p.degree() >= 2
    return transitions

def min_plus_trace(n, trans):
    # Closed walks of length n on the eight-state automaton; every
    # labelled Ising configuration contributes exactly one closed walk.
    best = 10**100
    count = 0
    outgoing = [[] for _ in range(8)]
    for i,j,f in trans:
        outgoing[i].append((j,f))
    for start in range(8):
        dp = {start:(0,1)}
        for _ in range(n):
            nxt = {}
            for i,(value,ways) in dp.items():
                for j,f in outgoing[i]:
                    v = value+f
                    if j not in nxt or v < nxt[j][0]:
                        nxt[j] = (v,ways)
                    elif v == nxt[j][0]:
                        nxt[j] = (v,nxt[j][1]+ways)
            dp = nxt
        if start not in dp:
            continue
        v,ways = dp[start]
        if v<best:
            best,count = v,ways
        elif v==best:
            count+=ways
    return best,count

def direct_enumeration(n):
    # Independent edge-energy computation, with no use of transfer states.
    edges = [(i,(i+1)%n) for i in range(n)]
    edges += [(n+i,n+(i+2)%n) for i in range(n)]
    edges += [(i,n+i) for i in range(n)]
    emin = 3*n+1
    count = 0
    for bits in range(1<<(2*n)):
        f = 0
        for a,b in edges:
            f += 1 - (((bits>>a)^(bits>>b))&1)
        if f<emin:
            emin,count = f,1
        elif f==emin:
            count+=1
    return emin,count

def expected(n):
    assert n>=5 and n%2==1
    half = (n-1)//2 if n%4==1 else (n+1)//2
    return (n+1)//2, 2*n*int(fibonacci(half))

def main():
    trans=transfer_polynomial()
    checked=0
    for n in list(range(5,54,2)) + [61,71,81]:
        a=min_plus_trace(n,trans)
        assert a==expected(n),(n,a,expected(n))
        checked+=1
    brute=0
    for n in [5,7,9]:
        assert direct_enumeration(n)==expected(n)
        brute+=1
    print(f'VERIFY_OK symbolic_determinant=1 exact_transfer_sizes={checked} exhaustive_spin_sizes={brute}')

if __name__ == '__main__':
    main()
