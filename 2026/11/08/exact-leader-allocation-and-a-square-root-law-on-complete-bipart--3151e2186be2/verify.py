#!/usr/bin/env python3
"""Exact-rational replay for biclique grounded inverse-trace identities."""
from fractions import Fraction as Q
from itertools import combinations

def inverse(A):
    n=len(A)
    B=[[Q(x) for x in row]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        z=next((i for i in range(j,n) if B[i][j]),None)
        assert z is not None
        B[j],B[z]=B[z],B[j]
        c=B[j][j]
        B[j]=[t/c for t in B[j]]
        for i in range(n):
            if i==j:continue
            c=B[i][j]
            if c:B[i]=[t-c*v for t,v in zip(B[i],B[j])]
    return [row[n:] for row in B]

def objective(p,q,a,b):
    x,y=p-a,q-b
    assert 0<=x<=p and 0<=y<=q and a+b>=1
    return Q(x-1,q)+Q(y-1,p)+Q(p+q,p*q-x*y)

def ground_trace(p,q,a,b):
    F=list(range(a,p))+list(range(p+b,p+q))
    n=len(F)
    A=[[0]*n for _ in range(n)]
    for i,u in enumerate(F):
        for j,v in enumerate(F):
            A[i][j]=(q if u<p else p) if i==j else (-int((u<p)!=(v<p)))
    R=inverse(A)
    return sum(R[i][i] for i in range(n))

checks=0
for p in range(2,8):
    for q in range(2,8):
        for a in range(p+1):
            for b in range(q+1):
                if a+b==0 or a+b==p+q:continue
                assert ground_trace(p,q,a,b)==objective(p,q,a,b),(p,q,a,b)
                checks+=1
print('exact_grounded_checks',checks)

# Independent exact optimize all possible leader subsets on small networks.
subset_checks=0
for p in range(2,5):
    for q in range(2,6):
        for k in range(1,p+q):
            best=min(objective(p,q,a,k-a) for a in range(max(0,k-q),min(p,k)+1))
            actual=None
            for S in combinations(range(p+q),k):
                a=sum(v<p for v in S);b=k-a
                val=ground_trace(p,q,a,b)
                if actual is None or val<actual:actual=val
                subset_checks+=1
            assert actual==best,(p,q,k,actual,best)
print('exhaustive_subset_checks',subset_checks)

# Non-nesting and mixed selections: unique optimal part allocations.
def unique_a(p,q,k):
    vals={a:objective(p,q,a,k-a) for a in range(max(0,k-q),min(p,k)+1)}
    m=min(vals.values());v=[a for a in vals if vals[a]==m]
    assert len(v)==1,(p,q,k,v)
    return v[0],m
assert unique_a(2,3,2)==(2,Q(3,2))
assert unique_a(2,3,3)==(0,Q(2,3))
assert unique_a(2,9,4)==(1,Q(41,12))
print('strict_witnesses',3)

# Algebraic asymptotic differences for fixed p,k, including tie cases.
for p in range(2,32):
 for k in range(1,32):
  r=next(a for a in range(1,p+1) if a*(a+1)>=p)
  target={min(k,r)}
  if r<min(k,p) and r*(r+1)==p:target.add(r+1)
  g=lambda a:Q(a,p)+Q(1,a)
  candidates=range(1,min(p,k)+1)
  mn=min(g(a) for a in candidates)
  assert {a for a in candidates if g(a)==mn}==target,(p,k,target)
print('limit_allocation_checks',30*31)
print('VERIFY_OK')
