"""Exact rational tests for minimum enclosing spheres of symmetric one-cut boxes."""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def geometry(n, tau):
    q = tau.numerator // tau.denominator
    s = tau - q
    low = min(F(q,n), F(1,2))
    high = min(tau/n,F(1,2))
    a = min(high,max(low,s/2))
    ri = n*a*a + q*(1-2*a)
    rf = n*a*a + q+s*s-2*(q+s)*a if s else ri
    return a,max(ri,rf)


def vertices(n,tau):
    q=tau.numerator//tau.denominator
    s=tau-q
    for k in range(q+1):
        for S in combinations(range(n),k):
            v=[F(0)]*n
            for j in S:v[j]=F(1)
            yield tuple(v)
    if s:
        for S in combinations(range(n),q):
            outside=set(range(n))-set(S)
            for j in outside:
                v=[F(0)]*n
                for i in S:v[i]=F(1)
                v[j]=s
                yield tuple(v)


def check():
    assertions=0
    examples=0
    for n in range(3,9):
      for q in range(n+1):
       fracs=[F(0)] if q==n else [F(0),F(1,12),F(1,6),F(1,4),F(1,3),F(2,5),F(1,2),F(3,5),F(2,3),F(3,4),F(5,6),F(11,12)]
       fracs+=([F(2*q,n),F(2*q,n-2)] if q<n and q else [])
       for s in set(f for f in fracs if 0<=f<1):
        tau=F(q)+s
        if tau==0:continue
        a,R2=geometry(n,tau)
        vs=list(vertices(n,tau))
        assert vs
        ds=[sum((x-a)**2 for x in v) for v in vs]
        assert max(ds)==R2
        assertions+=1
        for d in ds:
            assert d<=R2
            assertions+=1
        contacts=[v for v,d in zip(vs,ds) if d==R2]
        if a==F(1,2):
            ccount=sum(comb(n,k) for k in range(q+1))
        elif s==0:
            ccount=comb(n,q)
        else:
            ccount=(comb(n,q)*(n-q) if a<s/2 else
                    comb(n,q) if a>s/2 else comb(n,q)*(n-q+1))
        assert len(contacts)==ccount
        assertions+=1
        # The center must be a convex combination of the contact-layer barycenters.
        if a==F(1,2):
            # 1/2 lies in the convex hull of 0/1 layers of ranks 0,...,q.
            assert q>=F(n,2)
        elif s==0 or a>s/2:
            assert a==F(q,n)
        elif a<s/2:
            assert a==tau/n
        else:
            assert F(q,n)<=a<=tau/n
        assertions+=1
        # An independent exact inequality against the two orbit profiles.
        for c in [F(0),F(1,2),s/2,F(q,n),tau/n,a]:
            if 0<=c<=F(1,2):
                d=max(sum((x-c)**2 for x in v) for v in vs)
                assert d>=R2
                assertions+=1
        examples+=1
    n,tau=5,F(8,5)
    a,r=geometry(n,tau)
    assert (a,r)==(F(3,10),F(17,20))
    assert sum(sum((x-a)**2 for x in v)==r for v in vertices(n,tau))==25
    print('PASS',examples,'parameter instances,',assertions+2,'exact rational assertions; transition n=5 tau=8/5 has 25 contacts')
if __name__=='__main__':check()
