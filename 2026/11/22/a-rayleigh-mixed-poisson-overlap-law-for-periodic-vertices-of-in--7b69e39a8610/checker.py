"""Exact small-size checks for intersections of cyclic sets of independent uniform maps."""
from itertools import product
from collections import Counter
from fractions import Fraction
from math import comb, factorial, sqrt, pi


def cyclic_mask(f):
    n=len(f); bits=0
    for v in range(n):
        p=v; seen=set()
        while p not in seen:
            seen.add(p); p=f[p]
        if p==v: bits |= 1<<v
    return bits


def cyclic_size_prob(n,k):
    t=1
    for j in range(k): t*=n-j
    return Fraction(k*t,n**(k+1))


def overlap_distribution(n):
    out=Counter()
    for a in range(1,n+1):
        for b in range(1,n+1):
            weight=cyclic_size_prob(n,a)*cyclic_size_prob(n,b)
            for z in range(max(0,a+b-n),min(a,b)+1):
                out[z]+=weight*Fraction(comb(a,z)*comb(n-a,b-z),comb(n,b))
    return out


def enumerate_mapping_masks(n):
    return Counter(cyclic_mask(f) for f in product(range(n),repeat=n))

checks=0
for n in range(1,6):
    hist=enumerate_mapping_masks(n)
    assert sum(hist.values())==n**n
    for mask,count in hist.items():
        k=mask.bit_count()
        expected=factorial(k)*(k if k<n else 1)*n**(n-k-1 if k<n else 0)
        assert count==expected,(n,mask,count,expected)
        checks+=1
    for k in range(1,n+1):
        actual=Fraction(sum(v for mask,v in hist.items() if mask.bit_count()==k),n**n)
        assert actual==cyclic_size_prob(n,k)
        checks+=1
    out=overlap_distribution(n)
    brute=Counter()
    for a,ca in hist.items():
        for b,cb in hist.items():
            brute[(a&b).bit_count()]+=ca*cb
    for z in range(n+1):
        assert out[z]==Fraction(brute[z],n**(2*n)),(n,z)
        checks+=1
    mean=sum(Fraction(k)*cyclic_size_prob(n,k) for k in range(1,n+1))
    var=sum(Fraction(k*k)*cyclic_size_prob(n,k) for k in range(1,n+1))-mean*mean
    first=sum(Fraction(z)*p for z,p in out.items())
    assert first==mean*mean/n
    checks+=1
    # Three independent maps: compare exact edge-overlap covariance two ways.
    # Conditional on cyclic set S1, the others independently overlap S1.
    e_joint=sum(Fraction(ca*cb*cc*(a&b).bit_count()*(a&ccmask).bit_count(),n**(3*n))
                for a,ca in hist.items() for b,cb in hist.items() for ccmask,cc in hist.items())
    assert e_joint-first*first==var*mean*mean/n**2
    checks+=1
    print('n',n,'number_masks',len(hist),'P(no common)',out[0], 'mean overlap',first)
print('EXACT_ASSERTIONS',checks)

# Numerical P0 from exact size probabilities and disjoint-subset factor.
def pzero_float(n):
    p=[0.0]*(n+1);p[1]=1.0/n
    for k in range(2,n+1): p[k]=p[k-1]*(k/(k-1))*((n-k+1)/n)
    # stable disjoint probability via recurrence in b
    total=0.0
    for a in range(1,n+1):
        q=1.0
        for b in range(1,n-a+1):
            q*= (n-a-b+1)/(n-b+1)
            total+=p[a]*p[b]*q
    return total
for n in (10,30,100,300):
    v=pzero_float(n)
    print('asymptotic n',n,'Pzero',round(v,9),'limit',1/3,'difference',round(v-1/3,9))
print('Rayleigh mean^2',pi/2,'limiting adjacent-edge covariance',pi-pi*pi/4)
