#!/usr/bin/env python3
"""Independent finite-channel and moment checks for one length-three permutation burst."""
from fractions import Fraction
from itertools import product, permutations
from collections import Counter

def channel_count(x):
    n=len(x)
    out={x}
    for i in range(n-2):
        t=x[i:i+3]
        for p in set(permutations(t)):
            out.add(x[:i]+p+x[i+3:])
    return len(out)

def identity(x):
    n=len(x)
    E=[int(x[i]==x[i+1]) for i in range(n-1)]
    F=[int(x[i]==x[i+2]) for i in range(n-2)]
    H=[int(x[i]==x[i+1]==x[i+2]) for i in range(n-2)]
    d=5*sum(E)+3*sum(F)-2*(E[0]+E[-1])-4*sum(H)
    return 4*n-6-d

def mean(q,n):
    return Fraction(4*n-6,1)-Fraction(8*n-15,q)+Fraction(4*(n-2),q*q)

def variance(q,n):
    return Fraction((q-1)*(34*n*q*q-88*n*q+48*n-75*q*q+208*q-128),q**4)

def main():
    examples=0
    moments=0
    for q in (2,3,4,5):
        for n in range(3,9 if q<=4 else 8):
            dist=Counter()
            for x in product(range(q),repeat=n):
                direct=channel_count(x)
                form=identity(x)
                if direct!=form:
                    raise AssertionError(('identity',q,n,x,direct,form))
                dist[direct]+=1
                examples+=1
            if n<=6:
                total=q**n
                mu=sum(k*c for k,c in dist.items())/total
                # Use exact rationals.
                m1=Fraction(sum(k*c for k,c in dist.items()),total)
                m2=Fraction(sum(k*k*c for k,c in dist.items()),total)
                v=m2-m1*m1
                if m1!=mean(q,n) or v!=variance(q,n):
                    raise AssertionError(('moments',q,n,m1,v,mean(q,n),variance(q,n)))
                moments+=1
    print('CERTIFICATE_OK direct_channel_words=',examples,'exact_moment_profiles=',moments)

if __name__=='__main__':
    main()
