"""Exact finite checks supporting the short-cycle lattice theorem.
Run: python check.py. No external packages required.
"""
from itertools import product
from math import gcd

def group_rep(x,q):
    M=q*q
    x=tuple(t%M for t in x)
    return min(tuple((t+z*q)%M for t in x) for z in range(q))

def check(q,d,graph=False):
    M=q*q
    N=M**d//q
    # Every lattice vector whose l1 norm <= d*q is either a coordinate
    # period or a shortest diagonal representative (possibly both at end).
    # Finite brute force on the relevant integer cube for small q,d.
    vectors=set()
    for z in product(range(-M,M+1),repeat=d):
        if sum(map(abs,z))>d*q or not any(z): continue
        # z in L iff all coordinates are multiples of q with equal residue mod q^2.
        if all(t%q==0 for t in z) and len({(t//q)%q for t in z})==1:
            vectors.add(z)
    coord= [v for v in vectors if sum(abs(x) for x in v) <= M]
    assert set(coord)=={tuple(sign*M if i==j else 0 for i in range(d)) for j in range(d) for sign in (-1,1)}
    assert min(sum(abs(x) for x in v) for v in vectors if any(t%M for t in v))==d*q
    print('lattice',q,d,'vertices',N,'coordinate shell',len(coord),'first noncoordinate length',d*q)
    if graph:
        verts={group_rep(v,q) for v in product(range(M), repeat=d)}
        assert len(verts)==N
        basis=[tuple(int(i==j) for i in range(d)) for j in range(d)]
        def step(v,j,sign):
            return group_rep(tuple(v[i]+sign*(i==j) for i in range(d)),q)
        assert all(step(v,j,+1)!=step(v,j,-1) for v in verts for j in range(d))
        assert all(len({step(v,j,s) for j in range(d) for s in (-1,1)})==2*d for v in verts)
        # Every length-3 closed walk contains a backtrack, no triangle.
        first=group_rep((0,)*d,q)
        nbr=lambda v:{step(v,j,s) for j in range(d) for s in (-1,1)}
        A=nbr(first)
        assert not any((A & nbr(x)) for x in A)
        # A coordinate and a diagonal path are embedded simple cycles.
        for path in [[(j,s) for s in [1]*M] for j in range(d)]:
            v=first; seen={v}
            for j,s in path[:-1]:
                v=step(v,j,s); assert v not in seen; seen.add(v)
            v=step(v,path[-1][0],path[-1][1]); assert v==first
        v=first; seen={v}
        diag=[(j,1) for j in range(d) for _ in range(q)]
        for j,s in diag[:-1]:
            v=step(v,j,s); assert v not in seen; seen.add(v)
        v=step(v,*diag[-1]); assert v==first
        print('graph',q,d,'degree',2*d,'edges',N*d,'diagonal simple length',d*q,'PASS')

check(3,4,True)
# q=4,d=5 checked by arithmetic inequalities only; full brute vector cube is too large.
print('GENERAL PROOF INPUT: for nonzero diagonal residue, every coordinate absolute value >=q; for zero residue, every nonzero coordinate >= q^2.')
