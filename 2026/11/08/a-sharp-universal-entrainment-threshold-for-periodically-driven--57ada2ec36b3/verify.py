"""Auxiliary diagnostic calculations for a forced two-strategy replicator map.

This finite verification supplements the analytic proof; it is not an
all-parameter proof or an independent audit.
"""
import math
import sympy as sp
import mpmath as mp

def sigmoid_from_y(y):
    return 1/(1+mp.exp(y))

def Gstep(a,b,y):
    return y + a*(sigmoid_from_y(y)-b)

# Formal conjugacy and critical Taylor coefficients.
y,a,b=sp.symbols('y a b',real=True)
x=1/(1+sp.exp(y))
f=x/(x+(1-x)*sp.exp(a*(x-b)))
assert sp.simplify((1-f)/f-sp.exp(y+a*(x-b)))==0
S=y+a*x
assert sp.simplify(sp.diff(S,y) - (1-a*sp.exp(y)/(1+sp.exp(y))**2))==0
crit=y-4*sp.tanh(y/2)
ser=sp.series(crit,y,0,9).removeO().expand()
assert ser.coeff(y,1)==-1 and ser.coeff(y,3)==sp.Rational(1,6)
assert ser.coeff(y,5)==-sp.Rational(1,60)

# Periodic forcing: numerically solve the return fixed point, check phase locking and exact mean.
mp.mp.dps=45
cases=[(mp.mpf('3.5'),[mp.mpf('0.2'),mp.mpf('0.6'),mp.mpf('0.8')]),
       (mp.mpf('8'),[mp.mpf('0.25'),mp.mpf('0.75')]),
       (mp.mpf('8'),[mp.mpf('0.5'),mp.mpf('0.5'),mp.mpf('0.53')]),
       (mp.mpf('7.9'),[mp.mpf('0.01'),mp.mpf('0.99'),mp.mpf('0.2'),mp.mpf('0.8')])]
for alpha,inputs in cases:
    def return_map(t):
        for bi in inputs:
            t=Gstep(alpha,bi,t)
        return t
    # bracket + bisection, avoiding derivative changes near a=8.
    lo,hi=mp.mpf('-40'),mp.mpf('40')
    assert return_map(lo)>lo and return_map(hi)<hi
    for _ in range(175):
        mid=(lo+hi)/2
        if return_map(mid)-mid>0: lo=mid
        else: hi=mid
    y0=(lo+hi)/2
    phases=[]; t=y0
    for bi in inputs:
        phases.append(t);t=Gstep(alpha,bi,t)
    assert abs(t-y0)<mp.mpf('1e-37')
    xmean=sum(sigmoid_from_y(j) for j in phases)/len(phases)
    assert abs(xmean-sum(inputs)/len(inputs))<mp.mpf('1e-37')
    der=mp.mpf('1')
    for yi in phases:
        der*=1-alpha/(4*mp.cosh(yi/2)**2)
    assert abs(der)<1
    if alpha==8 and len(inputs)==2 and inputs[0]==mp.mpf('0.25'):
        assert abs(sigmoid_from_y(phases[0])-mp.mpf('0.9406126803877602'))<mp.mpf('1e-14')
        assert abs(der-mp.mpf('0.3059376113997673'))<mp.mpf('1e-14')
    for start in [-35,-5,0,1,12,35]:
        t=mp.mpf(start)
        for n in range(5000):
            t=Gstep(alpha,inputs[n%len(inputs)],t)
        assert abs(t-phases[5000 % len(phases)])<mp.mpf('1e-12')

# Borderline autonomous: higher precision lets us observe slow n^(-1/2) relaxation.
for start in [0.5,1.5,2.5]:
    t=start
    for n in range(1,150001):
        t=t-4*math.tanh(t/2)
    assert abs(math.sqrt(n)*abs(t)-math.sqrt(3))<0.02

# Beyond criticality the centered constant input has an attracting symmetric two-cycle.
for alpha in [mp.mpf('8.01'),mp.mpf('9'),mp.mpf('12'),mp.mpf('30')]:
    t=mp.findroot(lambda u: 4*u-alpha*mp.tanh(u/2),
                  (mp.mpf('0.1'),mp.sqrt(alpha-8)+mp.mpf('0.4')),
                  solver='secant')
    if abs(t)<mp.mpf('1e-15'):
        t=mp.findroot(lambda u: 4*u-alpha*mp.tanh(u/2),
                       (mp.sqrt(alpha-8)+mp.mpf('0.4'),alpha/4))
    assert t>0
    assert abs(Gstep(alpha,mp.mpf('0.5'),t)+t)<mp.mpf('1e-37')
    mul=1-alpha/(4*mp.cosh(t/2)**2)
    assert abs(mul)<1

# Aperiodic signals: two widely separated starts become synchronized.
for alpha in [mp.mpf('3'),mp.mpf('7.9'),mp.mpf('8')]:
    u,v=mp.mpf('-12'),mp.mpf('9')
    for n in range(2500):
        bn=mp.mpf('0.5')+mp.mpf('0.25')*mp.sin(mp.mpf(n)*mp.sqrt(2))
        u=Gstep(alpha,bn,u)
        v=Gstep(alpha,bn,v)
    assert abs(u-v)<mp.mpf('1e-20')

print('VERIFY_OK formal_identity=1 derivative_identity=1 critical_coefficients=3 periodic_forcings=4 phase_mean=4 global_starts=24 boundary_tail=3 supercritical_two_cycles=4 aperiodic_sync=3')
