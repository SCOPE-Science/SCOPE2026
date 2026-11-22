"""Independent numerical and symbolic checks for renewal-reset return statistics.

Run: python verify.py
Requires: Python 3, sympy, mpmath. Finite checks do not replace the proof.
"""
from math import exp, gamma, pi, sqrt
import mpmath as mp
import sympy as sp

mp.mp.dps = 70
checks = 0

def close(a, b, tol=mp.mpf('1e-12')):
    global checks
    aa, bb = mp.mpf(a), mp.mpf(b)
    if abs(aa-bb) > tol * max(1, abs(aa), abs(bb)):
        raise AssertionError(f'{aa} != {bb}')
    checks += 1

z, b, lam = sp.symbols('z b lam', positive=True)
radial = sp.exp(-z)*(1-b+b*z)
assert sp.simplify(sp.integrate(radial, (z, 0, sp.oo)) - 1) == 0
assert sp.simplify(sp.integrate(z**2*radial, (z, 0, sp.oo)) - (2+4*b)) == 0
assert sp.simplify(sp.integrate(radial, (z, 0, lam)) - (1-sp.exp(-lam)*(1+b*lam))) == 0
checks += 3

for D, r in [(1,1), (2,3), (mp.mpf('.7'),mp.mpf('1.3'))]:
    k = mp.sqrt(r/D)
    for a in [mp.mpf('0'), mp.mpf('.2'),mp.mpf('.5'),mp.mpf('.8')]:
        c = mp.mpf('.9')
        mut = mp.mpf(2)/r
        nur = mp.gamma(1-a)*k**(a-1)*(3-a)/(2*c)
        w = mut/(mut+nur)
        bb = w/4 + (1-w)/(3-a)
        for x in [mp.mpf('.27')/k, mp.mpf('1')/k, mp.mpf('2.5')/k]:
            xx = abs(x); zz = k*xx
            heat = lambda t: mp.exp(-xx**2/(4*D*t))/mp.sqrt(4*mp.pi*D*t)
            rho_d = mp.quad(lambda t: mp.exp(-r*t)*(1+r*t)*heat(t), [0,1/r,mp.inf])
            rho_d_formula = mp.exp(-zz)*(zz+3)/(4*mp.sqrt(D*r))
            close(rho_d,rho_d_formula)
            # Endpoint density evaluated by direct time integral.
            g = mp.quad(lambda t: r*r*t*mp.exp(-r*t)*heat(t), [0,1/r,mp.inf])
            close(g,k*mp.exp(-zz)*(1+zz)/4)
            endpoint = lambda y:k/4*mp.exp(-k*y)*(1+k*y)
            rho_r = mp.quad(lambda u:endpoint(xx+u)*u**(-a)/c,[0,1/k,mp.inf])
            rho_r_formula = mp.gamma(1-a)*k**a*mp.exp(-zz)*(zz+2-a)/(4*c)
            close(rho_r,rho_r_formula)
            predicted = (rho_d+rho_r)/(mut+nur)
            collapsed = k/2*mp.exp(-zz)*(1-bb+bb*zz)
            close(predicted,collapsed)
        close(mp.quad(lambda t: mp.exp(-t)*(1-bb+bb*t),[0,mp.inf]),1)
        close(mp.quad(lambda t: t**2*mp.exp(-t)*(1-bb+bb*t),[0,mp.inf]),2+4*bb)

# Exact example: ballistic and accelerating returns are spatially identical.
alpha0 = mp.mpf(0); c0=mp.mpf('0.5')
alpha1 = mp.mpf('0.5'); c1=5*mp.sqrt(mp.pi)/4
for a,c,expect_w in [(alpha0,c0,mp.mpf(2)/5),(alpha1,c1,mp.mpf(2)/3)]:
    w=4*c/(4*c+mp.gamma(1-a)*(3-a))
    bv=w/4+(1-w)/(3-a)
    close(w,expect_w);close(bv,mp.mpf(3)/10)
    for x in [0,mp.mpf('.3'),1,mp.mpf(2),mp.mpf(5)]:
        close(mp.exp(-x)/2*(1-bv+bv*x),mp.exp(-x)*(7+3*x)/20)

# Stationary position law provides b; return-labelled second moment provides alpha.
for a in [mp.mpf('.05'),mp.mpf('.5'),mp.mpf('.93')]:
    return_b = 1/(3-a)
    return_m2 = 2+4*return_b
    recovered_alpha = 3-1/((return_m2-2)/4)
    close(recovered_alpha,a)

# Exact TV/CDF bounds: integrate both sides of the unique crossing.
for ba,bb in [(mp.mpf('.29'),mp.mpf('.4')),(mp.mpf('.26'),mp.mpf('.49'))]:
    f = lambda t:mp.exp(-t)*(ba-bb)*(t-1)
    tv=mp.mpf('.5')*(mp.quad(lambda t:abs(f(t)),[0,1])+mp.quad(lambda t:abs(f(t)),[1,mp.inf]))
    close(tv,abs(ba-bb)/mp.e)
    close(mp.quad(f,[0,1]),-(ba-bb)/mp.e)

print('PASS: direct renewal integrations, moments, inversion, aliasing, TV, and phase recovery; checks=',checks)
