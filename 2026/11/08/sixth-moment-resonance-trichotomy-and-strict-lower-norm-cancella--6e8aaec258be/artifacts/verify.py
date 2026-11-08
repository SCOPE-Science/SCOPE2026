#!/usr/bin/env python3
"""Exact rational checks for the two-tone sixth-moment theorem.

No dependencies beyond Python 3's standard library are required.
"""
from fractions import Fraction as Q
from math import comb
from collections import defaultdict

# Polynomial in two real amplitudes and two symbolic phase exponents.
# A signed frequency is a pair (integer t-frequency, integer phase frequency).
def moment(m,n):
    f={(m,0,1,0): Q(1,2), (-m,0,1,0): Q(1,2),
       (n,1,0,1):Q(1,2),(-n,-1,0,1):Q(1,2)}
    g={(0,0,0,0):Q(1)}
    for _ in range(6):
        h=defaultdict(Q)
        for (w,p,a,b),c in g.items():
            for (v,q,d,e),t in f.items():
                h[(w+v,p+q,a+d,b+e)]+=c*t
        g=h
    return {(p,a,b):c for (w,p,a,b),c in g.items() if w==0 and c}

base={(0,6,0):Q(5,16),(0,4,2):Q(45,16),
      (0,2,4):Q(45,16),(0,0,6):Q(5,16)}
extra={
  2:{(2,4,2):Q(15,64),(-2,4,2):Q(15,64)},
  3:{(1,5,1):Q(15,32),(-1,5,1):Q(15,32),
     (1,3,3):Q(15,16),(-1,3,3):Q(15,16)},
  5:{(1,5,1):Q(3,32),(-1,5,1):Q(3,32)}
}
for n in range(2,51):
    expected=base | extra.get(n,{})
    # Collision between equal keys cannot arise for these supports.
    assert moment(1,n)==expected, (n, moment(1,n), expected)
print('EXACT_FOURIER_SIXTH_MOMENT_CLASSIFICATION_OK 2..50')

# For derivative checks, polynomials are represented in ascending order.
def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def der(a):return [(i+1)*a[i+1] for i in range(len(a)-1)]
def sub(a,b):
    n=max(len(a),len(b))
    return [(a[i] if i<len(a) else Q(0))-(b[i] if i<len(b) else Q(0)) for i in range(n)]
def eqpoly(a,b):return all(x==0 for x in sub(a,b))
def val(a,x):return sum(v*x**i for i,v in enumerate(a))

denom=mul(mul([Q(1),Q(0),Q(1)],[Q(1),Q(0),Q(1)]),[Q(1),Q(0),Q(1)])
for n,sg,np,qpoly,pref in [
(2,1,[Q(10),0,Q(105),0,Q(90),0,Q(10)], [Q(-5),0,Q(2),0,Q(4)], Q(-15,2)),
(3,-1,[Q(5,2),Q(-15,2),Q(45,2),Q(-15),Q(45,2),0,Q(5,2)], [Q(1),-4,1,0,-6,4],Q(-15,2)),
(3,1,[Q(5,2),Q(15,2),Q(45,2),Q(15),Q(45,2),0,Q(5,2)], [Q(-1),-4,-1,0,6,4],Q(-15,2)),
(5,-1,[Q(5,2),Q(-3,2),Q(45,2),0,Q(45,2),0,Q(5,2)], [Q(1),-20,-5,0,0,20],Q(-3,2)),
(5,1,[Q(5,2),Q(3,2),Q(45,2),0,Q(45,2),0,Q(5,2)], [Q(-1),-20,5,0,0,20],Q(-3,2)),
]:
    if n==2:
        # numerator of K_2^+: (10t^6 +90t^4+105t^2+10)/(4(1+t^2)^3)
        numerator=[x/Q(4) for x in np]
        factor=[Q(0)]+qpoly
    else:
        numerator=np
        factor=qpoly
    lhs=sub(mul(der(numerator),denom),mul(numerator,der(denom)))
    rhs=mul([pref*x for x in factor],mul(mul([Q(1),0,Q(1)],[Q(1),0,Q(1)]),[Q(1),0,Q(1)]))
    # f'=pref * factor /(1+t^2)^4 ; multiplying by denom**2 gives pref*factor*(1+t^2)^2
    rhs=mul([pref*x for x in factor],mul([Q(1),0,Q(1)],[Q(1),0,Q(1)]))
    assert eqpoly(lhs,rhs),(n,sg,sub(lhs,rhs))
print('EXACT_CRITICAL_QUINTIC_DERIVATIVES_OK')

p3m=[Q(1),-4,1,0,-6,4]
p3p=[Q(-1),-4,-1,0,6,4]
p5m=[Q(1),-20,-5,0,0,20]
p5p=[Q(-1),-20,5,0,0,20]
for p,lo,hi in [(p3m,Q(26,100),Q(27,100)),
                 (p3m,Q(160,100),Q(162,100)),
                 (p3p,Q(86,100),Q(87,100)),
                 (p5m,Q(49,1000),Q(50,1000)),
                 (p5m,Q(104,100),Q(106,100)),
                 (p5p,Q(95,100),Q(96,100))]:
    assert val(p,lo)*val(p,hi)<0, (p,lo,hi)
print('EXACT_RATIONAL_ROOT_BRACKETS_OK')

# Independent rational zero-frequency convolution: for integer amplitudes
# at zero relative phase, sum the exactly enumerated signs and compare formula.
for n in range(2,13):
    for a,b in [(1,0),(0,1),(1,1),(2,1),(-3,2),(2,-4)]:
        mom=sum(c*Q(a)**p*Q(b)**q for (phase,p,q),c in moment(1,n).items())
        baseline=Q(5,16)*(a**6+b**6)+Q(45,16)*(a**4*b*b+a*a*b**4)
        correction={2:Q(15,32)*a**4*b*b,
                    3:Q(15,16)*a**5*b+Q(15,8)*a**3*b**3,
                    5:Q(3,16)*a**5*b}.get(n,Q(0))
        assert mom==baseline+correction
print('INDEPENDENT_RATIONAL_MOMENT_WITNESSES_OK')
print('ALL_TWO_TONE_SIXTH_MOMENT_CHECKS_PASSED')
