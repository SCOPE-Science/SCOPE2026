"""Independent, standalone checks of exact power-map identities and examples.

Requires Python 3, sympy and mpmath. This is supplementary verification;
finite checks are not a proof of continuum assertions.
"""
from fractions import Fraction
import sympy as s
import mpmath as mp

u = s.symbols('u', real=True)
for deg in (2, 3, 4, 6):
    d = s.Integer(deg)
    qc = (d + 1) ** (d - 1) / d ** d
    G = qc * (1 - qc * (1-u) ** d) ** d
    x0 = 1 / (d + 1)
    assert s.simplify(G.subs(u, x0) - x0) == 0
    assert s.simplify(s.diff(G, u).subs(u, x0) - 1) == 0
    assert s.simplify(s.diff(G, u, 2).subs(u, x0)) == 0
    assert s.simplify(s.diff(G, u, 3).subs(u, x0) + (d-1)*(d+1)**3/d**2) == 0

mp.mp.dps = 65
cases = 0
for d in (mp.mpf(2), mp.mpf(3), mp.mpf('1.5'), mp.mpf(6)):
    qc = (d+1)**(d-1)/d**d
    sconst = mp.sqrt(2*d/((d-1)*(d+1)**2*qc))
    C = 4*(d+1)**2*sconst/(3*d)
    tstar = d/(d+1)
    P = lambda t: t**(d-1)*(d*d-(d*d-1)*t)
    for eps in (mp.mpf('1e-4'), mp.mpf('1e-6')):
        q = qc + eps
        tminus = mp.findroot(lambda t: q*P(t)-1,
                             (tstar-2*sconst*mp.sqrt(eps), tstar-mp.mpf('.5')*sconst*mp.sqrt(eps)))
        tplus = mp.findroot(lambda t: q*P(t)-1,
                            (tstar+mp.mpf('.5')*sconst*mp.sqrt(eps), tstar+2*sconst*mp.sqrt(eps)))
        H = lambda t: (1-t)/(1-q*t**d)**d
        width = H(tplus)-H(tminus)
        assert abs(width/(C*eps**mp.mpf('1.5'))-1)<mp.mpf('0.001')
        assert tminus<tstar<tplus
        cases+=1

# Exact rational cubic root census at a representative point.
# d=2, q=4/5, r=4/5; cusp is (3/4,3/4), while
# the local minimum and maximum of H are 25/32 and 27/32.
q=s.Rational(4,5)
r=s.Rational(4,5)
t=s.symbols('t')
poly=s.factor((1-t)-r*(1-q*t*t)**2)
roots=s.nroots(poly, maxsteps=200)
physical=sorted(float(s.re(z)) for z in roots if abs(float(s.im(z)))<1e-12 and 0<float(s.re(z))<1)
assert len(physical)==3, (poly,roots)
assert physical[0]<physical[1]<physical[2]

# For d=1 return is an affine strict contraction with multiplier qr.
for aq,br,cr in ((s.Rational(3,4),s.Rational(1,2),s.Rational(1,4)),
                  (s.Rational(5,6),s.Rational(2,3),s.Rational(1,3))):
    qq=(1-aq)/(1-br);rr=cr/br
    assert qq>0 and qq<1 and rr>0 and rr<1
    assert rr*qq<1

# High-exponent three-phase and endpoint asymptotics at fixed parameters.
q=mp.mpf('0.8');r=mp.mpf('0.6')
def bisect(f,a,b,steps=280):
    fa=f(a)
    for _ in range(steps):
        mid=(a+b)/2; fm=f(mid)
        if fa*fm>0: a=mid;fa=fm
        else: b=mid
    return (a+b)/2
for d in (20, 40):
    H=lambda t:(1-t)/(1-q*t**d)**d
    ta=1-2*mp.log(d)/d
    tb=1-mp.mpf(1)/d**2
    assert 0<ta<tb<1 and H(ta)<r<H(tb)
    tleft=bisect(lambda z:H(z)-r,mp.mpf('0'),ta)
    tright=bisect(lambda z:H(z)-r,tb,mp.mpf('1'))
    ularge=1-tleft; usmall=1-tright
    assert 0<usmall<ularge<r
    assert abs(usmall/(r*(1-q)**d)-1)<mp.mpf('1e-5')
    assert abs((r-ularge)/(r*d*q*(1-r)**d)-1)<mp.mpf('1e-3')
    for troot in (tleft,tright):
        multiplier=r*d*d*q*troot**(d-1)*(1-q*troot**d)**(d-1)
        assert 0<multiplier<1
print('PASS: exact cusp derivatives,',cases,
      'high-precision cusp-width checks, rational triple-cycle census,',
      'affine contraction and large-exponent branch checks')
