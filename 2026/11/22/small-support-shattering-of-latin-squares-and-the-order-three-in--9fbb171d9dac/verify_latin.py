#!/usr/bin/env python3
"""Rebuild the Latin-square membership traces and the F_2 chain complex."""
from itertools import permutations, product, combinations
from collections import Counter

def latin_squares(n):
    perms = list(permutations(range(n)))
    return [rows for rows in product(perms, repeat=n)
            if all(len({rows[r][c] for r in range(n)}) == n
                   for c in range(n))]

def supports(n, maxk):
    squares=latin_squares(n)
    points=list(product(range(n), repeat=3))
    concepts=[]
    for sq in squares:
        concepts.append(sum(1<<i for i,(r,c,s) in enumerate(points)
                            if sq[r][c]==s))
    faces={}
    for k in range(maxk+1):
        faces[k]=[]
        for comb in combinations(range(len(points)), k):
            bits=[1<<j for j in comb]
            traces={sum((1<<i) for i,b in enumerate(bits) if c&b)
                    for c in concepts}
            if len(traces)==(1<<k):faces[k].append(comb)
    return squares, points, faces

def f2_rank(columns):
    pivots={}
    for col in columns:
        while col:
            pivot=col.bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=col
                break
            col ^= pivots[pivot]
    return len(pivots)

def check():
    sq,points,F=supports(3,4)
    assert len(sq)==12
    assert [len(F[k]) for k in range(5)]==[1,27,270,216,0]
    T=set(F[3]); E=set(F[2]); VE={e for t in T for e in combinations(t,2)}
    assert len(VE)==162
    assert len(E-VE)==108
    for (a,b) in E:
        p,q=points[a],points[b]
        assert sum(x==y for x,y in zip(p,q))<=1
    for a,b,c in T:
        pp=[points[x] for x in (a,b,c)]
        equaltypes=[]
        for i,j in combinations(range(3),2):
            idx=[k for k in range(3) if pp[i][k]==pp[j][k]]
            assert len(idx)==1
            equaltypes.append(idx[0])
        assert sorted(equaltypes)==[0,1,2]
    for t in combinations(range(27),3):
        pp=[points[x] for x in t]
        expected=(len({next((j for j in range(3) if pp[a][j]==pp[b][j]),-1)
                      for a,b in combinations(range(3),2)})==3
                  and all(sum(pp[a][j]==pp[b][j] for j in range(3))==1
                          for a,b in combinations(range(3),2)))
        assert (t in T)==expected
    eindex={e:i for i,e in enumerate(F[2])}
    boundary=[sum(1<<eindex[e] for e in combinations(t,2)) for t in F[3]]
    rank=f2_rank(boundary)
    assert rank==133
    beta1=len(E)-(len(F[1])-1)-rank
    beta2=len(T)-rank
    assert (beta1,beta2)==(111,83)
    # Independent n=4 sanity check for the degree-three stabilization.
    sq4=latin_squares(4)
    assert len(sq4)==576
    pts4=list(product(range(4), repeat=3))
    cols=[sum(1<<i for i,L in enumerate(sq4) if L[r][c]==s)
          for (r,c,s) in pts4]
    allbits=(1<<576)-1
    num_shattered=0; num_compatible=0
    for ids in combinations(range(64),3):
        p=[pts4[i] for i in ids]
        compatible=all(sum(a==b for a,b in zip(p[i],p[j]))<=1
                       for i,j in combinations(range(3),2))
        if not compatible:continue
        num_compatible+=1
        b=[cols[i] for i in ids]
        for pattern in range(8):
            possible=allbits
            for t in range(3):
                possible &= b[t] if (pattern>>t)&1 else allbits ^ b[t]
            if not possible:break
        else:num_shattered+=1
    assert (num_compatible,num_shattered)==(25920,25920)
    print('LATIN_TRACES_PASS n3=12 f=[1,27,270,216] facets=[108,216]')
    print('LATIN_MOD2_PASS boundary_rank=133 betti1=111 betti2=83')
    print('LATIN_ORDER4_TRIPLE_PASS compatible=shattered=25920')

if __name__=='__main__':check()
