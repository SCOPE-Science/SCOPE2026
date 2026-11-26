#!/usr/bin/env python3
"""Standalone finite-field checks of the prescribed-square fiber theorem for UT_5.

Runs complete 5-by-5 matrix-square enumerations for GF(2) and GF(4), and
independent restricted-variable counts at selected targets in GF(8).
Uses only Python's standard library; no papers or external data are required.
"""
from collections import Counter
from itertools import product
import random

POLYS={2:0b11,4:0b111,8:0b1011}

def mult_table(q):
    assert q in POLYS and q & (q-1)==0
    top=q.bit_length()-1
    poly=POLYS[q]
    result=[]
    for a in range(q):
        row=[]
        for b in range(q):
            v=0;x=a;y=b
            while y:
                if y&1:v^=x
                y>>=1;x<<=1
                if x&q:x^=poly
            row.append(v)
        result.append(row)
    return result

def predicted(q,z,times):
    A,B,C,D,E,F=z
    p=times
    if B:
        if A or C:return q**3*(q-1)
        return q**4*(q-1) if p[B][F]==(p[D][E]) else 0
    if A and C:return 0
    if A or C:return q**4*(q-1)
    if D and E:return q**4*(q-1)
    if D or E:return q**4*(q*q-1)
    if F:return 3*q**5*(q-1)
    return q**5*(5*q-4)

def matrix_square(q,variables,p):
    # Variables correspond to strict upper entries 12,23,34,45,13,24,35,14,25.
    a,b,c,d,e,f,g,h,i=variables
    N=[[0]*5 for _ in range(5)]
    for (r,s),v in zip([(0,1),(1,2),(2,3),(3,4),
                        (0,2),(1,3),(2,4),(0,3),(1,4)],variables):
        N[r][s]=v
    out=[]
    for r,s in [(0,2),(1,3),(2,4),(0,3),(1,4),(0,4)]:
        acc=0
        for k in range(r+1,s):acc^=p[N[r][k]][N[k][s]]
        out.append(acc)
    return tuple(out)

def exhaustive(q):
    p=mult_table(q); actual=Counter()
    for x in product(range(q),repeat=9):
        # The tenth coordinate (1,5) of the strict upper matrix is free.
        actual[matrix_square(q,x,p)]+=q
    expected=Counter()
    for z in product(range(q),repeat=6):
        v=predicted(q,z,p)
        if v:expected[z]=v
    assert actual==expected,(q,[(z,actual[z],expected[z])
                                for z in set(actual)|set(expected)
                                if actual[z]!=expected[z]][:6])
    assert sum(actual.values())==q**10
    image=q**6-q**5+q**4+q**3-q**2
    assert len(actual)==image,(q,len(actual),image)
    expected_hist={
       q**3*(q-1):q**3*(q-1)*(q*q-1),
       q**4*(q-1):q*(q-1)*(2*q*q+2*q-1),
       q**4*(q*q-1):2*q*(q-1),
       3*q**5*(q-1):q-1,
       q**5*(5*q-4):1}
    assert Counter(actual.values())==Counter(expected_hist),Counter(actual.values())
    print('GF',q,'EXHAUSTIVE_OK','group_size',q**10,'image',image,
          'histogram',sorted(Counter(actual.values()).items()))

def pointwise_seven_coordinates(q,target):
    # Count 7 lower coordinates directly and solve only for the final two
    # through their explicitly linear appearance, retaining free top corner.
    p=mult_table(q)
    A,B,C,D,E,F=target
    total=0
    for a,b,c,d in product(range(q),repeat=4):
        if p[a][b]!=A or p[b][c]!=B or p[c][d]!=C:continue
        for e,f,g in product(range(q),repeat=3):
            if p[a][f]^p[e][c]!=D:continue
            if p[b][g]^p[f][d]!=E:continue
            if a or d:
                # Solve a*i + d*h = F + e*g, one equation in 2 unknowns.
                total+=q*q
            elif p[e][g]==F:
                total+=q**3
    return total

def sample_q8():
    q=8;p=mult_table(q)
    targets=[(0,0,0,0,0,0),(0,0,0,0,0,1),
             (0,0,0,1,0,3),(0,0,0,1,1,0),
             (1,1,0,0,1,2),(0,1,0,0,0,0),
             (0,1,0,2,3,p[2][3]),(0,1,0,2,3,p[2][3]^1),
             (1,0,1,0,0,0)]
    for z in targets:
        a=pointwise_seven_coordinates(q,z)
        b=predicted(q,z,p)
        assert a==b,(z,a,b)
    rng=random.Random(20261016)
    for _ in range(2000):
        x=tuple(rng.randrange(q) for _ in range(9))
        z=matrix_square(q,x,p)
        assert predicted(q,z,p)>0
    print('GF 8 POINTWISE_OK',len(targets),'targets + 2000 direct-square samples')

if __name__=='__main__':
    exhaustive(2)
    exhaustive(4)
    sample_q8()
    print('ALL_EXACT_CHECKS_PASSED')
