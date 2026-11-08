#!/usr/bin/env python3
"""Independent exact checks for sparse directed trust-game Shapley laws.
Uses coalition marginals rather than the local closed form in the core test.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
from math import comb, factorial, exp, log


def direct_value(n, edges, mask):
    inn = 0
    ext_targets = set()
    for a,b in edges:
        if mask>>a&1 and mask>>b&1:
            inn += 1
        elif not(mask>>a&1) and mask>>b&1:
            ext_targets.add(b)
    return inn+len(ext_targets)


def shapley_by_coalitions(n, edges):
    values = [direct_value(n, edges, S) for S in range(1<<n)]
    den=factorial(n)
    sh=[]
    for i in range(n):
        u=F(0)
        for S in range(1<<n):
            if not (S>>i)&1:
                size=S.bit_count()
                u+=F(factorial(size)*factorial(n-size-1),den)*(values[S|(1<<i)]-values[S])
        sh.append(u)
    return sh


def shapley_local(n, edges):
    di=[0]*n
    do=[0]*n
    for a,b in edges:
        do[a]+=1;di[b]+=1
    out=[]
    for i in range(n):
        x=F(di[i]+do[i],2)+F(di[i],di[i]+1)
        for a,b in edges:
            if a==i:
                x-=F(1,di[b]+1)
        out.append(x)
    return out


def binomlaw(N,p):
    return [F(comb(N,k))*p**k*(1-p)**(N-k) for k in range(N+1)]


def conv(A,B):
    C=defaultdict(F)
    for x,px in A.items():
        for y,py in B.items():C[x+y]+=px*py
    return dict(C)


def factorized_root_distribution(n,p):
    # Exact law for the Shapley payoff of any prescribed root.
    din=binomlaw(n-1,p)
    dout=binomlaw(n-1,p)
    B=binomlaw(n-2,p)
    mark={F(b,2*(b+2)):pb for b,pb in enumerate(B)}
    z={F(0):F(1)}
    law=defaultdict(F)
    for k,pk in enumerate(dout):
        for d,pd in enumerate(din):
            H=F(d,2)+F(d,d+1)
            for v,pv in z.items():law[H+v]+=pk*pd*pv
        z=conv(z,mark)
    return dict(law)


def test(n,p):
    pairs=[(a,b) for a in range(n) for b in range(n) if a!=b]
    dist=defaultdict(F)
    m=len(pairs)
    for bits in range(1<<m):
        edges=[pair for j,pair in enumerate(pairs) if bits>>j&1]
        direct=shapley_by_coalitions(n,edges)
        local=shapley_local(n,edges)
        assert local==direct,(n,bits,direct,local)
        assert sum(direct)==len(edges)
        weight=p**len(edges)*(1-p)**(m-len(edges))
        dist[direct[0]]+=weight
    factorized=factorized_root_distribution(n,p)
    assert dict(dist)==factorized,(dist,factorized)
    q=F(0)
    for v,pr in dist.items():
        if v==0:q+=pr
    expected=(1-p)**(n-1)*(1-p+p*(1-p)**(n-2))**(n-1)
    assert q==expected,(q,expected)
    mean=sum(v*pr for v,pr in dist.items())
    assert mean==(n-1)*p,(mean,(n-1)*p)
    print('n=%d: %d complete labeled directed graphs, %d exact root-payoff values, P(phi=0)=%s, E(phi)=%s' % (n,1<<m,len(dist),q,mean))

for n,p in [(2,F(1,3)),(3,F(1,3)),(4,F(1,3))]:
    test(n,p)
# Critical-window extra condition behind equivalence to isolates:
for n in [1000,10000,100000]:
    p=log(n)/(2*n)
    q=(1-p)**(n-1)*(1-p+p*(1-p)**(n-2))**(n-1)
    qiso=(1-p)**(2*(n-1))
    print('critical n=%d: expected null=%0.6f, expected isolate=%0.6f, difference=%0.6f' % (n,n*q,n*qiso,n*(q-qiso)))
print('All exact checks passed.')
