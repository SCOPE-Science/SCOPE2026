#!/usr/bin/env python3
"""Exact finite checks for the two-scale Fibonacci-partition doubling identity.
No floating point, third-party libraries, or external network access.
"""
from functools import lru_cache

F=[0,1]
for _ in range(33): F.append(F[-1]+F[-2])
L=[2,1]
for _ in range(24): L.append(L[-1]+L[-2])

@lru_cache(None)
def partitions(t,i):
    if t == 0: return 1
    if t < 0 or i < 2: return 0
    if F[i] > t: return partitions(t,i-1)
    return partitions(t,i-1)+partitions(t-F[i],i-1)

def counts_from_word(word,variant):
    inds=[i for i,x in enumerate(word) if x=='1']
    if len(inds)<=1:return 1
    gaps=[inds[k+1]-inds[k]-1 for k in range(len(inds)-2,-1,-1)]
    prev=1; s=gaps[0]
    cur=(s//2+1 if s%2==0 else (s+1)//2 + (variant=='knott'))
    for s in gaps[1:]:
        nxt=((s//2+1) if s%2==0 else (s+3)//2)*cur-(prev if s%2 else 0)
        prev,cur=cur,nxt
    return cur

def phi_pair(power):
    # phi**j = F_j phi + F_(j-1), valid also for negative j.
    def fib_z(j):return F[j] if j>=0 else (-1)**(-j+1)*F[-j]
    return fib_z(power-1),fib_z(power)

def bergman(n):
    # Exact integer-pair greedy algorithm in Z[phi].
    # Candidate exponents are bounded by phi**L <= n < phi**(L+1).
    # Since phi>1, positive pairs can be ordered using rational bounds for sqrt(5).
    def signpair(pair):
        a,b=pair
        if b==0:return (a>0)-(a<0)
        # sign(2a+b+b*sqrt5): compare squared magnitudes when needed
        c=2*a+b
        if c>=0 and b>=0:return 1
        if c<=0 and b<=0:return -1
        d=c*c-5*b*b
        if d==0:return 0
        if b>0:return 1 if d<0 else -1
        return -1 if d<0 else 1
    def sub(u,v):return (u[0]-v[0],u[1]-v[1])
    remainder=(n,0)
    top=0
    while signpair(sub(remainder,phi_pair(top+1)))>=0:top+=1
    digits=[]
    for j in range(top,-120,-1):
        p=phi_pair(j)
        if signpair(sub(remainder,p))>=0:
            digits.append('1');remainder=sub(remainder,p)
        else:digits.append('0')
        if remainder==(0,0):return ''.join(digits)
    raise ArithmeticError((n,remainder))

intervals=[]
for j in range(1,6):
    intervals.append((L[2*j],L[2*j+1],2*j,False))
    intervals.append((L[2*j+1]+1,L[2*j+2]-1,2*j+2,True))
checked=0; strict=0; equal=0
for lo,hi,r,expected_equal in intervals:
    for n in range(lo,min(hi,220)+1):
        if n>220:continue
        w=bergman(n)
        v=counts_from_word(w,'natural')
        k=counts_from_word(w,'knott')
        a=partitions(F[r+2]*n,len(F)-1)
        b=partitions(F[r+4]*n,len(F)-1)
        assert (a,b)==(v,k+v),(n,r,w,a,b,k,v)
        assert (b==2*a)==expected_equal,(n,a,b,expected_equal)
        checked+=1
        equal+=b==2*a
        strict+=b>2*a
for j in range(1,5):
    n=L[2*j+1]
    a=partitions(F[2*j+2]*n,len(F)-1)
    b=partitions(F[2*j+4]*n,len(F)-1)
    assert (a,b)==(1,2*j+2),(j,a,b)
print('VERIFY_OK parameter_integers=',checked,'equality=',equal,'strict=',strict,'endpoint_cases=4')
