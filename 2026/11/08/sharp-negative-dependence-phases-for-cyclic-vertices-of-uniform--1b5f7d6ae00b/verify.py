"""Exact checks for cyclic-vertex dependence of uniform finite mappings.

Run with: python3 verify.py
Only Python's standard library is required.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial


def tail_moments(n):
    # a[k] = P(number of cyclic vertices >= k) (birthday tail).
    a = [Q(1)]
    for k in range(1, n+1):
        a.append(a[-1]*Q(n-k+1,n))
    m = sum(a[1:],Q(0))
    p1 = m/n
    p2 = Q(2)*(n-m)/(n*(n-1)) if n>=2 else Q(0)
    return m,p1,p2


def cyclic_mask(mapping):
    n=len(mapping)
    mask=0
    for v in range(n):
        u=v
        seen=set()
        while u not in seen:
            seen.add(u)
            u=mapping[u]
        if u==v:
            # A vertex is cyclic iff the orbit returns to it.
            mask |= 1<<v
    return mask


def exhaustive(n):
    counts=[0]*(1<<n)
    for mapping in product(range(n),repeat=n):
        counts[cyclic_mask(mapping)]+=1
    total=n**n
    p1=sum(counts[s] for s in range(1<<n) if s&1)
    p2=sum(counts[s] for s in range(1<<n) if (s&3)==3) if n>=2 else 0
    p4=sum(counts[s] for s in range(1<<n) if (s&15)==15) if n>=4 else 0
    return (Q(p1,total),Q(p2,total),Q(p4,total),counts,total)


def is_increasing_function(bits,m):
    return all(not (bits>>a & 1) or all(bits>>b&1 for b in range(1<<m) if (b&a)==a) for a in range(1<<m))


def check():
    checks=0
    assert Q(707,500)**2<2; checks+=1
    assert Q(63,50)**2>Q(11,7); checks+=1
    assert Q(13*77,500)>2; checks+=1
    # a_k-a_{k+1}=k*a_k/n, so k(n)_k/n^(k+1) is the cyclic count mass.
    # Sum identities imply E(K)_2=2(n-M).
    signs={}
    for n in range(2,169):
        m,p1,p2=tail_moments(n)
        cov=p2-p1*p1
        expected='negative' if n<=5 else 'positive'
        assert (cov<0 if expected=='negative' else cov>0), (n,cov)
        checks+=1
        signs[n]=expected
    for n in range(2,7):
        p1,p2,p4,counts,total=exhaustive(n)
        m,q1,q2=tail_moments(n)
        assert p1==q1 and p2==q2, (n,p1,q1,p2,q2)
        checks+=2
        if n==4:
            assert p1==Q(71,128)
            assert p2==Q(19,64)
            assert p4==Q(3,32)
            assert p2-p1*p1==Q(-177,16384)
            assert p4-p2*p2==Q(23,4096)
            checks+=5
        if n==3:
            # Check all increasing Boolean functions of a disjoint pair
            # against an increasing function of the remaining singleton.
            for bits in range(16):
                if not is_increasing_function(bits,2):
                    continue
                ef=Q(sum(counts[s] for s in range(8) if bits>>(s&3)&1),total)
                eg=Q(sum(counts[s] for s in range(8) if s&4),total)
                efg=Q(sum(counts[s] for s in range(8) if bits>>(s&3)&1 and s&4),total)
                assert efg-ef*eg<=0
                checks+=1
    # For n>=169 the analytic bound is:
    # M_n<=1+sqrt(pi*n/2)<1+sqrt(11*n/7)<sqrt(2*n)-1
    # <2n/(sqrt(2n-1)+1); exact rational comparisons above validate
    # the only nontrivial rational comparison at n=169.
    print('PASS',checks,'exact assertions; all 2<=n<=168 certified and n>=169 by analytic bound')
    print('n=4: pairwise covariance -177/16384; disjoint pair-events +23/4096')
    print('strict pairwise sign: negative n=2..5; positive n>=6')

if __name__=='__main__': check()
