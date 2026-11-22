"""Standalone diagnostic checks for the refuge-protection allocation theorem.

Run: python check.py.  Uses Python standard library only.
Numerical sampling is supplementary: the universal proof is in RESULT.md.
"""
from fractions import Fraction
import math
import random


def benefit(theta, alloc):
    assert theta > 0 and all(v >= 0 for v in alloc)
    return sum(math.exp(-theta/v) if v > 0 else 0.0 for v in alloc)


def candidates(n, theta):
    return [j*math.exp(-j*theta) for j in range(1,n+1)]


def support(n, theta):
    values=candidates(n,theta)
    return [j+1 for j,v in enumerate(values) if abs(v-max(values)) < 2e-12]


def expected(n, theta):
    return [j for j in range(1,n+1) if (j==1 or theta <= math.log(j/(j-1))) and (j==n or theta >= math.log((j+1)/j))]


def exact_ties():
    checks=0
    for n in range(2,18):
        for j in range(1,n):
            # theta=log((j+1)/j); exp(-k theta)=(j/(j+1))**k.
            r=Fraction(j,j+1)
            vals=[k*r**k for k in range(1,n+1)]
            maximum=max(vals)
            assert [k for k,v in enumerate(vals,1) if v==maximum]==[j,j+1]
            checks+=n
    return checks


def grid_search():
    checks=0
    # For all integer simplex grid allocations, compare to continuous optimum.
    for n in range(2,6):
        for theta in (0.03,0.15,0.28,0.34,0.41,0.55,0.68,0.72,1.00,1.70):
            m=max(candidates(n,theta))
            scale=30
            def compositions(k, remaining, prefix=()):
                if k==1:
                    yield prefix+(remaining,)
                else:
                    for t in range(remaining+1):
                        yield from compositions(k-1,remaining-t,prefix+(t,))
            for comp in compositions(n,scale):
                val=benefit(theta,[v/scale for v in comp])
                assert val <= m+5e-13,(n,theta,comp,val,m)
                checks+=1
    return checks


def random_search():
    rng=random.Random(317164)
    checks=0
    for n in (2,3,4,5,6,8,12):
        for _ in range(8000):
            theta=math.exp(rng.uniform(math.log(.001),math.log(5.0)))
            alloc=[rng.random()**(rng.randrange(1,6)) for _ in range(n)]
            sm=sum(alloc)
            alloc=[a/sm for a in alloc]
            val=benefit(theta,alloc)
            target=max(candidates(n,theta))
            assert val <= target+1e-12,(n,theta,alloc,val,target)
            checks+=1
    return checks


def pairwise_shape():
    checks=0
    for c in (.0001,.01,.1,.3,.5, math.log(2),.7,.9,1.0,1.5,5,20):
        base=max(math.exp(-c),2*math.exp(-2*c))
        for i in range(1,10000):
            x=i/20000
            cur=math.exp(-c/x)+math.exp(-c/(1-x))
            assert cur<=base+1e-14,(c,x,cur,base)
            checks+=1
    return checks


def boundaries():
    checks=0
    for n in range(2,25):
        for j in range(1,n):
            theta=math.log((j+1)/j)
            delta=min(1e-5,theta/100)
            assert support(n,theta+delta)==[j]
            assert support(n,theta-delta)==[j+1]
            checks+=2
    return checks



def baseline_grid():
    checks=0
    # Baseline shelters beta>0 alter the transition locations but not the equal-positive-support reduction.
    for n in (2,3,4,5):
        for beta in (0.005,0.03,0.2,1.0,4.0):
            for theta in (0.01,0.1,0.4,0.8,1.5,4,15):
                proposed=max(j*math.exp(-theta/(beta+1/j))+(n-j)*math.exp(-theta/beta) for j in range(1,n+1))
                budget=22
                def compositions(k, rem, prefix=()):
                    if k==1:yield prefix+(rem,)
                    else:
                        for y in range(rem+1):
                            yield from compositions(k-1,rem-y,prefix+(y,))
                for co in compositions(n,budget):
                    outcome=sum(math.exp(-theta/(beta+r/budget)) for r in co)
                    assert outcome <= proposed +1e-12,(n,beta,theta,co,outcome,proposed)
                    checks+=1
    return checks

def main():
    for name, fn in [('exact_ties',exact_ties),('grid_search',grid_search),('random_search',random_search),('pairwise_shape',pairwise_shape),('boundaries',boundaries),('baseline_grid',baseline_grid)]:
        c=fn(); print(f'{name}: {c} assertions passed')
    print('All diagnostic checks passed; infinite-dimensional assertions are proved analytically in RESULT.md.')


if __name__=='__main__':
    main()
