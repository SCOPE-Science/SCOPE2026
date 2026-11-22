"""Standalone exact sanity checks for pure distance-two hopping of independent sets on rings.

Usage: python check.py [max_n]. Works with Python standard library only.
Finite checks supplement, but do not replace, the all-length proof.
"""
import sys
from collections import Counter
from fractions import Fraction
from math import comb


def fib(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a


def gap_spectrum(n):
    """Independent anchored-gap enumeration of predicted half-degrees."""
    counts=Counter({0:1}) # empty set
    for k in range(1,n//2+1):
        for t in range(k+1):
            e=n-2*k-2*t
            if e<0:continue
            c=0
            if t==0:
                if e<=k:c=comb(k,e)
            else:
                for j in range(min(k-t,e)+1):
                    c+=comb(k-t,j)*comb(e-j+t-1,t-1)
            val=Fraction(n*comb(k,t)*c,k)
            if val.denominator!=1:
                raise AssertionError((n,k,t,val))
            counts[t]+=val.numerator
    return counts


def direct_spectrum(n):
    """Enumerate the actual reconfiguration graph via bit moves, not gaps."""
    counts=Counter()
    vertices=0;sum_degree=0
    for bits in range(1<<n):
        if any((bits>>i&1) and (bits>>((i+1)%n)&1) for i in range(n)):
            continue
        vertices+=1
        neighbors=set()
        for i in range(n):
            if not (bits>>i&1):continue
            for delta in (-2,2):
                j=(i+delta)%n
                if bits>>j&1:continue
                candidate=bits^(1<<i)^(1<<j)
                if all(not ((candidate>>q&1) and (candidate>>((q+1)%n)&1)) for q in range(n)):
                    neighbors.add(candidate)
        if len(neighbors)%2:
            raise AssertionError((n,bits,len(neighbors)))
        counts[len(neighbors)//2]+=1
        sum_degree+=len(neighbors)
    return counts,vertices,sum_degree//2


def extremal_count(n):
    h,r=divmod(n,4)
    if r==0:return 4
    if r==1:return n
    if r==2:return n*(h+3)//2
    return n*(h+1)*(h+8)//6


def main():
    high=int(sys.argv[1]) if len(sys.argv)>1 else 20
    total_checked=0
    for n in range(5,high+1):
        predicted=gap_spectrum(n)
        observed,vertices,edges=direct_spectrum(n)
        assert predicted==observed,(n,predicted,observed)
        assert vertices==fib(n-1)+fib(n+1),n
        assert edges==n*fib(n-3),(n,edges)
        assert max(observed)==n//4
        assert observed[n//4]==extremal_count(n)
        for t in range(n//4+1):assert observed[t]>0
        total_checked+=vertices
        print(f'n={n:2d} states={vertices:6d} edges={edges:7d} half-degree={dict(sorted(observed.items()))}')
    # Numerically check the analytic gap coefficient, edge and extremum identities
    # at larger lengths; these share the same gap formula, unlike direct_spectrum.
    for n in range(high+1,76):
        predicted=gap_spectrum(n)
        assert max(predicted)==n//4
        assert predicted[n//4]==extremal_count(n)
        assert sum(t*v for t,v in predicted.items())==n*fib(n-3)
    print(f'PASS: {total_checked} explicitly inspected legal states, lengths 5..{high};')
    print('PASS: exact gap enumerator/extremal/edge identity checks through length 75')

if __name__=='__main__':main()
