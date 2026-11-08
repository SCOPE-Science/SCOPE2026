#!/usr/bin/env python3
"""Exhaustive independent finite-domain checks for finite-field unit-circle shattering.
Uses bitsets of centers, rather than the geometric proof's antipodal counting.
Only the listed sample fields are enumerated; the all-odd-q theorem is proved separately.
"""
from itertools import combinations
from math import comb

# For q=9 use F_3[u]/(u^2+1); integers a+3b represent a+bu.
# -1 is not a square in F_3, so the modulus is irreducible.
def add(a,b,q):
    if q==9:
        return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
    return (a+b)%q

def neg(a,q):
    if q==9:return (-(a%3))%3 + 3*((-(a//3))%3)
    return -a%q

def sub(a,b,q):return add(a,neg(b,q),q)

def mul(a,b,q):
    if q==9:
        x,y=a%3,a//3; z,w=b%3,b//3
        return (x*z-y*w)%3+3*((x*w+y*z)%3)
    return a*b%q

def count(q,t):
    pts=[(x,y) for x in range(q) for y in range(q)]
    N=q*q; full=(1<<N)-1
    squares=[mul(x,x,q) for x in range(q)]
    membership=[]
    for ax,ay in pts:
        mask=0
        for ci,(cx,cy) in enumerate(pts):
            dx=sub(ax,cx,q);dy=sub(ay,cy,q)
            if add(squares[dx],squares[dy],q)==t:mask|=1<<ci
        membership.append(mask)
    k=(membership[0]).bit_count()
    chi=-1 if q%4==3 else 1
    assert k==q-chi,(q,t,k)
    count1=sum(bool(m) and bool(full&~m) for m in membership)
    count2=count3=0
    for a,b in combinations(range(N),2):
        A=membership[a];B=membership[b]
        if not(A&B):continue
        if (A&~B) and (B&~A) and (full&~(A|B)):count2+=1
    for a,b,c in combinations(range(N),3):
        A=membership[a];B=membership[b];C=membership[c]
        if not(A&B&C):continue
        if not(A&B&~C):continue
        if not(A&~B&C):continue
        if not(~A&B&C):continue
        if not(A&~B&~C):continue
        if not(~A&B&~C):continue
        if not(~A&~B&C):continue
        if not(full&~(A|B|C)):continue
        count3+=1
    predicted=[1,N,N*k*k//4,N*k*(k-2)*(k-4)//6]
    actual=[1,count1,count2,count3]
    assert actual==predicted,(q,t,actual,predicted)
    print('FINITE_FIELD_CIRCLE_PASS',q,'radius',t,'cardinality',k,'faces',','.join(map(str,actual)),flush=True)
    return actual

if __name__=='__main__':
    for q in [3,5,7,9,11,13]:
        for t in (list(range(1,q)) if q<=9 else [1]):count(q,t)
    print('FINITE_FIELD_UNIT_CIRCLE_SHATTER_PASS',flush=True)
