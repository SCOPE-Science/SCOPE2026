"""Independent checks for single-count reconstruction of a Poisson first arrival.

Requires mpmath and sympy; all calculations are finite and supplemental to
an analytic global uniqueness proof.
"""
import math
import mpmath as mp
import sympy as sp

mp.mp.dps = 70
z = sp.symbols('z', positive=True)
F = sp.Ei(z)-sp.EulerGamma-sp.log(z)
g = sp.exp(z)-2*z+(1-z)*F
R = 2-sp.exp(-z)*(1+2*z+z*F)
assert sp.simplify(sp.diff(R,z)+sp.exp(-z)*g)==0
assert sp.simplify(sp.diff(g,z)-(sp.exp(z)-1)/z+1+F)==0
assert sp.simplify(sp.diff(g,z,2)-(1+z-sp.exp(z))/z**2)==0
print('symbolic risk/first derivative/second derivative identities: PASS')


def fm(x):
    return mp.ei(x)-mp.euler-mp.log(x)

def gm(x):
    return mp.exp(x)-2*x+(1-x)*fm(x)

def rm(x):
    return 2-mp.exp(-x)*(1+2*x+x*fm(x))

c=mp.findroot(gm,(mp.mpf('1.5'),mp.mpf('2.2')))
assert mp.mpf('1.7856603836284727')<c<mp.mpf('1.7856603836284729')
assert abs(gm(c))<mp.mpf('1e-60')
print('unique-root bracket:',mp.nstr(c,42))
print('normalized minimum risk:',mp.nstr(rm(c),42))

# Independent posterior-variance series, using conditional uniform order statistics.
def risk_series(x):
    p = mp.exp(-x)
    out = p
    term = p
    for k in range(1,200):
        term*=x/k
        out+=term*x*x*k/((k+1)**2*(k+2))
    return out

# Independent truncation of E[(conditional mean)^2], with a Poisson tail.
def risk_means(x):
    p = mp.exp(-x)
    sq = p*(1+x)**2
    term=p
    for k in range(1,200):
        term*=x/k
        sq+=term*(x/(k+1))**2
    return 2-sq

for x in [mp.mpf('0.05'),mp.mpf('0.5'),mp.mpf('1'),c,mp.mpf('3'),mp.mpf('7'),mp.mpf('20')]:
    assert abs(risk_series(x)-rm(x))<mp.mpf('1e-45')
    assert abs(risk_means(x)-rm(x))<mp.mpf('1e-45')
print('two independent conditional Poisson series vs closed risk, seven points: PASS')

# Rescale to distinct rates, and compare conditional formula to direct quadrature.
for rate in [mp.mpf('0.25'),mp.mpf('1'),mp.mpf('7')]:
    x=c/rate
    P0=mp.exp(-rate*x)
    mean0=x+1/rate
    E2=2/rate**2
    meansq=P0*mean0**2
    pk=P0
    for k in range(1,170):
        pk*=rate*x/k
        meansq+=pk*(x/(k+1))**2
    expected=(E2-meansq)*rate**2
    assert abs(expected-rm(c))<mp.mpf('1e-45')
print('dimensional rate scaling at 0.25, 1, 7: PASS')

zb=mp.findroot(lambda x:(2-x)*mp.exp(x)-2,(mp.mpf('1.4'),mp.mpf('1.8')))
Rb=1-zb**2/(mp.exp(zb)-1)
assert 0<rm(c)<Rb<1
print('binary-only optimal time:',mp.nstr(zb,42))
print('binary-only normalized risk:',mp.nstr(Rb,42))
print('count advantage over optimal binary risk:',mp.nstr((Rb-rm(c))/Rb,32))

# Numeric differentiation on both sides of the unique minimizer.
for x in [c-mp.mpf('0.6'),c-mp.mpf('0.25'),c+mp.mpf('0.25'),c+mp.mpf('1')]:
    derivative=mp.diff(rm,x)
    assert (derivative<0)==(x<c)
print('numerical derivative signs around minimizer: PASS')
