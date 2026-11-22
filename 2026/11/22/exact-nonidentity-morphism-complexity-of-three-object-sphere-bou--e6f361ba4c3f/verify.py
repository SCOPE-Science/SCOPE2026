#!/usr/bin/env python3
"""Exact modular rank checks for three-object composition-table constructions.

For every constructed table the mathematical proof, not this finite test,
shows that the nerve is simply connected and has the target homotopy type.
"""
from math import isqrt
from random import Random


def optimum(s):
    if not isinstance(s, int) or s < 1:
        raise ValueError('s must be a positive integer')
    return min((u + v + u*v - s + 3, u, v)
               for u in range(1, s+1)
               for v in [(s+u-1)//u])


def composition(s, u, v):
    if not (1 <= s <= u*v):
        raise ValueError('invalid inputs')
    c = u*v-s+1
    tab = [[0]*(v+1) for _ in range(u+1)]
    for color, (i, j) in enumerate(((i,j) for i in range(1,u+1)
                                           for j in range(1,v+1)), 1):
        if color < c:
            tab[i][j] = color
    assert set(sum(tab, [])) == set(range(c))
    return tab


def rank_mod(cols, nrows, prime):
    basis = {}
    for src in cols:
        vec = [x % prime for x in src]
        while True:
            p = next((i for i, val in enumerate(vec) if val), None)
            if p is None: break
            if p not in basis:
                inv = pow(vec[p], -1, prime)
                basis[p] = [(v*inv) % prime for v in vec]
                break
            c = vec[p]
            vec = [(v - c*w) % prime for v, w in zip(vec, basis[p])]
    return len(basis)


def check(s, u, v):
    tab = composition(s, u, v)
    a,b,c = u+1,v+1,u*v-s+1
    m=a+b+c
    assert c >= 1
    edges=[]
    for i in range(a): edges.append((-1,1,0))
    for j in range(b): edges.append((0,-1,1))
    for k in range(c): edges.append((-1,0,1))
    twocells=[]
    for i in range(a):
        for j in range(b):
            vec=[0]*m
            vec[i]+=1
            vec[a+j]+=1
            vec[a+b+tab[i][j]]-=1
            twocells.append(tuple(vec))
            assert tuple(sum(vec[z]*edges[z][t] for z in range(m))
                         for t in range(3)) == (0,0,0)
    for p in (2,3,101):
        assert rank_mod(edges,3,p)==2
        assert rank_mod(twocells,m,p)==m-2
    assert len(twocells)-(m-2) == s
    # The anchor row and column prove that f_i,g_j,h_k are all null in pi_1.
    assert all(tab[0][j]==0 for j in range(b))
    assert all(tab[i][0]==0 for i in range(a))
    return dict(s=s,a=a,b=b,c=c,morphisms=m,triangles=a*b)


def run():
    sample=[]
    for s in range(1,151):
        _, u, v=optimum(s)
        sample.append(check(s,u,v))
    rng=Random(1729)
    for _ in range(250):
        u=rng.randint(1,9)
        v=rng.randint(1,9)
        s=rng.randint(1,u*v)
        check(s,u,v)
    # Compare 1-dimensional minimization with an independent rectangular
    # exhaustive search over all allowable u,v for small s.
    for s in range(1,101):
        manual=min((u+v+u*v-s+3, u, v)
                   for u in range(1,s+1) for v in range(1,s+1) if u*v>=s)
        assert optimum(s)==manual
    k=10
    assert optimum(k*k)==(23,10,10)
    assert optimum(7)[0]>optimum(8)[0]
    print('PASS: 150 optimal tables, 250 random nonoptimal tables, 100 exhaustive cost comparisons;')
    print('      1200 modular boundary-rank checks, all chain identities, anchor relations.')
    print('selected:', *(str(sample[s-1]) for s in (1,4,7,8,11,12,100)), sep='\n  ')


if __name__=='__main__':
    run()
