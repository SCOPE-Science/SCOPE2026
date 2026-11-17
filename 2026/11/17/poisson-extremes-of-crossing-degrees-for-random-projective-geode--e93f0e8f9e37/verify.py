"""Numerical and geometric checks for extreme degrees of projective geodesic arcs.

Requires Python, NumPy and SciPy. Experiments corroborate, but do not replace,
the analytic probability and Poisson-convergence arguments in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import comb

rng = np.random.default_rng(217314159)
PI = math.pi

def sample_arcs(n):
    x = rng.normal(size=(n, 2, 3))
    x /= np.linalg.norm(x, axis=2)[:, :, None]
    sg = np.where(np.sum(x[:, 0] * x[:, 1], axis=1) >= 0, 1., -1.)
    x[:, 1] *= sg[:, None]
    return x[:, 0], x[:, 1]

def degrees_of_targets(a, b, targets):
    normal = np.cross(a, b)
    r = np.cross(normal[targets, None, :], normal[None, :, :])
    def on_short_projective_arc(a0, b0, n0, r0):
        x1 = np.einsum('...k,...k->...', np.cross(a0, r0), n0)
        x2 = np.einsum('...k,...k->...', np.cross(r0, b0), n0)
        return x1*x2 > 1e-20
    h1 = on_short_projective_arc(a[targets, None, :], b[targets, None, :],
                                  normal[targets, None, :],r)
    h2 = on_short_projective_arc(a[None, :, :], b[None, :, :], normal[None, :, :],r)
    hits = h1 & h2
    for k,i in enumerate(targets): hits[k,i] = False
    return hits.sum(axis=1)

# The exact endpoint law is P(L <= t) = 1 - cos(t) for 0 <= t <= pi/2.
tests = np.linspace(0,PI/2,11)
assert abs(quad(math.sin,0,PI/2)[0]-1.) < 1e-11
assert abs(quad(lambda x:x*math.sin(x),0,PI/2)[0]-1.) < 1e-11
for t in tests:
    assert abs(quad(math.sin,0,t)[0]-(1-math.cos(t))) < 1e-11

# Direct intersection geometry for truly sampled projective endpoint pairs.
a,b = sample_arcs(4000)
length = np.arccos(np.clip(np.sum(a*b,axis=1),-1,1))
for lo,hi in [(0,.25),(.25,.5),(.5,.9),(.9,1.3),(1.3,1.57)]:
    ids = np.where((length>=lo)&(length<hi))[0]
    if len(ids)<4: continue
    sub = ids[:min(100,len(ids))]
    deg=degrees_of_targets(a,b,sub)
    expected=(len(a)-1)*length[sub]/(PI*PI)
    # Every target uses the same pool of independently drawn geodesics.
    assert np.abs(deg.mean()-expected.mean()) < 8*max(1.,np.sqrt(expected.mean()/len(sub)))

# Conditional mixture probabilities and their fixed-k sharp n^-2 asymptotics.
for n in [2000,10000,50000]:
    for k in [0,1,2]:
        def f(l):
            q=l/(PI*PI)
            return comb(n-1,k)*q**k*(1-q)**(n-1-k)*math.sin(l)
        prob=quad(f,0,PI/2,epsabs=1e-12,limit=120)[0]
        asympt=(k+1)*PI**4/n**2
        assert abs(prob/asympt-1) < (0.13 if n==2000 else 0.055 if n==10000 else 0.03)

# Direct finite geometric networks: short arcs have degree close to their
# length-predicted mean at the local n^1/2 scale.
errors=[]
for _ in range(60):
    a,b=sample_arcs(12000)
    length=np.arccos(np.clip(np.sum(a*b,axis=1),-1,1))
    idx=np.argsort(length)[:5]
    degrees=degrees_of_targets(a,b,idx)
    pred=(len(a)-1)*length[idx]/PI**2
    errors.extend((degrees-pred)/math.sqrt(len(a)))
assert np.mean(np.abs(errors)) < 0.055
print('sampled short-arc mean normalized degree error',round(float(np.mean(np.abs(errors))),6))
print('projective line-crossing probability',1/PI**2)
print('minimum-degree limiting survival P(M_n/sqrt(n)>x) = exp(-pi^4*x^2/2)')
print('PROJECTIVE_EXTREME_DEGREE_CHECKS_OK')

# A second, independently specified power-law family tests the general
# small-length exponent and the derived fixed-degree constant.
for alpha in [1.5, 3.0]:
    radius=PI/2
    c=radius**(-alpha)
    mu=alpha*radius/(alpha+1)
    n=40000
    for k in [0,1]:
        def integrand(t):
            q=mu*t/(PI*PI)
            return (comb(n-1,k)*q**k*(1-q)**(n-1-k)
                    *alpha*c*t**(alpha-1))
        actual=quad(integrand,0,radius,epsabs=1e-12,limit=120)[0]
        predicted=alpha*c*math.gamma(k+alpha)/math.factorial(k)*(PI*PI/(mu*n))**alpha
        assert abs(actual/predicted-1)<0.05,(alpha,k,actual/predicted)
for x in [0.03, 0.08, 0.13, 0.2]:
    n=50000
    exact=math.cos(PI*PI*x/math.sqrt(n))**n
    limit=math.exp(-PI**4*x*x/2)
    assert abs(exact-limit)<0.001
print('POWER_LAW_EXTREMES_CHECKS_OK')
