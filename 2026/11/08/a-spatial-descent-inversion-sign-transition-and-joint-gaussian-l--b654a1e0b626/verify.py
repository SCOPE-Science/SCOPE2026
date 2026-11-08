"""Exact finite-checker for two-packet riffle-shuffle descent/inversion claims.

Run: python verify.py. Requires only Python standard library.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import defaultdict
from math import comb

checks=0

def check(a,b,tag):
    global checks
    assert a==b,(tag,a,b)
    checks+=1


def stats(bits):
    n=len(bits)
    desc=[int(bits[i]>bits[i+1]) for i in range(n-1)]
    inv=sum(bits[i]>bits[j] for i in range(n) for j in range(i+1,n))
    return desc,inv


def perm_from_bits(bits):
    """Invert the stable digit sort permutation to get the forward shuffle."""
    sorted_labels=sorted(range(len(bits)),key=lambda k:(bits[k],k))
    perm=[0]*len(bits)
    for rank,orig in enumerate(sorted_labels,1):
        perm[orig]=rank
    return tuple(perm)


def direct_shuffle_dist(n,p):
    d=defaultdict(F)
    r=1-p
    for k in range(n+1):
        for idx in combinations(range(n),k):
            i,j=1,k+1
            s=set(idx)
            perm=[]
            for pos in range(n):
                if pos in s:
                    perm.append(i); i+=1
                else:
                    perm.append(j); j+=1
            d[tuple(perm)]+=p**k*r**(n-k)
    return d

for p in [F(1,5),F(3,10),F(1,2),F(7,10),F(4,5)]:
    r=1-p; q=p*r; delta=r-p
    for n in range(2,10):
        m=n-1
        eD=eI=eD2=eI2=eDI=F(0)
        eBI=[F(0) for _ in range(m)]
        eB=[F(0) for _ in range(m)]
        distribution=defaultdict(F)
        for bits in product((0,1),repeat=n):
            w=p**bits.count(0)*r**bits.count(1)
            desc,I=stats(bits)
            D=sum(desc)
            eD+=w*D; eI+=w*I; eD2+=w*D*D; eI2+=w*I*I; eDI+=w*D*I
            for i in range(m):
                eB[i]+=w*desc[i]
                eBI[i]+=w*desc[i]*I
            if n<=7: distribution[perm_from_bits(bits)]+=w
        check(eD,m*q,('meanD',p,n))
        check(eI,comb(n,2)*q,('meanI',p,n))
        check(eD2-eD*eD,m*q*(1-q)-2*(n-2)*q*q,('varD',p,n))
        check(eI2-eI*eI,comb(n,2)*q*(1-q)+2*comb(n,3)*q*(1-3*q),('varI',p,n))
        check(eDI-eD*eI,m*q*(1-q)+comb(m,2)*q*delta*delta,('covDI',p,n))
        for i in range(1,n):
            check(eB[i-1],q,('meanB',p,n,i))
            check(eBI[i-1]-eB[i-1]*eI,q*(1-q+delta*((i-1)-p*(n-2))),('covBI',p,n,i))
        if n<=7:
            check(dict(distribution),dict(direct_shuffle_dist(n,p)),('forward_shuffle_law',p,n))
        # Monotonic spatial covariance, and finite sign switch iff the threshold holds.
        c=[q*(1-q+delta*((i-1)-p*(n-2))) for i in range(1,n)]
        if p==F(1,2):
            check(len(set(c)),1,('fair_flat',n))
        else:
            check(all((c[i+1]>c[i])==(delta>0) for i in range(len(c)-1)),True,('spatial_slope',p,n))
            criterion=n>2+(1-q)/(min(p,r)*abs(delta))
            check(min(c)<0<max(c),criterion,('spatial_sign',p,n))
        # The limiting Gaussian covariance matrix is strictly positive definite.
        check(1-12*q*q>0,True,('nondegenerate',p,n))

print('PASS:',checks,'exact assertions; exhaustive iid words through n=9 and forward shuffle distributions through n=7.')
