"""Exact algebra and independent finite-sample checks for broken quadratic L2 projection BV gain.

Requires Python 3 with sympy. Run: python CHECKER.py
Finite tests supplement the proof; they do not certify its universal quantifiers.
"""
import math
import random
import sympy as S

z, t = S.symbols('z t', real=True)
u = t * (1-t)
P = S.expand((1-t)+3*u*(2*z-1)+5*u*(2*t-1)*(6*z*z-6*z+1))
P0 = S.factor(P.subs(z,0)); P1 = S.factor(P.subs(z,1))
xc = S.factor((5*t-3)/(5*(2*t-1)))
PM = S.factor(P.subs(z,xc))
alpha=(4-S.sqrt(6))/10; beta=(6-S.sqrt(6))/10
F_left=S.factor(1+2*(PM-P1))
F_center=S.factor(1+2*(PM-P0-P1))
F_right=S.factor(2*(PM-P0)-1)
F_monotone=S.factor(2*(P1-P0)-1)
expected_center=(500*t**4-1000*t**3+648*t**2-148*t+5)/(5*(2*t-1))
assert S.simplify(F_center-expected_center)==0
assert S.simplify(S.diff(F_center,t)-6*(500*t**4-1000*t**3+716*t**2-216*t+23)/(5*(2*t-1)**2))==0
assert S.simplify(S.diff(F_left,t)-12*(3*t-2)*(5*t-2)*(10*t**2-8*t+1)/(5*(2*t-1)**2))==0
assert S.simplify(S.diff(F_right,t)-12*(3*t-1)*(5*t-3)*(10*t**2-12*t+3)/(5*(2*t-1)**2))==0
assert S.simplify(F_monotone-(12*t*(1-t)-1))==0
for L in (1,2*z-1,6*z*z-6*z+1):
    assert S.simplify(S.integrate(P*L,(z,0,1))-S.integrate(L,(z,t,1)))==0
root=(1-S.sqrt((17+2*S.sqrt(41))/125))/2
assert S.simplify(500*(root*(1-root))**2-216*(root*(1-root))+23)==0
K=float(F_center.subs(t,root).evalf(30))
assert 0.25584 < float(root) < 0.25585
assert 2.06983 < K < 2.06985
assert S.simplify(F_center.subs(t,S.Rational(1,4))-S.Rational(331,160))==0
print('EXACT_PROJECTION_MOMENTS_AND_PIECEWISE_DERIVATIVES_PASS')

# Independent numerical variation of a reference-cell projected step.
def step_projector(s):
    if s<=0: return (1., 0., 0.)
    if s>=1: return (0., 0., 0.)
    w=s*(1-s)
    # Polynomial c0 + c1*x + c2*x^2.
    A=5*w*(2*s-1)
    return (1-s-3*w+A, 6*w-6*A, 6*A)

def poly_var(c):
    a,b,d=c
    xs=[0.,1.]
    if abs(d)>1e-14:
        stationary=-b/(2*d)
        if 0<stationary<1: xs.insert(1,stationary)
    vals=[a+b*x+d*x*x for x in xs]
    return sum(abs(y-x) for x,y in zip(vals,vals[1:]))

def full_var(jumps, n_cells):
    cs=[]
    for i in range(n_cells):
        coeff=[0.,0.,0.]
        for location,amplitude in jumps:
            d=step_projector(location-i)
            for j in range(3): coeff[j]+=amplitude*d[j]
        cs.append(coeff)
    total=sum(poly_var(c) for c in cs)
    for left,right in zip(cs,cs[1:]):
        total+=abs((left[0]+left[1]+left[2])-right[0])
    total+=abs(cs[0][0])+abs(sum(cs[-1]))
    return total

s=float(root.evalf(30))
for n in (4,6,9,13):
    # Plateau with jumps in two separate cells; zero outside.
    data=[(s,1.),(n-2+s,-1.)]
    tv=full_var(data,n)
    assert abs(tv/2-K)<1e-10, (tv/2,K)
print('OFFCENTRE_PLATEAU_EXACT_SHARPNESS_NUMERIC_PASS')

rng=random.Random(10517)
for trial in range(3000):
    count=rng.randint(2,9)
    coords=sorted(rng.uniform(1,10) for _ in range(count))
    amps=[rng.uniform(-2,2) for _ in range(count-1)]
    amps.append(-sum(amps))
    assert abs(sum(amps))<1e-12
    jumps=list(zip(coords,amps))
    vin=sum(abs(a) for a in amps)
    vout=full_var(jumps,12)
    assert vout<=K*vin+1e-8, (trial,vin,vout)
print('RANDOM_PIECEWISE_CONSTANT_INPUTS_BV_STRESS_PASS 3000')
print('ALL_BROKEN_QUADRATIC_BV_CHECKS_PASS')
