from itertools import product
from math import gcd
from collections import Counter
from itertools import combinations
import cmath

# Independent implementations: exact exponent congruences versus complex direct DFT.
def exact_modular(q,a,b):
    aa=(0,)+a; bb=(0,)+b
    m=0
    for x in range(3):
        r=[(aa[t]-bb[(t-x)%3])%q for t in range(3)]
        # A triple is a scalar cube-root character iff it is a geometric progression and ratio cube root.
        if (r[0]+r[2]-2*r[1])%q==0 and (3*(r[1]-r[0]))%q==0: m+=1
    return m

def direct_dft(q,a,b):
    f=[1]+[cmath.exp(2j*cmath.pi*v/q) for v in a]
    g=[1]+[cmath.exp(2j*cmath.pi*v/q) for v in b]
    w=cmath.exp(-2j*cmath.pi/3)
    s=0
    for x in range(3):
        for k in range(3):
            z=sum(f[t]*g[(t-x)%3].conjugate()*w**(k*t) for t in range(3))
            if abs(z)>1e-7:s+=1
    return s

def torus_memberships(q, a, b):
    assert q % 3 == 0
    aa=(0,)+a; bb=(0,)+b
    labels=[]
    for x in range(3):
        r=[(aa[t]-bb[(t-x)%3])%q for t in range(3)]
        for j in range(3):
            if all((r[t]-r[0]-(q//3)*j*t)%q==0 for t in range(3)):
                labels.append((x,j))
    return labels

for q in [2,3,4,6,9,12]:
    d=gcd(3,q); triple=27 if d==3 else 1
    expect={k:v for k,v in {3:triple,7:3*d*q*q-3*triple,9:q**4-3*d*q*q+2*triple}.items() if v>0}
    hist=Counter()
    strata={(x,j):set() for x in range(3) for j in range(3)} if q%3==0 else None
    for a in product(range(q),repeat=2):
        for b in product(range(q),repeat=2):
            m=exact_modular(q,a,b)
            s=direct_dft(q,a,b)
            assert s==9-2*m,(q,a,b,m,s)
            hist[s]+=1
            if strata is not None:
                labels=torus_memberships(q,a,b)
                assert len(labels)==m
                for label in labels:strata[label].add((a,b))
    assert dict(hist)==expect,(q,dict(hist),expect)
    if strata is not None:
        assert all(len(v)==q*q for v in strata.values())
        for (xa,A),(xb,B) in combinations(strata.items(),2):
            assert len(A&B)==(0 if xa[0]==xb[0] else 3)
    print(q,dict(sorted(hist.items())), 'PASS')
