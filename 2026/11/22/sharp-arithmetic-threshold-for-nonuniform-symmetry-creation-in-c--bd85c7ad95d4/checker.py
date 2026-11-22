#!/usr/bin/env python3
"""Exact short-target-period rigidity and symmetry-onset witnesses for binary majority rule."""
from itertools import product
from math import gcd

def majority(a,b,c):return int(a+b+c >= 2)
STATES=list(product((0,1),repeat=2))

def transition(bit):
    return [[int(u[1] == v[0] and majority(u[0],u[1],v[1]) == bit) for v in STATES] for u in STATES]

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

def matrix(word):
    P=[[int(i==j) for j in range(4)] for i in range(4)]
    for y in word:P=mul(P,transition(y))
    return P

def pure_loops(P):
    # in cyclic support, only single loops of multiplicity 1
    R=[[int(P[i][j]>0) for j in range(4)] for i in range(4)]
    for k in range(4):
        for i in range(4):
            for j in range(4):R[i][j] |= R[i][k] and R[k][j]
    for i in range(4):
        if P[i][i]>1:return False
        for j in range(4):
            if i != j and R[i][j] and R[j][i]:return False
    return True

def next_bits(x):
 n=len(x)
 return tuple(majority(x[(i-1)%n],x[i],x[(i+1)%n]) for i in range(n))

def fundamental_period(x):
 n=len(x)
 return min(d for d in range(1,n+1) if n%d==0 and all(x[i]==x[(i+d)%n] for i in range(n)))

if __name__=='__main__':
    print('period; nonconstant output words; outputs admitting cyclic preimages; maximum diagonal trace; failures of loop rigidity')
    for d in range(2,6):
        nwords=npossible=maxtrace=fail=0
        for y in product((0,1),repeat=d):
            if len(set(y))<2:continue
            nwords+=1
            P=matrix(y)
            diag=sum(P[i][i] for i in range(4))
            if diag>0:npossible+=1
            maxtrace=max(maxtrace,diag)
            if not pure_loops(P):
                fail+=1;print('counterexample',d,y,P)
        print(d,nwords,npossible,maxtrace,fail,sep='; ')
        assert not fail
    # Exact witness: repeat y=(000)(111...1) on m blocks and flip one 01 interface to 10
    for d in range(6,31):
      for m in range(2,7):
        n=d*m
        y=(0,0,0)+tuple(1 for _ in range(d-3))
        Y=y*m
        x=list(Y)
        x[2],x[3]=1,0
        x=tuple(x)
        assert next_bits(x)==Y,(d,m,x,Y,next_bits(x))
        assert fundamental_period(Y)==d
        assert fundamental_period(x)==n
    print('ALL WITNESSES PASS for 6<=d<=30, 2<=m<=6')
    # Exhaustive independent ring enumeration 3..16
    for n in range(3,17):
      possible=any(6<=d<=n//2 and n%d==0 for d in range(1,n))
      found=False
      for bits in product((0,1),repeat=n):
        if fundamental_period(bits)!=n:continue
        nxt=next_bits(bits)
        if len(set(nxt))>1 and fundamental_period(nxt)<n:
            found=True;break
      assert possible==found,(n,possible,found)
    print('EXHAUSTIVE n=3..16 confirms sharp arithmetic criterion')
