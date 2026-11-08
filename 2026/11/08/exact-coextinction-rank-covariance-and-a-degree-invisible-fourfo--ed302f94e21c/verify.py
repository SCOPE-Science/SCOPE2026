#!/usr/bin/env python3
"""Independent exhaustive checks of the random coextinction rank-covariance law."""
from fractions import Fraction as F
from itertools import permutations
from collections import Counter
from math import factorial

def analytic(n,A,B):
    a,b,c=len(A),len(B),len(A&B)
    u=a+b-c
    return F(n+1,(a+1)*(b+1))*(F(c*(n-u),u+2)-F((a-c)*(b-c),u+1))

def empirical(n,A,B):
    N=factorial(n)
    sa=sb=sab=0
    for perm in permutations(range(n)):
        ranks=[0]*n
        for t,j in enumerate(perm,1):ranks[j]=t
        x=max(ranks[i] for i in A)
        y=max(ranks[i] for i in B)
        sa+=x;sb+=y;sab+=x*y
    return F(sab,N)-F(sa,N)*F(sb,N)

def variance_network(n,neighbors):
    m=len(neighbors)
    return sum((analytic(n,A,B) for A in neighbors for B in neighbors),F(0))/(m*m*(n+1)**2)

def main():
    checks=0
    for n in range(1,8):
        for a in range(1,n+1):
            for b in range(1,n+1):
                for c in range(max(0,a+b-n),min(a,b)+1):
                    A=set(range(a))
                    B=set(range(c))|set(range(a,a+b-c))
                    assert len(B)==b and len(A&B)==c
                    x=analytic(n,A,B)
                    y=empirical(n,A,B)
                    assert x==y,(n,a,b,c,x,y)
                    checks+=1
                    diag=analytic(n,A,A)
                    assert diag==F(a*(n-a)*(n+1),(a+1)**2*(a+2))
                    checks+=1
                    if c==0 and a+b<=n and n>=2: assert x<0;checks+=1
                    if A<=B and b<n: assert x>0;checks+=1
                    if A==B and a==n: assert x==0;checks+=1
    ring=[{0,1},{1,2},{2,3},{3,0}]
    blocks=[{0,1},{0,1},{2,3},{2,3}]
    assert variance_network(4,ring)==F(1,1800);checks+=1
    assert variance_network(4,blocks)==F(1,450);checks+=1
    for neighbors,distribution in [(ring,{F(13,20):16,F(7,10):8}),(blocks,{F(7,10):16,F(3,5):8})]:
        counts=Counter()
        for perm in permutations(range(4)):
            ranks=[0]*4
            for t,j in enumerate(perm,1):ranks[j]=t
            R=sum(max(ranks[k] for k in A) for A in neighbors)
            counts[F(R,4*5)]+=1
            checks+=1
        assert counts==distribution,(counts,distribution);checks+=1
        E=sum((x*ct for x,ct in counts.items()),F(0))/24
        V=sum(((x-E)**2*ct for x,ct in counts.items()),F(0))/24
        assert E==F(2,3) and V==variance_network(4,neighbors)
        checks+=2
    print('PASS',checks,'exact rational checks; two bipartite networks E[R]=2/3; Var 1/1800 versus 1/450')
if __name__=='__main__':main()
