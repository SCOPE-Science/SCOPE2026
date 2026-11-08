"""Finite numerical cross-checks of the stated stationary-density identities.

Requirements: Python 3, scipy, numpy. The analytic argument is in RESULT.md.
Run: python checker.py
"""
import math
from scipy.integrate import quad
from scipy.special import beta, gammaln

def normalizer(a):
    return math.exp(gammaln(a + .5) - gammaln(a) - .5 * math.log(math.pi))

def density(z, a, b):
    assert a > 0 and b > 0 and 0 <= z < 1
    ka, kb = normalizer(a), normalizer(b)
    if z == 0:
        if a+b <= 1:
            return float('inf')
        return 2*ka*kb*beta(.5,a+b-1)
    left = 2*z-1
    def smooth(x):
        y = 2*z-x
        return (1+x)**(a-1)*(1+y)**(b-1)
    val = quad(smooth,left,1,weight='alg',wvar=(b-1,a-1),
               epsabs=2e-11,epsrel=2e-11,limit=250)[0]
    return 2*ka*kb*val

def center_second(a,b):
    assert a < 1 and a+b > 3 and b > 2
    return 16*normalizer(a)*normalizer(b)*(b-1)*(1-a)*beta(.5,a+b-2)/(a+b-3)

def check(ok, name):
    if not ok:
        raise AssertionError(name)
    print('PASS',name)

# Positive-curvature sector, checked against an independent convolution
# quadrature (not evaluated by differentiating the symbolic result).
for a,b in [(.2,4.0),(.4,3.2),(.8,3.0),(.5,4.0)]:
    h = 1e-4
    approximate = 2*(density(h,a,b)-density(0,a,b))/h**2
    prediction = center_second(a,b)
    check(prediction>0 and abs(approximate/prediction-1)<.03,
          f'positive center curvature a={a}, b={b}')

# Equal or fast rates: a strict central maximum on observed grid.
for a,b in [(1.2,2.3),(2.0,2.0),(1.0,3.0),(3.0,1.0)]:
    values=[density(z,a,b) for z in [0,.1,.2,.4,.65,.85,.97]]
    check(all(x>y for x,y in zip(values,values[1:])),
          f'decreasing center-to-edge a={a}, b={b}')

# The boundary asymptotic is an independent endpoint beta integral.
for a,b in [(.3,3.4),(1.2,2.3),(.4,.8)]:
    coeff=4**(a+b-1)*normalizer(a)*normalizer(b)*beta(a,b)
    z=.99999
    ratio=density(z,a,b)/(coeff*(1-z)**(a+b-1))
    check(abs(ratio-1)<.005, f'edge coefficient a={a}, b={b}')

# The normalized density integrates to one, using the symmetry of the
# convolution and excluding the endpoint, on two smooth examples.
for a,b in [(1.2,2.3),(.4,3.2)]:
    total=2*quad(lambda z: density(z,a,b),0,1,epsabs=2e-8,
                 epsrel=2e-8,limit=100)[0]
    check(abs(total-1)<1e-6, f'normalization a={a}, b={b}')

# The interaction cancels identically in the arithmetic mean drift.
for x1,x2,g in [(3.,-1.,.2),(2.1,.3,4.),(.4,-5.,1.5)]:
    force1=g/(x1-x2)
    force2=g/(x2-x1)
    check(abs(force1+force2)<1e-14,'pair-force cancellation')
print('All 16 checks passed; finite checks do not replace the proof.')
