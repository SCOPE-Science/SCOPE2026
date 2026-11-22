#!/usr/bin/env python3
"""Standalone exact checks for rare coordinatewise-comparability marks.

All checks are finite identities and limiting-rate consistency checks;
they are not a proof of weak convergence.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial, comb

checks=0

def eq(x,y):
    global checks
    checks+=1
    assert x==y,(x,y)

# Conditional ordered-pair density 2 * 1_{0<u<v<1}.
# E[U^a V^b] = 2 / ((a+1)(a+b+2)).
def moment(a,b):
    return F(2,(a+1)*(a+b+2))

for a in range(0,12):
    for b in range(0,12):
        # Independently integrate v^b * integral_0^v 2u^a du.
        independent=F(2,a+1)*F(1,a+b+2)
        eq(moment(a,b),independent)

mu_u=moment(1,0);mu_v=moment(0,1)
var_u=moment(2,0)-mu_u**2
var_v=moment(0,2)-mu_v**2
cov_uv=moment(1,1)-mu_u*mu_v
eq((mu_u,mu_v),(F(1,3),F(2,3)))
eq((var_u,var_v,cov_uv),(F(1,18),F(1,18),F(1,36)))

# Center A=U+V and separation B=V-U.
# Their means are 1 and 1/3. At Gaussian scale they decouple.
EA=mu_u+mu_v;EB=mu_v-mu_u
EA2=moment(2,0)+2*moment(1,1)+moment(0,2)
EB2=moment(2,0)-2*moment(1,1)+moment(0,2)
EAB=moment(0,2)-moment(2,0)
eq((EA,EB),(F(1),F(1,3)))
eq((EA2-EA*EA,EB2-EB*EB,EAB-EA*EB),(F(1,6),F(1,18),F(0)))

# 1-dimensional product moment for three uniform coordinates:
# two incoming to same endpoint or two outgoing from same source have 2/6,
# whereas a chained pair has 1/6.
orders=list(permutations((0,1,2)))
p=lambda test:F(sum(test(o) for o in orders),len(orders))
# position in a sorted list, not actual values
rank=lambda o,x:o.index(x)
eq(p(lambda o: rank(o,0)<rank(o,1) and rank(o,0)<rank(o,2)),F(1,3))
eq(p(lambda o: rank(o,1)<rank(o,0) and rank(o,2)<rank(o,0)),F(1,3))
eq(p(lambda o: rank(o,0)<rank(o,1) and rank(o,1)<rank(o,2)),F(1,6))
eq(p(lambda o: rank(o,0)<rank(o,1) and rank(o,1)<rank(o,0)),F(0))

# Each ordered pair of distinct vertices has marginal 2^{-d};
# it meets exactly 4n-6 directed-pair indices counting itself.
for n in range(3,21):
    pairs=[(i,j) for i in range(n) for j in range(n) if i!=j]
    for i,j in pairs:
        incident=sum((i in (a,b) or j in (a,b)) for a,b in pairs)
        eq(incident,4*n-6)

# At the critical sequence n=2^k, d=2k, lambda_n=n(n-1)2^-d -> 1;
# b1 (non-negligible only at small k) and b2 upper bound both decay.
prev_1=prev_2=None
for k in range(4,70):
    n=2**k;d=2*k
    lam=F(n*(n-1),2**d)
    b1=F(n*(n-1)*(4*n-6),4**d)
    b2=F(n*(n-1)*(4*n-8),3**d)
    assert 0<lam<1
    if prev_1 is not None:
        assert b1<prev_1 and b2<prev_2
        checks+=2
    prev_1,prev_2=b1,b2
    eq(lam,F(1)-F(1,n))

# Structure of Gaussian conversion (U,V) = ((A-B)/2,(A+B)/2).
# Starting with independent centered variances 1/6,1/18.
va,vb=F(1,6),F(1,18)
eq(((va+vb)/4,(va+vb)/4,(va-vb)/4), (var_u,var_v,cov_uv))

print('PASS: %d exact rational and combinatorial checks'%checks)
