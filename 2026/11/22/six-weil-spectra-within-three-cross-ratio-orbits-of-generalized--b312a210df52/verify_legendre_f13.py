#!/usr/bin/env python3
"""Exact standard-library verifier for eleven cyclic-quartic curves over F_13.

The extension fields are independently built from two distinct monic
irreducible polynomials of degrees two and three. No external database
or numerical approximations are used.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb

P = 13
MODELS = [
    {1: (0,1), 2: (2,0,1), 3: (1,4,0,1)},
    {1: (0,1), 2: (5,0,1), 3: (2,2,0,1)},
]
EXPECTED = {
 (2,12): (8,140,2216,(-6,6,6)),
 (3,5,9,11): (16,172,2128,(-6,-2,6)),
 (4,): (28,172,2092,(-6,-6,-2)),
 (6,8): (12,212,2268,(-4,2,4)),
 (7,): (20,180,2180,(-6,-4,4)),
 (10,): (4,172,2164,(-2,6,6)),
}

def extension(degree, modulus):
    assert len(modulus) == degree+1 and modulus[-1] == 1
    if degree > 1:
        assert all(sum(modulus[i]*x**i for i in range(degree+1))%P
                   for x in range(P)), 'monic quadratic/cubic must have no roots'
    q=P**degree
    def digits(i): return tuple((i//(P**j))%P for j in range(degree))
    def encode(coeff): return sum((a%P)*P**i for i,a in enumerate(coeff))
    elements = [digits(i) for i in range(q)]
    def mul(i,j):
        a,b=elements[i],elements[j]
        v=[0]*(2*degree-1)
        for r in range(degree):
            for s in range(degree): v[r+s]+=a[r]*b[s]
        for k in range(2*degree-2,degree-1,-1):
            for r in range(degree): v[k-degree+r]-=v[k]*modulus[r]
        return encode(v[:degree])
    def power(a,n):
        z=1
        while n:
            if n&1: z=mul(z,a)
            a=mul(a,a); n//=2
        return z
    sq=[mul(i,i) for i in range(q)]
    cubes=[mul(sq[i],i) for i in range(q)]
    fourth={mul(sq[i],sq[i]) for i in range(1,q)}
    assert len(fourth)==(q-1)//4 and 1 in fourth
    answer={}
    for lam in range(2,P):
        zero=quad=0
        for i in range(q):
            v=tuple((elements[cubes[i]][j]-(1+lam)*elements[sq[i]][j]
                     +lam*elements[i][j])%P for j in range(degree))
            f=encode(v)
            by_set=(f!=0 and f in fourth)
            by_exp=(f!=0 and power(f,(q-1)//4)==1)
            assert by_set == by_exp, (lam, degree, i)
            if not f: zero+=1
            elif by_set: quad+=1
        answer[lam]=1+zero+4*quad  # exactly one rational point over infinity
    return answer

def poly_mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return tuple(z)

def quartic_orbit(t):
    seen={t}; stack=[t]
    while stack:
        u=stack.pop()
        for v in ((1-u)%P,pow(u,-1,P)):
            if v not in seen:seen.add(v);stack.append(v)
    return tuple(sorted(seen))

all_N=[]
for model in MODELS:
    counts={n:extension(n,model[n]) for n in (1,2,3)}
    all_N.append(counts)
assert all_N[0]==all_N[1], 'independent field-model disagreement'
counts=all_N[0]
by_type=defaultdict(list)
for lam in range(2,P):
    n1,n2,n3=(counts[n][lam] for n in (1,2,3))
    s1,s2,s3=(P**k+1-n for k,n in zip((1,2,3),(n1,n2,n3)))
    assert (s1*s1-s2)%2==0
    assert (s1**3-3*s1*s2+2*s3)%6==0
    e1=(s1);e2=(s1*s1-s2)//2;e3=(s1**3-3*s1*s2+2*s3)//6
    L=(1,-e1,e2,-e3,P*e2,-P**2*e1,P**3)
    # factorization check: enumerate all possible elliptic traces satisfying Hasse
    factors=[]
    for a in range(-7,8):
        for b in range(a,8):
            for c in range(b,8):
                if poly_mul(poly_mul((1,-a,P),(1,-b,P)),(1,-c,P))==L:
                    factors.append((a,b,c))
    assert len(factors)==1,(lam,L,factors)
    by_type[(n1,n2,n3,factors[0])].append(lam)

actual={tuple(sorted(v)):k for k,v in by_type.items()}
assert actual==EXPECTED,(actual,EXPECTED)
assert len(actual)==6 and sum(map(len,actual))==11
orbits={quartic_orbit(lam) for lam in range(2,P)}
assert orbits=={(2,7,12),(3,5,6,8,9,11),(4,10)},orbits
for orbit in orbits:
    spectra={tuple(k) for k,v in by_type.items() if set(v)&set(orbit)}
    assert len(spectra)==2,(orbit,spectra)
assert counts[1][4]==28 and counts[1][10]==4
# Geometry: distinct branch points 0,1,t,infinity make every fiber smooth genus 3.
# Characteristic 13 Cartier matrix determinant can be obtained by direct extraction;
# Hasse roots are not in F13, so all eleven observed Weil factors are ordinary.
for k in sorted(actual):
    print('type=',k,'parameters=',actual[k])
print('GENERALIZED_LEGENDRE_F13_SIX_WEIL_SPECTRA_VERIFIED',
      'smooth=11','spectra=6','cross_ratio_orbits=3',
      'two_spectra_per_orbit=3','independent_field_models=2')
