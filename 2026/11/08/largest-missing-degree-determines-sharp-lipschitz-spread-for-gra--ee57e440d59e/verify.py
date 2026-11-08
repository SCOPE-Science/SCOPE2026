"""Standalone finite checker for the C4-free complement Lipschitz-variance theorem.

Run with Python 3. No dependencies. All comparisons use exact integers.
"""
from itertools import product
from math import comb
from random import Random


def edges_of_mask(n, mask):
    pairs = [(i, j) for i in range(n) for j in range(i+1,n)]
    return {(i,j) for t,(i,j) in enumerate(pairs) if (mask>>t)&1}


def graph_data(n, deleted):
    adjh=[set() for _ in range(n)]
    for i,j in deleted:
        adjh[i].add(j); adjh[j].add(i)
    if any(len(adjh[i]&adjh[j])>=2 for i in range(n) for j in range(i+1,n)):
        return None
    adjg=[set(range(n))-{i}-adjh[i] for i in range(n)]
    if any(j not in adjg[i] and not(adjg[i]&adjg[j]) for i in range(n) for j in range(i+1,n)):
        return None
    edges=[(i,j) for i in range(n) for j in range(i+1,n) if j in adjg[i]]
    return edges,max(map(len,adjh))


def formula(n, degree):
    baseline=n*n//4
    if degree==0:return baseline
    k=min(degree,n//2+1)
    f=n*(k+1)-(k-1)**2
    return max(baseline,f)


def complete_check(n,mask):
    graph=graph_data(n,edges_of_mask(n,mask))
    if graph is None:return False
    edges,degree=graph
    target=formula(n,degree)
    actual=-1
    opt=0
    for rest in product(range(-2,3),repeat=n-1):
        f=(0,)+rest
        if any(abs(f[i]-f[j])>1 for i,j in edges):continue
        numer=n*sum(v*v for v in f)-sum(f)**2
        if numer>actual:actual=numer;opt=0
        if numer==actual:
            opt+=1
            if numer==target:
                mini,maxi=min(f),max(f)
                if maxi-mini==1:
                    assert sum(v==maxi for v in f) in {n//2,(n+1)//2}
                else:
                    assert maxi-mini==2
                    lo=sum(v==mini for v in f); hi=sum(v==maxi for v in f)
                    assert min(lo,hi)==1
                    k=max(lo,hi)
                    assert n*(k+1)-(k-1)**2==target
    assert actual==target,(n,mask,degree,target,actual)
    return True


def run():
    for n in range(4,6):
        accepted=0
        for m in range(1<<(n*(n-1)//2)):
            accepted+=bool(complete_check(n,m))
        print('EXHAUSTIVE_ALL_LABELED_COMPLEMENTS_OK',n,accepted)
    r=Random(20261102)
    for n,count in [(6,900),(7,70)]:
        accepted=0; attempts=0
        while accepted<count and attempts<90000:
            attempts+=1
            # Mix sparse cycle-ish deleted graphs and high-degree deleted stars.
            rate=r.choice([0.12,0.2,0.33,0.5])
            mask=sum((r.random()<rate)<<k for k in range(n*(n-1)//2))
            if graph_data(n,edges_of_mask(n,mask)) is None:continue
            complete_check(n,mask)
            accepted+=1
        assert accepted==count,(n,accepted)
        print('SEEDED_VALID_C4_FREE_DIAMETER_TWO_OK',n,accepted,attempts)
    for n in range(5,51):
        H={(i,(i+1)%n) if i<(i+1)%n else ((i+1)%n,i) for i in range(n)}
        graph=graph_data(n,H)
        assert graph is not None
        assert graph[1]==2
        assert formula(n,2)==max(n*n//4,3*n-1)
        assert (3*n-1>n*n//4)==(n<=11)
    print('COMPLEMENT_CYCLE_THRESHOLD_OK',46)
    for n in range(5,1001):
        b=n*n//4
        fmax=max([n*(k+1)-(k-1)**2 for k in range(1,n-1)])
        assert fmax==b+2*n
        for delta in [0,1,2,n//4,n//2,n-2]:
            delta=min(delta,n-2)
            v=max([b]+[n*(k+1)-(k-1)**2 for k in range(1,delta+1)])
            assert v==formula(n,delta)
    print('EXACT_QUADRATIC_ENVELOPE_OK',996)
    print('ALL_C4_FREE_SPREAD_CHECKS_OK')

if __name__=='__main__':run()
