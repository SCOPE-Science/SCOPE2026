"""Exact-arithmetic corroboration for one-short-edge cycle Lipschitz variance.

Usage: python3 verify.py. Python standard library only.
The infinite-dimensional claim relies on the written mathematical proof.
"""
from fractions import Fraction as Q
from itertools import product
from collections import defaultdict

def var(y):
    n=len(y)
    return sum(t*t for t in y)/n-(sum(y)/n)**2

def formula(n,l):
    if n%2:
        return Q((n*n-1)*(n*n+3),48*n*n)
    return Q(n*n-4,48)+l*l/4

def canonical(n,l):
    m=n//2
    d=([Q(1)]*m+[Q(-1)]*m+[Q(0)]) if n%2 else ([Q(1)]*(m-1)+[l]+[Q(-1)]*(m-1)+[-l])
    assert sum(d)==0
    y=[Q(0)]
    for x in d[:-1]: y.append(y[-1]+x)
    return var(y)

def exact_max(n,l):
    limits=[Q(1)]*(n-1)+[l]
    best=Q(-1)
    winners=set()
    count=0
    for free in range(n):
        other=[i for i in range(n) if i!=free]
        for signs in product((-1,1),repeat=n-1):
            steps=[Q(0)]*n
            for i,s in zip(other,signs):steps[i]=s*limits[i]
            steps[free]=-sum(steps)
            if abs(steps[free])>limits[free]:continue
            heights=[Q(0)]
            for a in steps[:-1]:heights.append(heights[-1]+a)
            v=var(heights)
            count+=1
            if v>best:best=v; winners={tuple(steps)}
            elif v==best:winners.add(tuple(steps))
    return best,count,len(winners)

def green(n,i,j):
    r=(i-j)%n
    return Q(n*n-1,12*n)-Q(r*(n-r),2*n)

def polarization_check(n):
    # The finite-circle polarization proof uses a strict distance-to-zero
    # auxiliary preference to resolve ties. Test its cross-pair inequalities.
    score=lambda i:-10*min(i,n-i)+(1 if 0<i<=n//2 else 0)
    for c in range(n):
        R=lambda z:(c-z)%n
        H={i for i in range(n) if score(i)>=score(R(i))}
        for p in H:
            for q in H:
                if green(n,p,q)<green(n,p,R(q)):
                    return False
    # Any reversed rank pair has a reflection exchanging it, such that
    # the earlier-ranked site is on the preferred side.
    for a in range(n):
        for b in range(n):
            if score(a)>score(b):
                c=(a+b)%n
                if not(score(a)>score((c-a)%n)):
                    return False
    return True

if __name__=='__main__':
    cases=0
    for n in range(3,11):
        for l in (Q(1,5),Q(1,2),Q(4,5),Q(1)):
            got,vertices,winners=exact_max(n,l)
            want=formula(n,l)
            assert got==want,(n,l,got,want)
            assert canonical(n,l)==want,(n,l,'canonical')
            cases+=1
        print('EXACT_WEIGHTED_CYCLE_EXTREMA_OK',n, 'vertex_instances',vertices)
    print('EXACT_CYCLE_FORMULAS_OK',cases)
    for n in range(3,31):
        assert polarization_check(n),n
    print('REFLECTION_KERNEL_PAIRWISE_COMPARISONS_OK',28)
    print('ALL_ONE_SHORT_EDGE_CYCLE_TESTS_OK')
