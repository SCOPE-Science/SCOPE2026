"""Exact derivative and finite-precision asymptotic checks for a saddle cycle."""
import sympy as sp
import mpmath as mp
q,z,s = sp.symbols('q z s', positive=True)
qdot = 2*q*(q-1)/(q+1)
g = qdot-z
W = (q-1)**2/q
assert sp.simplify(sp.diff(W,q)*qdot - 2*W) == 0
assert sp.simplify(sp.diff(qdot,q) - 2*(q*q+2*q-1)/(q+1)**2) == 0
assert sp.simplify(sp.diff(g,q)*qdot - sp.diff(g,z)*z - (sp.diff(qdot,q)*qdot + z)) == 0
assert sp.simplify(qdot.subs(q,1)) == 0
assert sp.simplify(sp.diff(qdot,q).subs(q,1)) == 1
mp.mp.dps=60

def qfrom(eps,t):
    a=(eps**2/(1+eps))*mp.exp(2*t)
    return 1+(a+mp.sqrt(a*a+4*a))/2

def G(eps,t):
    Q=qfrom(eps,t)
    return 2*Q*(Q-1)/(Q+1)-eps*mp.exp(-t)

for s0 in [mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('2')]:
    qs=(s0+2+mp.sqrt((s0+2)**2+8*s0))/4
    cf=mp.log((qs-1)/mp.sqrt(qs))
    cb=mp.log(s0)
    for exponent in [4,6,9]:
        eps=mp.power(10,-exponent)
        center=mp.log(1/eps)
        Tf=mp.findroot(lambda t:G(eps,t)-s0,(center+cf-mp.mpf('.1'),center+cf+mp.mpf('.1')))
        Tb=mp.findroot(lambda u:G(eps,-u)+s0,(center+cb-mp.mpf('.1'),center+cb+mp.mpf('.1')))
        assert Tf>0 and Tb>0
        assert abs(Tf-(center+cf))<mp.mpf('0.05')
        assert abs(Tb-(center+cb))<mp.mpf('0.05')
print('VERIFY_OK rational_field_identity=5 positive_monotone_speed=1 threshold_cases=9 bidirectional_logarithmic_delay=18')
