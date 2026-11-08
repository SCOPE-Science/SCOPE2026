#!/usr/bin/env python3
"""Standalone exact rational simplex-integration verification.

For each layer-size composition, triangulate the order polytope by
linear extensions and map each simplex to the chain polytope by the
classical transfer map. Integrate moments over all simplices, without
using the closed-form proposed gap formula in the calculation.
"""
from itertools import product, permutations
from fractions import Fraction as F
from math import factorial

def product_perms(blocks):
    return product(*(permutations(b) for b in blocks))

def invariant_trace(composition):
    n=sum(composition)
    labels=[]; blocks=[]; current=0
    for m in composition:
        b=tuple(range(current,current+m));blocks.append(b);current+=m
    ntri=1
    for m in composition:ntri*=factorial(m)
    # expectation within every simplex has denominator (n+1)(n+2).
    mO=[F(0) for _ in range(n)];mC=[F(0) for _ in range(n)];
    qO=F(0);qC=F(0)
    covO=[[F(0) for _ in range(n)] for _ in range(n)]
    covC=[[F(0) for _ in range(n)] for _ in range(n)]
    for perms in product_perms(blocks):
        order=sum((list(t) for t in perms),[])
        prevmax={}
        for g,perm in enumerate(perms):
            for i in perm:
                prevmax[i]=perms[g-1][-1] if g else None
        verticesO=[];verticesC=[]
        for j in range(n+1):
            v=[0]*n
            for i in order[n-j:]:v[i]=1
            w=[v[i]-(v[prevmax[i]] if prevmax[i] is not None else 0) for i in range(n)]
            assert set(w).issubset({0,1})
            verticesO.append(v);verticesC.append(w)
        for vertices,mu,cov in [(verticesO,mO,covO),(verticesC,mC,covC)]:
            s=[sum(v[i] for v in vertices) for i in range(n)]
            for i in range(n):mu[i]+=F(s[i],ntri*(n+1))
            for i in range(n):
                for j in range(n):
                    cov[i][j]+=F(s[i]*s[j]+sum(v[i]*v[j] for v in vertices),ntri*(n+1)*(n+2))
    for i in range(n):
        for j in range(n):
            covO[i][j]-=mO[i]*mO[j]
            covC[i][j]-=mC[i]*mC[j]
    return covO,covC

def compositions(n):
    for mask in range(1<<(n-1)):
        c=[];prev=0
        for k in range(1,n):
            if mask&(1<<(k-1)):
                c.append(k-prev);prev=k
        c.append(n-prev)
        yield c

def e3(c):
    return sum(c[i]*c[j]*c[k]
               for i in range(len(c)) for j in range(i+1,len(c))
               for k in range(j+1,len(c)))

def main():
    cases=0;contrast=0;balance_cases=0;reflections=0
    for n in range(1,8):
        for comp in compositions(n):
            O,C=invariant_trace(comp)
            n=sum(comp)
            actual=sum((O[i][i]-C[i][i] for i in range(n)),F(0))
            expected=F(e3(comp),(n+1)**2*(n+2))
            assert actual==expected, (comp,actual,expected)
            starts=[];s=0
            for m in comp:starts.append(s);s+=m
            for g,m in enumerate(comp):
                s=starts[g];exp=F(s*(n-s-m),(n+1)**2*(n+2))
                for i in range(s,s+m):
                    for j in range(s,s+m):
                        # stronger within-block covariance matrix identity
                        assert O[i][j]-C[i][j]==exp,(comp,i,j,O[i][j]-C[i][j],exp)
                        contrast+=1
            cases+=1
    # Independent finite equality-class tests using the combinatorial e3 count.
    for n in range(3,12):
        for k in range(3,n+1):
            evalues=[(e3(comp),comp) for comp in compositions(n) if len(comp)==k]
            lo=min(a for a,_ in evalues);hi=max(a for a,_ in evalues)
            for v,comp in evalues:
                minimal=(sorted(comp)==[1]*(k-1)+[n-k+1])
                balanced=(max(comp)-min(comp)<=1)
                assert (v==lo)==minimal,(n,k,comp,lo,v)
                assert (v==hi)==balanced,(n,k,comp,hi,v)
                balance_cases+=1
    # Verify the explicit two-layer coordinate reflection by binary vertices.
    for n in range(2,8):
        for a in range(1,n):
            b=n-a
            O=set();C=set()
            for x in product((0,1),repeat=n):
                if max(x[:a])<=min(x[a:]):O.add(x)
                if not (any(x[:a]) and any(x[a:])):C.add(x)
            reflected={tuple(x[:a])+tuple(1-v for v in x[a:]) for x in O}
            assert reflected==C,(a,b)
            reflections+=1
    print('ORDER_CHAIN_DIRICHLET_SIMPLEX_CHECKS_PASSED',cases,contrast,balance_cases,reflections)
if __name__=='__main__':main()
