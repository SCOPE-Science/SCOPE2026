#!/usr/bin/env python3
"""Exact adjoint-square checks for the graph Lie algebras of stars.

Run with Python 3.9+; uses only the standard library. In addition to prime
fields the program implements F4 = F2[z]/(z^2+z+1) for an extension-field test.
"""
from itertools import product, combinations
from collections import Counter
from fractions import Fraction
from math import comb

class Field:
    def __init__(self, q):
        self.q = q
        assert q in (2, 3, 4, 5)
    def add(self, x, y):
        return x ^ y if self.q == 4 else (x+y) % self.q
    def neg(self, x):
        return x if self.q == 4 else (-x) % self.q
    def mul(self, x, y):
        if self.q != 4:
            return (x*y) % self.q
        z = 0
        for i in range(2):
            for j in range(2):
                if (x >> i) & 1 and (y >> j) & 1:
                    z ^= 1 << (i+j)
        if z & 8: z ^= 14  # z^3=z^2+z -> x^3=x+1
        if z & 4: z ^= 7   # x^2=x+1
        return z
    def inv(self, x):
        assert x != 0
        return next(y for y in range(1,self.q) if self.mul(x,y) == 1)

def lie_tensor(m, field):
    pairs = list(combinations(range(m), 2))
    n = 1 + 2*m + len(pairs)
    C = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    def insert(i,j,k):
        C[i][j][k]=1
        C[j][i][k]=field.neg(1)
    for i in range(m):
        insert(0, 1+i, 1+m+i)
    for h, (i,j) in enumerate(pairs):
        k=1+2*m+h
        insert(1+i, 1+m+j,k)
        insert(1+j, 1+m+i,k)
    return C

def adjoint(C,x,F):
    n=len(C)
    A=[[0]*n for _ in range(n)]
    for i,coef in enumerate(x):
        if coef == 0: continue
        for j in range(n):
            for k,z in enumerate(C[i][j]):
                if z: A[k][j]=F.add(A[k][j],F.mul(coef,z))
    return A

def matmul(A,B,F):
    n=len(A); out=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):
                    if B[k][j]:
                        out[i][j]=F.add(out[i][j],F.mul(A[i][k],B[k][j]))
    return out

def rank(M,F):
    A=[row[:] for row in M]
    h=len(A);w=len(A[0]);r=0
    for c in range(w):
        pivot=next((k for k in range(r,h) if A[k][c]),None)
        if pivot is None:continue
        A[pivot],A[r]=A[r],A[pivot]
        u=F.inv(A[r][c]); A[r]=[F.mul(u,z) for z in A[r]]
        for k in range(r+1,h):
            if A[k][c]:
                v=A[k][c]
                A[k]=[F.add(A[k][j],F.neg(F.mul(v,A[r][j]))) for j in range(w)]
        r+=1
        if r==h:break
    return r

def predicted(m,q,t,u):
    s=sum(a!=0 for a in u)
    if t:
        return 0 if s==0 else (m-1 if q%2==0 or s<=2 else m)
    return int(q%2 and s>=2)

def count_formula(m,q):
    A=m*(q-1);B=comb(m,2)*(q-1)**2;C=q**m-1-A-B
    if q%2==0:
        ranks=Counter({0:q**m+q-1, m-1:(q-1)*(q**m-1)})
        return ranks
    ranks=Counter()
    ranks[0]+=1+A+(q-1)
    ranks[1]+=q**m-1-A
    ranks[m-1]+=(q-1)*(A+B)
    ranks[m]+=(q-1)*C
    return ranks

def verify_case(q,m):
    F=Field(q);C=lie_tensor(m,F);n=len(C)
    histogram=Counter()
    for tup in product(range(q),repeat=m+1):
        x=list(tup)+[0]*(n-m-1)
        A=adjoint(C,x,F); A2=matmul(A,A,F)
        actual=rank(A2,F)
        asserted=predicted(m,q,tup[0],tup[1:])
        assert actual==asserted, (m,q,tup,actual,asserted)
        histogram[actual]+=1
    wanted=count_formula(m,q)
    assert histogram == wanted,(m,q,histogram,wanted)
    probability=sum((Fraction(c,q**r) for r,c in histogram.items()),Fraction(0,1))/q**(m+1)
    # The even- and odd-characteristic predictions are checked without floats.
    Q=q**m
    A=m*(q-1);B=comb(m,2)*(q-1)**2;D=Q-1-A-B
    if q%2==0:
        e=(Fraction(Q)+ (q-1)*(1+Fraction(Q-1,q**(m-1)))) / q**(m+1)
    else:
        e=(Fraction(1+A)+Fraction(Q-1-A,q)
           +(q-1)*(1+Fraction(A+B,q**(m-1))+Fraction(D,q**m)))/q**(m+1)
    assert e==probability
    print(f'CASE q={q} m={m} dimension={n} ranks={sorted(histogram.items())} '
          f'engel_probability={probability}')
    return q**(m+1)

def bracket(C,x,y,F):
    n=len(C)
    out=[0]*n
    for i,xi in enumerate(x):
        if not xi:continue
        for j,yj in enumerate(y):
            if not yj:continue
            scalar=F.mul(xi,yj)
            for k,c in enumerate(C[i][j]):
                if c:out[k]=F.add(out[k],F.mul(scalar,c))
    return out

def verify_direct_pairs(q):
    m=2
    F=Field(q); C=lie_tensor(m,F)
    vectors=list(product(range(q),repeat=len(C)))
    good=0
    for x in vectors:
        for y in vectors:
            z=bracket(C,x,y,F)
            good+=int(not any(bracket(C,x,z,F)))
    expected=Fraction(13,16) if q==2 else Fraction(41,81)
    assert Fraction(good,len(vectors)**2)==expected
    print(f'DIRECT q={q} m=2 satisfying_pairs={good} total_pairs={len(vectors)**2}')
    return len(vectors)**2

if __name__=='__main__':
    cases=[(2,2),(3,2),(5,2),(4,2),(2,3),(3,3),(4,3),
           (2,4),(3,4),(5,3)]
    total=sum(verify_case(q,m) for q,m in cases)
    pairs=sum(verify_direct_pairs(q) for q in (2,3))
    print(f'VERIFY_OK cases={len(cases)} adjoint_square_profiles={total} extension_field_cases=2 direct_pair_checks={pairs}')
