#!/usr/bin/env python3
"""Exact checks for adjacent swaps constrained by unequal neighbors."""
from itertools import product
from collections import Counter
from math import comb

def poly_model(q,n):
    assert q>=3 and n>=3
    a=q-2
    L=n-2
    C=Counter()
    for Y in product((0,1),repeat=L):
        s=Y[0]+Y[-1]+sum(Y[i]*Y[i+1] for i in range(L-1))
        C[s]+=a**sum(Y)
    return {k:q*(q-1)*v for k,v in C.items()}

def brute(q,n):
    H=Counter()
    for x in product(range(q),repeat=n):
        if any(x[i]==x[i+1] for i in range(n-1)):continue
        ys={x}
        for i in range(n-1):
            y=list(x);y[i],y[i+1]=y[i+1],y[i]
            if all(y[j]!=y[j+1] for j in range(n-1)):
                ys.add(tuple(y))
        H[len(ys)-1]+=1
    return dict(H)

def transfer(q,n):
    a=q-2
    v=[1,a] # initial 0/1 with no left boundary yet
    L=n-2
    # t polynomials; initial y=1 has t to mark start
    p0={0:1};p1={1:a}
    for _ in range(L-1):
        next0=Counter(p0)+Counter(p1)
        next1=Counter({e:a*c for e,c in p0.items()})+Counter({e+1:a*c for e,c in p1.items()})
        p0,p1=next0,next1
    H=Counter(p0)+Counter({e+1:c for e,c in p1.items()})
    return {s:q*(q-1)*v for s,v in H.items()}

if __name__=='__main__':
  for q,nmax in [(3,9),(4,7),(5,6)]:
    for n in range(3,nmax+1):
      p=poly_model(q,n);t=transfer(q,n);b=brute(q,n)
      assert p==t==b,(q,n,p,t,b)
      assert sum(p.values())==q*(q-1)**(n-1)
      assert n-2 not in p
      assert set(p)==set(range(n-2))|{n-1},(q,n,p)
      if n>=4:
        a=q-2;L=n-2;I=[0]*(L-1)
        I[0]=1
        if L>=3:I[1]=1+a
        for i in range(2,L-1):I[i]=I[i-1]+a*I[i-2]
        assert p[0]==q*(q-1)*I[-1]
      assert p[n-1]==q*(q-1)*(q-2)**(n-2)
      print(q,n, 'words',sum(p.values()), 'spectrum',sorted(p.items()))
  print('ALL_CHECKS_PASSED')
