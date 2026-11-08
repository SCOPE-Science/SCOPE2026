#!/usr/bin/env python3
"""Exact checks for extreme-key search depth dependence in a uniformly built BST."""
from itertools import permutations
from collections import Counter
from fractions import Fraction as F
from math import factorial, pi

def qdist(n):
    d={0:F(1)}
    for j in range(2,n+1):
        w=F(1,j)
        z={}
        for k,v in d.items():
            z[k]=z.get(k,F(0))+v*(1-w)
            z[k+1]=z.get(k+1,F(0))+v*w
        d=z
    return d

def conditional(l):
    return {0:F(1)} if l==0 else {a+1:v for a,v in qdist(l).items()}

def joint_by_split(n):
    d={}
    for l in range(n):
        for a,pa in conditional(l).items():
            for b,pb in conditional(n-1-l).items():
                d[a,b]=d.get((a,b),F(0))+pa*pb/n
    return d

def brute(n):
    cnt=Counter()
    for order in permutations(range(1,n+1)):
        left=[0]*(n+1);right=[0]*(n+1)
        root=order[0]
        for x in order[1:]:
            a=root
            while True:
                if x<a:
                    if not left[a]: left[a]=x; break
                    a=left[a]
                else:
                    if not right[a]:right[a]=x; break
                    a=right[a]
        depth=[]
        for x in (1,n):
            a=root;dep=0
            while a!=x:
                a=left[a] if x<a else right[a]
                dep+=1
            depth.append(dep)
        cnt[tuple(depth)]+=1
    return {k:F(v,factorial(n)) for k,v in cnt.items()}

def moments(jd):
    ea=sum((F(a)*p for (a,b),p in jd.items()),F(0))
    eb=sum((F(b)*p for (a,b),p in jd.items()),F(0))
    eab=sum((F(a*b)*p for (a,b),p in jd.items()),F(0))
    return ea,eb,eab-ea*eb

checks=0
for n in range(2,9):
    q=joint_by_split(n)
    assert q==brute(n),(n,'enumeration mismatch');checks+=1
    assert sum(q.values())==1;checks+=1
    H=sum((F(1,j) for j in range(1,n+1)),F(0))
    H2=sum((F(1,j*j) for j in range(1,n+1)),F(0))
    aa,bb,cc=moments(q)
    assert (aa,bb,cc)==(H-1,H-1,1-H2);checks+=1
    v=sum((F(a*a)*p for (a,b),p in q.items()),F(0))-aa*aa
    assert v==H-H2;checks+=1
    for a in range(n-1):
        for b in range(n-1):
            pa=sum((p for (x,y),p in q.items() if x>a),F(0))
            pb=sum((p for (x,y),p in q.items() if y>b),F(0))
            pab=sum((p for (x,y),p in q.items() if x>a and y>b),F(0))
            assert pab<pa*pb,(n,a,b,'NQD');checks+=1

# Validate the harmonic convolution by exact arithmetic, independently of the joint law.
H=F(0);H2=F(0);hs=[F(0)]; h2=[F(0)]
for n in range(1,301):
    H+=F(1,n);H2+=F(1,n*n);hs.append(H);h2.append(H2)
    lhs=sum((hs[l]*hs[n-1-l] for l in range(n)),F(0))
    assert lhs==n*((H-1)**2+1-H2);checks+=1
for n in range(2,301):
    jd=joint_by_split(n) if n<=30 else None
    # Independent marginal moments and asymptotic correlation trend
    assert 1-h2[n]<0 and hs[n]-h2[n]>0;checks+=1
    if jd is not None:
        assert moments(jd)==(hs[n]-1,hs[n]-1,1-h2[n]);checks+=1
print(f'PASS: {checks} exact assertions; enumerated all insertions through n=8; exact recurrence through n=30; harmonic identities through n=300.')
print('n=8 covariance:',1-h2[8], 'corr:', float((1-h2[8])/(hs[8]-h2[8])))
