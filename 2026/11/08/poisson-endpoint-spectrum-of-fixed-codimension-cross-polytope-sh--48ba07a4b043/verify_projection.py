"""Numerical and algebraic checks for the random cross-polytope shadow-radius theorem."""
import math
import numpy as np
from scipy.integrate import quad

def octahedral_cdf(r):
    if r <= math.sqrt(2/3): return 0.0
    if r >= 1: return 1.0
    t=math.sqrt(1-r*r)
    return 1-3*t+(12/math.pi)*(t*math.asin(t/math.sqrt(1-t*t))
                         + math.atan(math.sqrt(1-2*t*t))-math.pi/4)

def pair_integral(t):
    # Independent integral of the projected two-coordinate spherical density.
    return (2/math.pi)*quad(lambda x:math.asin(t/math.sqrt(1-x*x)),0,t,
                             epsabs=2.e-13)[0]

for t in [0.01,0.08,0.2,0.4,1/math.sqrt(3)]:
    direct=1-3*t+3*pair_integral(t)
    value=octahedral_cdf(math.sqrt(1-t*t)) if t<1/math.sqrt(3)-1.e-10 else 0.
    assert abs(direct-value)<4.e-12,(t,value,direct)

rng=np.random.default_rng(20261103)
a=rng.normal(size=(500000,3))
a/=np.linalg.norm(a,axis=1)[:,None]
R=np.sqrt(1-np.min(a*a,axis=1))
errors=[abs(np.mean(R<=r)-octahedral_cdf(r)) for r in [.82,.85,.9,.95,.98]]
assert max(errors)<.004

# Stiefel construction: projected lengths are sqrt(1-lev_i), lev_i=g_i^T (G^T G)^{-1}g_i.
rows_checked=0
for codim in [1,2,3,4]:
    n=160
    reps=4000
    G=rng.normal(size=(reps,n,codim))
    gram=np.einsum('rni,rnj->rij',G,G)
    inv=np.linalg.inv(gram)
    lever=np.einsum('rni,rij,rnj->rn',G,inv,G)
    assert np.all(lever>=-1.e-10) and np.all(lever<=1+1.e-10)
    assert np.max(np.abs(np.sum(lever,axis=1)-codim))<1.e-10
    # For a random sample of frames, explicitly project each vertex onto normal complement.
    for i in range(3):
        Q=G[i]@np.linalg.inv(np.linalg.cholesky(gram[i]).T)
        assert np.max(np.abs(Q.T@Q-np.eye(codim)))<1.e-10
        v=np.eye(n)-Q@Q.T
        assert np.max(np.abs(np.sum(v*v,axis=0)-(1-lever[i])))<1.e-10
        rows_checked+=n
    D=n**(1+2/codim)*(1-np.sqrt(1-np.min(lever,axis=1)))
    mean_theory=math.gamma(1+codim/2)**(2/codim)*math.gamma(1+2/codim)
    cdf_theory=1-math.exp(-1/math.gamma(1+codim/2))
    empirical=float(np.mean(D<=1))
    assert abs(empirical-cdf_theory)<.065,(codim,empirical,cdf_theory)
    print(f'codimension={codim}  size={n}  reps={reps}  CDF_at_1={empirical:.6f}  limit={cdf_theory:.6f}  mean={D.mean():.5f} limit_mean={mean_theory:.5f}')
print(f'CHECKS_PASS integral_identities=5 octahedral_mc=500000 octahedral_CDF_cases=5 max_oct_error={max(errors):.7f} exact_projection_coordinate_checks={rows_checked} poisson_codimensions=4')
