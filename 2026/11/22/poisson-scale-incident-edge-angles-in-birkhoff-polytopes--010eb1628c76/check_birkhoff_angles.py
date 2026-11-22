"""Exact local-edge geometry checks and asymptotic sampling for the Birkhoff polytope.
Only finite instances are verified here; the all-dimensional statement is proved separately.
"""
from itertools import permutations, combinations
from collections import defaultdict, Counter
from fractions import Fraction
from math import factorial, comb, sqrt
from random import Random


def active_cycle(perm):
    n=len(perm); seen=[False]*n; lengths=[]
    for a in range(n):
        if not seen[a]:
            k=0; b=a
            while not seen[b]:
                seen[b]=True; b=perm[b]; k+=1
            if k>1: lengths.append(k)
    return len(lengths)==1


def falling(x,k):
    r=1
    for i in range(k):r*=x-i
    return r


def check_small(n):
    perms=[p for p in permutations(range(n)) if active_cycle(p)]
    expected=sum(comb(n,k)*factorial(k-1) for k in range(2,n+1))
    assert len(perms)==expected
    by_T=defaultdict(list)
    for p in perms:by_T[tuple(i for i,v in enumerate(p) if v==i)].append(p)
    hist=Counter()
    for sigma in perms:
        s=sum(i==v for i,v in enumerate(sigma))
        for T,taus in by_T.items():
            t=len(T)
            good=[i for i in range(n) if i!=sigma[i] and i not in T and sigma[i] not in T]
            u=len(good)
            den=n-t-1
            for j in range(min(3,len(taus),u,den,n-s-1)+1):
                actual=sum(falling(sum(sigma[i]==tau[i] for i in good),j) for tau in taus)
                predicted=Fraction(len(taus)*falling(u,j), falling(den,j))
                assert actual==predicted,(n,sigma,T,j,actual,predicted)
            for tau in taus:
                m=sum(sigma[i]==tau[i] for i in range(n))
                dot=n-s-t+m
                d1=2*(n-s);d2=2*(n-t)
                hist[(s,t,m)]+=1
                assert dot>=0
                # The Frobenius inner product of both actual edge matrices.
                direct=0
                for i in range(n):
                    for j in range(n):
                        direct+=(int(j==sigma[i])-int(j==i))*(int(j==tau[i])-int(j==i))
                assert direct==dot
                assert dot*dot<=d1*d2
    assert sum(hist.values())==len(perms)**2
    print('EXACT_PASS n=%s degree=%s ordered_pairs=%s distinct_triples=%s' % (n,len(perms),len(perms)**2,len(hist)))
    return hist


def sample_cycle(n,rng):
    weights=[1/(factorial(s)*(n-s)) for s in range(n-1)]
    total=sum(weights); x=rng.random()*total; s=0
    while x>weights[s]:x-=weights[s];s+=1
    perm=list(range(n)); vals=list(range(n));rng.shuffle(vals)
    moving=vals[s:]
    for k,i in enumerate(moving):perm[i]=moving[(k+1)%len(moving)]
    return perm,s


def approximate(n=100, trials=35000):
    rng=Random(20261115)
    moments=[0.0]*3; moments2=[0.0]*3; cross=[[0.0]*3 for _ in range(3)]
    zsum=0.0; z2sum=0.0
    for _ in range(trials):
        sig,s=sample_cycle(n,rng);tau,t=sample_cycle(n,rng)
        m=sum(a==b for a,b in zip(sig,tau))
        vals=[s,t,m]
        z=(s+t-2*m)/(2*sqrt(3))
        zsum+=z/trials;z2sum+=z*z/trials
        cos=(n-s-t+m)/(2*sqrt((n-s)*(n-t)))
        fluct=n*(cos-0.5)
        assert abs(fluct-(2*m-s-t)/4)<0.2,(fluct,s,t,m)
        for i in range(3):
            moments[i]+=vals[i]/trials
            moments2[i]+=vals[i]**2/trials
            for j in range(3):cross[i][j]+=vals[i]*vals[j]/trials
    cov=[[cross[i][j]-moments[i]*moments[j] for j in range(3)] for i in range(3)]
    assert all(abs(x-1)<0.05 for x in moments),(moments,cov)
    assert abs(z2sum-zsum*zsum-0.5)<0.07,(zsum,z2sum)
    assert all(abs(cov[i][j])<0.08 for i in range(3) for j in range(3) if i!=j),(moments,cov)
    print('ASYMPTOTIC_SANITY_PASS n=%s trials=%s means=%s offdiagonal_cov=%s' % (n,trials,[round(x,4) for x in moments],[round(cov[i][j],4) for i in range(3) for j in range(i)]))
    print('ANGLE_LIMIT_VARIANCE_SANITY_PASS empirical=%0.4f target=0.5' % (z2sum-zsum*zsum))


if __name__=='__main__':
    for n in range(3,7):check_small(n)
    approximate()
    print('BIRKHOFF_LOCAL_ANGLE_EXACT_PASS')
