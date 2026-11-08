#!/usr/bin/env python3
"""Independent checks of the harmonic polytropic-entropy peak classification.
Only finite consistency checks; the proof is in RESULT.md.
Requires sympy and mpmath.
"""
import sympy as sp
import mpmath as mp

z=sp.symbols('z',positive=True)
F=(sp.exp(z)-1)/z
Fp=sp.diff(F,z); Fpp=sp.diff(Fp,z); Fppp=sp.diff(Fpp,z)
Q=sp.exp(z)*(z*z-4*z+6)-2*z-6
assert sp.simplify(z**4*(3*Fpp**2-2*Fp*Fppp)-sp.exp(z)*Q)==0
assert sp.simplify(sp.diff(sp.diff(Q,z),z)-sp.exp(z)*z*z)==0
print('Symbolic strict-monotonicity identity and q-second-derivative: OK')
mp.mp.dps=65

def g(L,x):
    if abs(L*x)<mp.mpf('1e-18'):
        return L+L**2*x/2+L**3*x*x/6+L**4*x**3/24+L**5*x**4/120
    return mp.expm1(L*x)/x

def gp(L,x):
    if abs(L*x)<mp.mpf('1e-13'):
        return L**2/2+L**3*x/3+L**4*x*x/8+L**5*x**3/30
    return (L*x*mp.exp(L*x)-mp.expm1(L*x))/x**2

def entropy(L,delta,x):
    return (1-x)*((1+delta)*g(L,x)-L)

def deriv(L,delta,x):
    return L-(1+delta)*(g(L,x)-(1-x)*gp(L,x))

def duration(L,delta,x):
    return (1-x)/x*mp.log((1+1/delta)*mp.exp(L*x)-1/delta)

def peak(L,delta):
    a=mp.mpf(0);b=mp.mpf(1)
    if deriv(L,delta,a)<=0: return None
    for _ in range(200):
        m=(a+b)/2
        if deriv(L,delta,m)>0:a=m
        else:b=m
    return (a+b)/2

cases = [
 (mp.log(mp.mpf('1.5')),mp.mpf('0.1'),True),
 (mp.log(mp.mpf('1.5')),mp.mpf('0.5'),False),
 (mp.mpf('1.5'),mp.mpf('2'),True),
 (mp.mpf('1.5'),mp.mpf('4'),False),
 (mp.mpf('2'),mp.mpf('20'),True),
 (mp.mpf('10'),mp.mpf('100'),True),
 (-mp.log(mp.mpf('1.5')),mp.mpf('-0.1'),True),
 (-mp.log(mp.mpf('1.5')),mp.mpf('-0.3'),False),
 (-mp.mpf('4'),mp.mpf('-0.2'),True),
 (-mp.mpf('4'),mp.mpf('-0.8'),False),
]
for L,delta,expected in cases:
    rt=peak(L,delta)
    assert (rt is not None)==expected, (L,delta,rt,expected)
    # finite differences of exact entropy expression vs analytic derivative
    for x in [mp.mpf('0.07'),mp.mpf('0.31'),mp.mpf('0.69')]:
        fd=(entropy(L,delta,x+mp.mpf('1e-12'))-entropy(L,delta,x-mp.mpf('1e-12')))/mp.mpf('2e-12')
        assert abs(fd-deriv(L,delta,x)) < mp.mpf('1e-18')*max(1,abs(deriv(L,delta,x)))
    xs=[mp.mpf(i)/100 for i in range(1,100)]
    assert all(duration(L,delta,x)>duration(L,delta,x+mp.mpf('0.00001')) for x in xs)
    if rt is not None:
        assert abs(deriv(L,delta,rt))<mp.mpf('1e-49')
        assert entropy(L,delta,rt)>max(entropy(L,delta,0),entropy(L,delta,1))
        assert all(deriv(L,delta,x)>0 for x in [rt/4,rt/2])
        assert all(deriv(L,delta,x)<0 for x in [(1+rt)/2,(3+rt)/4])
    else:
        assert all(deriv(L,delta,x)<0 for x in xs)
    print('PASS: L=',mp.nstr(L,7),'delta=',mp.nstr(delta,7),'peak=',mp.nstr(rt,8) if rt else 'none')

# Critical-window coefficients: x_*/(threshold-mismatch) approaches closed form.
for L in [mp.mpf('0.4'),mp.mpf('1.5')]:
    dc=L/(2-L);pred=(2-L)**2/(4*L*(1-L/3)); eps=mp.mpf('0.0000001')
    xx=peak(L,dc-eps)
    assert abs(xx/eps/pred-1)<mp.mpf('0.00001')
    print('PASS compression critical scaling, L=',L)
for ell in [mp.mpf('0.4'),mp.mpf('4')]:
    ec=ell/(2+ell);pred=(2+ell)**2/(4*ell*(1+ell/3));eps=mp.mpf('0.0000001')
    xx=peak(-ell,-ec+eps)
    assert abs(xx/eps/pred-1)<mp.mpf('0.00001')
    print('PASS expansion critical scaling, ell=',ell)
print('ALL CHECKS PASSED; finite checks are not a substitute for the proof.')
