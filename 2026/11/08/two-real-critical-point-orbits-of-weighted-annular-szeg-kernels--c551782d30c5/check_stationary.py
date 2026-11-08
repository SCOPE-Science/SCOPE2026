"""Numerical corroboration of the annular weighted Szego derivative identities.

Run with Python 3 and mpmath >= 1.3. This finite test is not a proof of
root uniqueness, multiplicity, or the small-hole asymptotic theorem.
"""
import mpmath as mp

mp.mp.dps = 60

def theta(z, q):
    return mp.qp(z, q) * mp.qp(q / z, q)

def theta_ratio(s, q, t):
    return theta(-t * s, q) / theta(s, q)

def derivative_series(s, q, t, radius=65):
    return mp.fsum(
        n * s ** (n - 1) / (1 + t * q ** n)
        for n in range(-radius, radius + 1) if n
    )

def check(a, b, scale=mp.mpf('1e-30')):
    assert abs(a - b) < scale, (a, b, a-b)

identities=0
for q,t,s in [
    (mp.mpf('.25'), mp.mpf('.7'), mp.mpc('.58','.10')),
    (mp.mpf('.16'), mp.mpf('3.2'), mp.mpc('.52','-.17')),
    (mp.mpf('.09'), mp.mpf('1.7'), mp.mpc('.44','.15')),
]:
    check(theta_ratio(q*s,q,t),-theta_ratio(s,q,t)/t)
    d1=mp.diff(lambda v:theta_ratio(v,q,t),q*s)
    d2=mp.diff(lambda v:theta_ratio(v,q,t),s)
    check(d1,-d2/(t*q),mp.mpf('1e-26'))
    identities+=2

stationary=0
# Strictly interior and equality radius regimes are explicitly tested.
for q in [mp.mpf('0.0001'), mp.mpf('0.000001')]:
    t=mp.mpf('4')
    roots=[]
    for sign in [-1,1]:
        guess=sign*mp.sqrt(q/t)+q*(t-1)/t
        root=mp.findroot(lambda v: derivative_series(v,q,t),
                         (guess*mp.mpf('.9999'),guess*mp.mpf('1.0001')))
        assert root*sign>0
        assert q<abs(root)<1
        assert abs(derivative_series(root,q,t))<mp.mpf('1e-40')
        approx=sign*mp.sqrt(q/t)+q*(t-1)/t
        assert abs(root-approx)< 3*q**mp.mpf('1.5')
        roots.append(root)
        stationary+=1
    assert abs(roots[0])<abs(roots[1])
    for a,expected in [(mp.mpf('.4'),2),(mp.mpf('.5'),1),(mp.mpf('.6'),0)]:
        inside=sum(1 for root in roots if mp.sqrt(q)*a < abs(root) < a)
        assert inside==expected,(q,a,inside,expected)
        stationary+=1

print(f'WEIGHTED_ANNULUS_CRITICAL_PASS theta_identities={identities} root_and_phase_checks={stationary}')
