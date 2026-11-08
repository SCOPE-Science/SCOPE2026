#!/usr/bin/env python3
"""Standalone exact checks for the random noncrossing-partition outer/block-size covariance."""
from fractions import Fraction
from math import comb


def catalan(n):
    return comb(2*n,n)//(n+1)


def partitions(n):
    """Generate each set partition as a restricted-growth string."""
    if n == 0:
        yield ()
        return
    def extend(a,k):
        if len(a)==n:
            yield tuple(a)
        else:
            for q in range(k+2):
                a.append(q)
                yield from extend(a,max(k,q))
                a.pop()
    yield from extend([0],0)


def blocks_from_rgs(a):
    b=[[] for _ in range(max(a)+1)]
    for j,v in enumerate(a): b[v].append(j+1)
    return b


def noncrossing(blocks):
    for ix,A in enumerate(blocks):
        for B in blocks[ix+1:]:
            for a in A:
                for c in A:
                    if c<=a:continue
                    for b in B:
                        if not a<b<c:continue
                        for d in B:
                            if c<d:return False
            for a in B:
                for c in B:
                    if c<=a:continue
                    for b in A:
                        if not a<b<c:continue
                        for d in A:
                            if c<d:return False
    return True


def outer_count(blocks):
    return sum(not any(
        (min(A)<min(B) and max(B)<max(A))
        for A in blocks if A is not B) for B in blocks)


def expected_block_count(n,r):
    return Fraction(comb(2*n-r-1,n-r),catalan(n))


def expected_outer(n):
    return Fraction(3*n,n+2)


def mixed(n,r):
    M=comb(2*n-r-1,n-r)
    return Fraction(M*(3*n-2*r),n*catalan(n))


def covariance(n,r):
    M=comb(2*n-r-1,n-r)
    return Fraction(2*M*(3*n-r*(n+2)),n*(n+2)*catalan(n))


def run():
    tests=0
    for n in range(1,10):
        c=tot_R=0
        sums=[0]*(n+1); cross=[0]*(n+1)
        for a in partitions(n):
            blocks=blocks_from_rgs(a)
            if not noncrossing(blocks):continue
            c+=1
            R=outer_count(blocks)
            tot_R+=R
            for r in range(1,n+1):
                count=sum(len(B)==r for B in blocks)
                sums[r]+=count
                cross[r]+=R*count
        assert c==catalan(n),(n,'Catalan',c,catalan(n));tests+=1
        assert Fraction(tot_R,c)==expected_outer(n);tests+=1
        for r in range(1,n+1):
            assert Fraction(sums[r],c)==expected_block_count(n,r),(n,r,'mean');tests+=1
            assert Fraction(cross[r],c)==mixed(n,r),(n,r,'mixed');tests+=1
            assert Fraction(cross[r],c)-Fraction(tot_R,c)*Fraction(sums[r],c)==covariance(n,r),(n,r,'cov');tests+=1
            if n>=2:
                sign=1 if (r==1 or (r==2 and n>=5)) else (0 if r==2 and n==4 else -1)
                assert (covariance(n,r)>0)-(covariance(n,r)<0)==sign,(n,r,'sign');tests+=1
        print(f'noncrossing n={n}: {c} partitions, all exact identities hold')
    for n in range(100,1101,100):
        for r in (1,2,3,4,5,7):
            mu=expected_block_count(n,r)
            cov=covariance(n,r)
            ratio=float(mu)/n
            assert abs(ratio-2**(-r-1))<0.01,(n,r,ratio)
            if r==3:
                assert abs(float(n*cov)+.75)<.015,(n,r,float(n*cov))
            else:
                assert abs(float(cov)-(3-r)/2**r)<.05,(n,r,float(cov))
            tests+=1
    print(f'PASS {tests} exact or bounded asymptotic assertions; independent exhaustive enumeration through n=9')

if __name__=='__main__':run()
