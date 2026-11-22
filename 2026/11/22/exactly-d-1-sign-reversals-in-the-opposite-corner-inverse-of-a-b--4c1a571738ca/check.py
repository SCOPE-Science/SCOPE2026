#!/usr/bin/env python3
"""Exact-arithmetic, finite checks accompanying the opposite-corner mass-inverse theorem.

Run: python3 check.py . Requires only Python's standard library.
These checks do not replace the all-dimension proof in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb

checks=0

def check(pred):
    global checks
    assert pred
    checks += 1

def mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def poly_trim(p):
    p=p[:]
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def divrem(a,b):
    a=poly_trim(a);b=poly_trim(b)
    if b==[0]:raise ZeroDivisionError()
    q=[Q(0)]*max(1,len(a)-len(b)+1)
    while a != [0] and len(a)>=len(b):
        k=len(a)-len(b)
        u=a[-1]/b[-1]
        q[k]=u
        for j in range(len(b)):a[k+j]-=u*b[j]
        a=poly_trim(a)
    return poly_trim(q),a

def sign(q):return (q>0)-(q<0)

def changes(seq):
    seq=[sign(x) for x in seq if x]
    return sum(a!=b for a,b in zip(seq,seq[1:]))

def positive_roots_sturm(p):
    p=poly_trim(p)
    chain=[p,poly_trim([Q(j)*p[j] for j in range(1,len(p))])]
    while chain[-1] != [0]:
        rem=divrem(chain[-2],chain[-1])[1]
        if rem == [0]:break
        chain.append([-x for x in rem])
    return changes([a[0] for a in chain])-changes([a[-1] for a in chain])

def numerator(d):
    factors=[[Q(1), Q(3**k)] for k in range(d+1)]
    N=[Q(0)]*(d+1)
    for k in range(d+1):
        p=[Q(1)]
        for j,g in enumerate(factors):
            if j!=k:p=mul(p,g)
        for j,val in enumerate(p):N[j]+=(-1)**k*comb(d,k)*3**k*val
    return poly_trim(N)

def F(d,t):
    return sum(((-1)**k*comb(d,k)*Q(3**k,1)/(1+3**k*t) for k in range(d+1)),Q(0))

def mat_inverse(M):
    n=len(M)
    A=[row[:]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(M)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if A[i][j])
        A[j],A[pivot]=A[pivot],A[j]
        z=A[j][j]
        A[j]=[v/z for v in A[j]]
        for i in range(n):
            if i!=j:
                z=A[i][j]
                A[i]=[a-z*b for a,b in zip(A[i],A[j])]
    return [row[n:] for row in A]

def C(d,i,j):
    return Q(2**(d-(i^j).bit_count()),3**d)

for d in range(2,10):
    p=numerator(d)
    check(len(p)==d)
    check(p[-1] != 0)
    check(positive_roots_sturm(p)==d-1)
    for t in [Q(1,13),Q(2,3),Q(7,2),Q(10,1)]:
        t2=Q(1,3**d)/t
        check(F(d,t2)==(-1)**(d+1)*3**d*t*t*F(d,t))
        v=sum(p[j]*t**j for j in range(len(p)))
        denom=Q(1)
        for k in range(d+1):denom*=1+3**k*t
        check(F(d,t)==v/denom)
for d in range(2,5):
    n=2**d
    for alpha in [Q(1,10),Q(1,2),Q(3,4),Q(9,10),Q(99,100)]:
        M=[[Q(int(i==j))*(1-alpha)+alpha*C(d,i,j) for j in range(n)] for i in range(n)]
        R=mat_inverse(M)
        expected=F(d,(1-alpha)/alpha)/((2**d)*alpha)
        check(R[0][-1] == expected)
        for i in range(n):
            check(sum(M[i][j]*R[j][i] for j in range(n))==1)
        # this also verifies the row-sum normalization.
        check(all(sum(M[i])==1 for i in range(n)))
check(F(3,Q(1,1))<0)
check(F(3,Q(1,4))>0)
check(F(3,Q(1,100))<0)
print('VERIFY_OK',checks)
