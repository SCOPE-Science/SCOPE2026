#!/usr/bin/env python3
"""Independent checks of hard-core two-activity wheel root-collision theorem.
No external data or runtime state is required; Python 3 and sympy suffice.
This finite computation supplements, but does not replace, the all-size proof.
"""
from fractions import Fraction
from math import comb, cos, pi, floor
import sympy as s
z=s.Symbol('z')

def cycle_enumerate(n):
    out=[0]*(n//2+1)
    for bits in range(1<<n):
        if bits & (((bits<<1)|(bits>>(n-1))) & ((1<<n)-1)):
            continue
        out[bits.bit_count()]+=1
    return s.Poly(sum(c*z**j for j,c in enumerate(out)),z)

def cycle_formula(n):
    return s.Poly(sum(n*s.binomial(n-k,k)/s.Integer(n-k)*z**k for k in range(n//2+1)),z)

def threshold(n,j):
    return 2.**(1-n)/cos((2*j-1)*pi/(n-1))**(n-1)

for n in range(4,15):
    P=cycle_enumerate(n)
    assert P==cycle_formula(n),('combinatorial identity',n)
    d=n//2
    tstar=[threshold(n,j) for j in range(1,d//2+1)]
    assert all(a<b for a,b in zip(tstar,tstar[1:]))
    # Exact Sturm counts for rational fugacities strictly away from thresholds.
    probes=[s.Rational(0)]
    if tstar:
        probes.append(s.Rational(str(tstar[0]/2)))
        probes += [s.Rational(str((a+b)/2)) for a,b in zip(tstar,tstar[1:])]
        probes.append(s.Rational(str(tstar[-1]*2)))
    for tt in probes:
        observed=P.add(s.Poly(tt,z)).count_roots(-s.oo,0)
        predicted=d-2*sum(float(tt)>t for t in tstar)
        assert observed==predicted,(n,str(tt),observed,predicted)
    # Analytic derivative critical points and negative critical values.
    for k in range(1,d):
        a=k*pi/(n-1)
        zz=-1/(4*cos(a)**2)
        value=float(P.eval(zz))
        ideal=(-1.)**k*2.**(1-n)/cos(a)**(n-1)
        assert abs(value-ideal)<=1e-7*max(1,abs(ideal)),(n,k,value,ideal)
    print('n',n,'degree',d,'collision_thresholds',len(tstar),'probes',len(probes),'PASS')

# Critical double root at exactly rational thresholds n=4,5,7.
for n,tt in [(4,s.Rational(1)),(5,s.Rational(1,4)),(7,s.Rational(1,27))]:
    P=cycle_formula(n).as_expr()+tt
    common=s.gcd(s.Poly(P,z),s.Poly(s.diff(P,z),z))
    assert common.degree()==1,(n,common)
    assert s.degree(s.gcd(common,s.Poly(s.diff(P,z,2),z)))==0
    print('exact_double_root',n,'factor',s.factor(common.as_expr()),'PASS')
print('WHEEL_ZERO_CENSUS_CHECKS_PASSED')
