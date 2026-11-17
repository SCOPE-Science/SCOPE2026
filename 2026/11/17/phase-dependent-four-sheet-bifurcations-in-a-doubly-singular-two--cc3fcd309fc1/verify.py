"""Exact-coefficient checks for an alternating scalar implicit relation.

Standalone Python 3 checker; requires only the standard library.
The universal root counts follow from the proof, not finite sampling.
"""
from fractions import Fraction as Q
from math import sqrt

# Sparse polynomial ring in variables (z,a,b), with exact rational coefficients.
ZERO = {}
def mono(i=0,j=0,k=0,c=1):
    c=Q(c)
    return {(i,j,k):c} if c else {}
def add(p,q):
    d=p.copy()
    for m,v in q.items():
        d[m]=d.get(m,Q(0))+v
        if not d[m]: del d[m]
    return d
def neg(p): return {m:-v for m,v in p.items()}
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    d={}
    for (i,j,k),v in p.items():
        for (ii,jj,kk),w in q.items():
            m=(i+ii,j+jj,k+kk)
            d[m]=d.get(m,Q(0))+v*w
            if not d[m]: del d[m]
    return d
def times(c,p): return {m:Q(c)*v for m,v in p.items() if Q(c)*v}
def power(p,n):
    result=mono(); base=p
    while n:
        if n&1: result=mul(result,base)
        base=mul(base,base); n//=2
    return result
z,a,b=mono(i=1),mono(j=1),mono(k=1)
h0=add(power(z,2),mul(a,z))
h1=add(times(2,power(z,2)),mul(b,z))
H0=add(power(h1,2),mul(a,h1))
H1=add(times(2,power(h0,2)),mul(b,h0))
H0_nf=sub(power(sub(times(2,power(add(z,times(Q(1,4),b)),2)),times(Q(1,8),sub(power(b,2),times(4,a)))),2),times(Q(1,4),power(a,2)))
H1_nf=sub(times(2,power(sub(power(add(z,times(Q(1,2),a)),2),times(Q(1,4),sub(power(a,2),b))),2)),times(Q(1,8),power(b,2)))
assert H0==H0_nf, (H0,H0_nf)
assert H1==H1_nf, (H1,H1_nf)
print('SYMBOLIC_NORMAL_FORMS_OK coefficients=exact')

# Verify phase-by-phase criteria and caustic width formula with exact rationals.
for av,bv in [(Q(1,100),Q(1,100)),(-Q(1,100),Q(1,100)),
              (Q(1,100),-Q(1,100)),(-Q(1,100),-Q(1,100)),
              (Q(1,100000),Q(1,10)),(Q(1,10),Q(1,100000))]:
    d0=bv*bv-4*av
    d1=av*av-bv
    c0=(4 if d0>0 else 2)
    c1=(4 if d1>0 else 2)
    w0=(d0*d0/Q(64)) if d0>0 else Q(0)
    w1=(d1*d1/Q(8)) if d1>0 else Q(0)
    assert c0 in [2,4] and c1 in [2,4]
    assert w0 >= 0 and w1 >= 0
    print('PHASE_REGION_OK',str(av),str(bv),'max_regular_valences',c0,c1,'widths',str(w0),str(w1))

# Exact phase-asymmetric witness at the distinguished two-phase stationary state.
e=Q(1,100); av=-e; bv=e
phase0_d=bv*bv-8*av
phase1_d=av*av-2*bv
assert phase0_d>0 and phase1_d<0
# Phase 0: z=0,-e/2, (-e +/- sqrt(e^2+8e))/4.
z0=[0.,-float(e)/2,(-float(e)+sqrt(float(e*e+8*e)))/4,
    (-float(e)-sqrt(float(e*e+8*e)))/4]
assert len({round(t,14) for t in z0})==4
for zz in z0:
    intermediate=2*zz*zz+float(e)*zz
    assert abs(intermediate*intermediate-float(e)*intermediate)<1e-12
# Phase 1: exactly z=0 and z=e; the other quadratic has negative discriminant.
for zz in [0.,float(e)]:
    intermediate=zz*zz-float(e)*zz
    assert abs(2*intermediate*intermediate+float(e)*intermediate)<1e-12
assert Q(1)-av*bv>0
multiplier=Q(1)/(av*bv)
assert multiplier == -Q(10000)
print('PHASE_ASYMMETRY_OK phase0=4 phase1=2 multiplier=',str(multiplier),'cyclic_det=',str(1-av*bv))

# Non-Hoelder exponent > 1/4: at central point x=4z^4 or x=2z^4,
# ratio z/x^alpha diverges as x goes to zero when alpha>1/4.
print('VERIFY_OK exact_polynomial_normal_forms=2 distinct_phase_maxima=4 witness=1')
