#!/usr/bin/env python3
"""Exact orbit-chain audit for even-row quotient of the four-row rook complex.
Requires Python 3 and SymPy (integer Smith normal form).
"""
from itertools import combinations, permutations
from collections import Counter
from sympy import zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form


def parity(t):
    return 1 if sum(t[i] > t[j] for i in range(len(t)) for j in range(i+1,len(t))) % 2 == 0 else -1


def orbit_tables(n):
    even=[p for p in permutations(range(4)) if parity(p)==1]
    def canon(rows):return min(tuple(p[r] for r in rows) for p in even)
    fs=[]
    for k in range(1,5):
        fs.append(sorted({(c,canon(r)) for c in combinations(range(n),k) for r in permutations(range(4),k)}))
    ds=[]
    for k in range(1,4):
        idx={f:i for i,f in enumerate(fs[k-1])}
        mat=zeros(len(fs[k-1]),len(fs[k]))
        for col,(c,r) in enumerate(fs[k]):
            for j in range(k+1):
                row=idx[(c[:j]+c[j+1:],canon(r[:j]+r[j+1:]))]
                mat[row,col] += (-1)**j
        ds.append(mat)
    return fs,ds


def parity_tables(n):
    # A second, representation-free construction directly from alternating parity.
    verts=list(combinations(range(n),1))
    edges=list(combinations(range(n),2))
    tris=[(a,s) for a in combinations(range(n),3) for s in (1,-1)]
    tets=[(a,s) for a in combinations(range(n),4) for s in (1,-1)]
    V={a:i for i,a in enumerate(verts)}
    E={a:i for i,a in enumerate(edges)}
    T={a:i for i,a in enumerate(tris)}
    A=zeros(len(verts),len(edges)); B=zeros(len(edges),len(tris)); C=zeros(len(tris),len(tets))
    for i,e in enumerate(edges):
        for j in range(2):A[V[e[:j]+e[j+1:]],i]+=(-1)**j
    for i,(t,s) in enumerate(tris):
        for j in range(3):B[E[t[:j]+t[j+1:]],i]+=(-1)**j
    for i,(t,s) in enumerate(tets):
        for j in range(4):
            C[T[(t[:j]+t[j+1:],s*((-1)**(3-j)))],i]+=(-1)**j
    return [A,B,C]


def profile(B):
    D=smith_normal_form(B,domain=ZZ)
    f=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
    return len(f), dict(sorted(Counter(f).items()))


def main():
    expect={4:((4,6,8,2),((3,{1:3}),(3,{1:3}),(2,{1:2}))),
            5:((5,10,20,10),((4,{1:4}),(6,{1:6}),(9,{1:9}))),
            6:((6,15,40,30),((5,{1:5}),(10,{1:10}),(25,{1:24,3:1})))}
    for n in (4,5,6):
        faces,oracle=orbit_tables(n)
        matrices=parity_tables(n)
        assert tuple(map(len,faces))==expect[n][0]
        assert all(a*b==zeros(a.rows,b.cols) for a,b in zip(matrices,matrices[1:]))
        assert all(a*b==zeros(a.rows,b.cols) for a,b in zip(oracle,oracle[1:]))
        summary=tuple(profile(a) for a in matrices)
        assert summary==expect[n][1],(n,summary)
        assert summary==tuple(profile(a) for a in oracle)
        print(f'n={n} cells={expect[n][0]} exact_SNFs={summary} crosscheck=PASS')
    print('ALL EXACT CHECKS PASSED')
if __name__=='__main__':main()
