#!/usr/bin/env python3
"""Finite cross-checks for cyclic independent-doublet digraphs. Stdlib only.

A coloring of a digraph is proper when no color induces a directed cycle.
This checker forms the arc set explicitly and detects cycles by topological sorting;
its tests are finite and are not a replacement for an all-order proof.
"""
from itertools import product
from math import comb

def predicted(r, q):
    return q**(2*r) - q * (2*q-1)**r + (q*(q-1)//2)*2**r

def edges(r):
    return [(2*i+a, 2*((i+1)%r)+b)
            for i in range(r) for a in range(2) for b in range(2)]

def acyclic_coloring(c, es, q):
    for col in range(q):
        vs = [v for v in range(len(c)) if c[v] == col]
        indeg = {v:0 for v in vs}
        out = {v:[] for v in vs}
        for u,v in es:
            if u in indeg and v in indeg:
                indeg[v] += 1
                out[u].append(v)
        todo = [v for v in vs if indeg[v] == 0]
        seen = 0
        while todo:
            u = todo.pop()
            seen += 1
            for v in out[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    todo.append(v)
        if seen != len(vs):
            return False
    return True

def poly_desc(r):
    # coefficients in ascending degree
    a = [0]*(2*r+1)
    a[2*r] += 1
    for j in range(r+1):
        a[j+1] -= comb(r,j)*2**j*(-1)**(r-j)
    a[2] += 2**(r-1)
    a[1] -= 2**(r-1)
    return a

def check_symbolic(r):
    p = poly_desc(r)
    assert sum(p) == 0
    assert p[0] == 0
    assert p[1] != 0
    assert sum(i*v for i,v in enumerate(p)) == 2**(r-1)-1
    # y=x-1; coefficient of y^j for F_r(1+y) for 1<=j<=2r-1
    b = []
    for j in range(2*r):
        v = comb(2*r-1,j)
        if j <= r: v -= 2**j*comb(r,j)
        if j==1: v += 2**(r-1)
        b.append(v)
    assert b[0] == 0
    assert b[1] == 2**(r-1)-1
    assert b[2] == -(r-1)
    assert b[3] == r-1
    assert all(v>=0 for v in b[4:])
    # For odd r, Descartes on t^(2r-1)-(2t+1)^r+2^(r-1)(t+1): exactly 2 variations.
    if r%2:
        f = [0]*(2*r)
        f[2*r-1] += 1
        for j in range(r+1): f[j] -= comb(r,j)*2**j
        f[0] += 2**(r-1)
        f[1] += 2**(r-1)
        signs = [1 if v>0 else -1 for v in reversed(f) if v]
        assert sum(a!=b for a,b in zip(signs,signs[1:])) == 2
        assert f[0] > 0
        # exact f(1/2) negative after multiplying by 2^(2r-1)
        assert 1 - 2**(3*r-1) + 3*2**(3*r-3) < 0

if __name__ == '__main__':
    c=0
    for r in range(3,7):
        es = edges(r)
        for q in range(1,4 if r<=5 else 3):
            actual = sum(acyclic_coloring(a, es, q) for a in product(range(q),repeat=2*r))
            assert actual == predicted(r,q), (r,q,actual,predicted(r,q))
            print('EXPLICIT_DIGRAPH',r,q,actual,'PASS')
            c+=1
    for r in (3,4):
        q=4; es=edges(r)
        actual=sum(acyclic_coloring(a,es,q) for a in product(range(q),repeat=2*r))
        assert actual==predicted(r,q)
        print('EXPLICIT_DIGRAPH',r,q,actual,'PASS')
        c+=1
    for r in range(3,81):check_symbolic(r)
    print('SYMBOLIC_COEFFICIENT_AND_DESCARTES_CHECKS r=3..80 PASS')
    print('VERIFY_OK cases=',c)
