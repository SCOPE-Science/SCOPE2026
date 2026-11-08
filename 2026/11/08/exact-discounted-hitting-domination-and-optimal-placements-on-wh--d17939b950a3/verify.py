#!/usr/bin/env python3
"""Standalone direct equilibrium and rational structural checks on wheels."""
from fractions import Fraction as F
from itertools import combinations
from math import comb

def fvals(lam,m):
    # homogeneous solution of y_i=(lam/3)(y_{i-1}+y_{i+1})
    p=[F(0),F(1)]
    for k in range(1,m):p.append(F(3,1)/lam*p[-1]-p[-2])
    return [(p[m-j]+p[j])/p[m] for j in range(1,m)]

def wheel_score(lam,n,hub,selected):
    c=lam/(3-2*lam)
    k=len(selected)
    if hub:
        if k==0:return c
        gaps=cyclic_gaps(n,selected)
        return min([F(1)]+[c+(1-c)*min([F(1)]+fvals(lam,m)) for m in gaps])
    assert k>=1
    gaps=cyclic_gaps(n,selected)
    Q=sum((sum(fvals(lam,m)) for m in gaps),F(0))
    x=lam*(k+Q)/(n-lam*c*(n-k-Q))
    v=min([F(1)]+[c*x+(1-c*x)*min([F(1)]+fvals(lam,m)) for m in gaps])
    return min(x,v)

def cyclic_gaps(n,selected):
    s=sorted(selected)
    return [((s[(j+1)%len(s)]-s[j])%n or n) for j in range(len(s))]

def balanced_score(lam,n,k,hub):
    c=lam/(3-2*lam)
    if hub and k==0:return c
    assert 1<=k<=n
    a,b=divmod(n,k)
    gaps=[a]*(k-b)+[a+1]*b
    if hub:return min([F(1)]+[c+(1-c)*min([F(1)]+fvals(lam,m)) for m in gaps])
    Q=sum((sum(fvals(lam,m)) for m in gaps),F(0))
    x=lam*(k+Q)/(n-lam*c*(n-k-Q))
    return min(x,min([F(1)]+[c*x+(1-c*x)*min([F(1)]+fvals(lam,m)) for m in gaps]))

def direct_equilibrium(lam,n,hub,selected):
    import numpy as np
    N=n+1
    S=set(selected)
    if hub:S.add(n)
    unknown=[i for i in range(N) if i not in S]
    A=np.eye(len(unknown))
    b=np.zeros(len(unknown))
    adj=[[(i-1)%n,(i+1)%n,n] for i in range(n)]+[list(range(n))]
    pos={v:i for i,v in enumerate(unknown)}
    for v in unknown:
        j=pos[v]
        for w in adj[v]:
            p=float(lam)/len(adj[v]);
            if w in S:b[j]+=p
            else:A[j,pos[w]]-=p
    ans=np.ones(N)
    if unknown:
        x=np.linalg.solve(A,b)
        for v,y in zip(unknown,x):ans[v]=y
    return float(min(ans))

def comp_count(n,k,M):
    # Number of labelled k-subsets with every cyclic gap at most M.
    if k==0:return 0
    from functools import lru_cache
    @lru_cache(None)
    def ways(t,rem):
        if t==0:return int(rem==0)
        return sum(ways(t-1,rem-d) for d in range(1,M+1) if rem>=d)
    val=n*ways(k,n)
    assert val%k==0
    return val//k

def run():
    tested=0; optcases=0; success=0
    for lam in [F(1,5),F(1,2),F(4,5)]:
        for n in range(4,9):
            max0={};max1={};all0={};all1={}
            for k in range(0,n+1):
                for selected in combinations(range(n),k):
                    for hub in [False,True]:
                        if not hub and not k:continue
                        theory=wheel_score(lam,n,hub,selected)
                        direct=direct_equilibrium(lam,n,hub,selected)
                        assert abs(float(theory)-direct)<1e-10,(n,lam,hub,selected,theory,direct)
                        key=max1 if hub else max0
                        key[k]=max(key.get(k,F(0)),theory)
                        (all1 if hub else all0).setdefault(k,[]).append((selected,theory))
                        tested+=1
            for k in range(n+1):
                if k:
                    assert max0[k]==balanced_score(lam,n,k,False),(n,lam,k,'rim')
                    actual=sum(v==max0[k] for _,v in all0[k])
                    a,b=divmod(n,k)
                    expected=n*comb(k,b)//k
                    assert actual==expected,(n,lam,k,'balanced_count',actual,expected)
                assert max1[k]==balanced_score(lam,n,k,True),(n,lam,k,'hub')
                if k:
                    actual=sum(v==max1[k] for _,v in all1[k])
                    expected=comp_count(n,k,(n+k-1)//k)
                    assert actual==expected,(n,lam,k,'hub_count',actual,expected)
                optcases+=1
    # Exactly classify wheel n=4, lambda=1/2, tau=1/3.
    n=4;lam=F(1,2);tau=F(1,3)
    feasible=[]
    for hub in [False,True]:
      for k in range(n+1):
       for selected in combinations(range(n),k):
        if not hub and not k:continue
        if wheel_score(lam,n,hub,selected)>=tau:
            feasible.append((k+int(hub),hub,selected))
    best=min(x[0] for x in feasible)
    opts=sorted((x[1],x[2]) for x in feasible if x[0]==best)
    assert best==2 and opts==[(False,(0,2)),(False,(1,3))],(best,opts)
    print('DIRECT_EQUILIBRIUM_OK',tested,'source_sets')
    print('BALANCED_MAXIMIN_AND_OPTIMIZER_COUNTS_OK',optcases,'cardinality_cases')
    print('EXACT_HUB_FREE_OPTIMUM_OK',len(opts),'configurations')
    print('VERIFY_OK')
if __name__=='__main__':run()
