"""Standalone numeric and symbolic checks for two-sign OU integral design.

Run: python verify_ou_sign.py (requires mpmath and sympy).
The continuum optimization theorem requires the accompanying analytic proof.
"""
import math
import random
import mpmath as mp
import sympy as sp

mp.mp.dps = 65
pi = mp.pi


def weight(t, lam):
    return (2-mp.exp(-lam*t)-mp.exp(-lam*(1-t)))/lam


def sign_corr(d, lam):
    return (2/pi)*mp.asin(mp.exp(-lam*d))


def explained(s, t, lam):
    """Variance explained by the two signs; uses analytic continuous limit."""
    s, t, lam = map(mp.mpf, (s,t,lam))
    if s == t:
        return (2/pi)*weight(s,lam)**2
    c = sign_corr(t-s,lam)
    u, v = weight(s,lam), weight(t,lam)
    return (2/pi)*(u*u + v*v-2*c*u*v)/(1-c*c)


def symmetric_score(d, lam):
    c=sign_corr(d,lam)
    k=weight((1-d)/2,lam)
    return (2/pi)*2*k*k/(1+c)


def a_func(d,lam):
    u=lam*d/2
    b=mp.exp(-lam/2)
    return b*mp.sinh(u)/(1-b*mp.cosh(u))


def g_func(d,lam):
    r=mp.exp(-lam*d)
    return r/(mp.sqrt(1-r*r)*(pi/2+mp.asin(r)))


def bisect(f,a,b,n=240):
    fa=f(a)
    fb=f(b)
    assert fa*fb<=0, (a,b,fa,fb)
    for _ in range(n):
        m=(a+b)/2
        fm=f(m)
        if fa*fm<=0:
            b=m;fb=fm
        else:
            a=m;fa=fm
    return (a+b)/2


crit = bisect(lambda lam:g_func(mp.mpf(1),lam)-1,mp.mpf('0.001'),mp.mpf('0.3'))
assert abs(crit-mp.mpf('0.0600892783079994')) < mp.mpf('1e-12')

checks = 0
# Sympy independently validates the central algebraic identity for the proof.
w,c,q,z=sp.symbols('w c q z',positive=True,real=True)
# q=e^(-w): cosh(w)=(q+1/q)/2, cosh(2w)=(q^2+q^-2)/2.
cs=(q+1/q)/2
ch2=(q**2+q**-2)/2
sh=(1/q-q)/2
assert sp.simplify((1-c)*cs-q*(ch2-c)-(q*q-c)*sh)==0
checks+=1

# Exact Gaussian sign-correlation sanity against the orthant formula.
for r in [mp.mpf('0.01'),mp.mpf('0.2'),mp.mpf('0.7'),mp.mpf('0.95')]:
    cc=2/mp.pi*mp.asin(r)
    assert 0<cc<r
    # P(++ ) = 1/4+arcsin(r)/(2 pi).
    pp=mp.mpf(1)/4+mp.asin(r)/(2*pi)
    assert abs((4*pp-1)-cc)<mp.mpf('1e-55')
    checks+=2

for lam in [mp.mpf(str(x)) for x in ['0.0001','0.003','0.03','0.06','0.08','0.1','0.2','0.5','1','2','5','15','50']]:
    if lam <= crit:
        d=mp.mpf(1)
    else:
        d=bisect(lambda x:g_func(x,lam)-a_func(x,lam),mp.mpf('0.00000001'),mp.mpf(1))
    assert d>0 and d<=1
    optimum = symmetric_score(d,lam)
    # Analytic derivative signs, bisection behavior, and global fixed-gap center.
    rng = random.Random(4301)
    for _ in range(140):
        dd=mp.mpf(str(rng.uniform(0.00001,1)))
        left=mp.mpf(str(rng.uniform(0,1-float(dd))))
        mid=(1-dd)/2
        val=explained(left,left+dd,lam)
        val_center=explained(mid,mid+dd,lam)
        assert val <= val_center + mp.mpf('1e-42')
        assert val <= optimum + mp.mpf('1e-38'), (lam,dd,d,val,optimum)
        checks+=2
    for frac in [mp.mpf(i)/100 for i in range(1,100)]:
        if frac < d and d < 1:
            assert g_func(frac,lam)>a_func(frac,lam)
        if frac > d:
            assert g_func(frac,lam)<a_func(frac,lam)
        checks+=1
    # Sign decoder projection formula has positive finite risk.
    varI=2*(lam+mp.expm1(-lam))/lam**2
    assert 0<optimum<varI
    assert abs(symmetric_score(d,lam)-explained((1-d)/2,(1+d)/2,lam))<mp.mpf('1e-45')
    checks+=2

# A direct covariance integral check using independent double numerical integration.
for lam,t in [(mp.mpf('0.3'),mp.mpf('0.1')),(mp.mpf('1.7'),mp.mpf('0.7'))]:
    integral=mp.quad(lambda u:mp.exp(-lam*abs(u-t)),[0,t,1])
    assert abs(integral-weight(t,lam))<mp.mpf('1e-55')
    checks+=1

for lam in [mp.mpf('100'),mp.mpf('200'),mp.mpf('500')]:
    d=bisect(lambda x:g_func(x,lam)-a_func(x,lam),mp.mpf('0.2'),mp.mpf('0.5'))
    leading=mp.mpf(1)/3+2*mp.log(4/pi)/(3*lam)
    assert abs(d-leading)<mp.mpf('2e-6')
    checks+=1

print('checks',checks)
print('critical_lambda',mp.nstr(crit,45))
for lam in [mp.mpf('0.03'),mp.mpf('0.1'),mp.mpf('1'),mp.mpf('20')]:
    d=mp.mpf(1) if lam<=crit else bisect(lambda x:g_func(x,lam)-a_func(x,lam),mp.mpf('0.00001'),mp.mpf(1))
    varI=2*(lam+mp.expm1(-lam))/lam**2
    gain=symmetric_score(d,lam)
    print('lambda',mp.nstr(lam,5),'separation',mp.nstr(d,20),'left',mp.nstr((1-d)/2,20), 'Bayes_risk',mp.nstr(varI-gain,18),'explained_fraction',mp.nstr(gain/varI,18))
