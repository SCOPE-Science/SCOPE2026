"""Numerical diagnostics for the thin isosceles, one-point-per-side acuteness law.
Run: python check.py . Requires numpy and scipy.
Finite diagnostics corroborate, but do not establish, the asymptotic proof.
"""
import numpy as np
from scipy.stats import qmc
from scipy.integrate import quad


def favorable_p_length(q, t, h):
    """Exact P-length from all three strict angle inequalities (array-safe)."""
    L = q + t
    a = (1-q)*(1-t)
    lower = np.maximum(-1, -t-h*h*(1-t)*(q-t)/L)
    upper = np.minimum(1, q-h*h*(1-q)*(q-t)/L)
    discriminant = L*L-4*h*h*a
    d = np.sqrt(np.maximum(discriminant, 0))
    left_root = (q-t-d)/2
    right_root = (q-t+d)/2
    separated = np.maximum(0,np.minimum(upper,left_root)-lower)+np.maximum(0,upper-np.maximum(lower,right_root))
    full = np.maximum(0,upper-lower)
    return np.where(discriminant >= 0,separated,full)


def brute_p_length(q,t,h,grid=70001):
    p=np.linspace(-1,1,grid)
    a=(1-q)*(1-t)
    ok=((q-p)*(-t-p)+h*h*a > 0)
    ok &= (q+t)*(q-p)-h*h*(1-q)*(q-t) > 0
    ok &= (q+t)*(p+t)+h*h*(1-t)*(q-t) > 0
    return 2*ok.mean()

rng=np.random.default_rng(151203)
for h in [0.03,0.1,0.6]:
    for j in range(6):
        q=float(rng.uniform(0.03,0.97))
        t=float(rng.uniform(0.03,0.97))
        exact=float(favorable_p_length(np.array([q]),np.array([t]),h)[0])
        mesh=brute_p_length(q,t,h)
        assert abs(exact-mesh)<0.00015,(q,t,h,exact,mesh)
print('ALL_ANGLE_INTERSECTION_CHECK_OK')

C=8*np.log(2)/3-7/6
C_int=quad(lambda x:(1-x)**2*np.log((1+x)/x),0,1,epsabs=1e-11)[0]
assert abs(C-C_int)<1e-10
print('LIMIT_INTEGRAL_CHECK_OK',C)

q,t=qmc.Sobol(2,scramble=True,seed=210311).random_base2(20).T
for h in [0.1,0.04,0.01]:
    P=np.mean(favorable_p_length(q,t,h))/2
    ratio=P/h**2
    print('h',h,'probability',f'{P:.10g}','scaled',f'{ratio:.9f}')
    assert abs(ratio-C)< 2.5*h
print('THIN_TRIANGLE_ACUTENESS_DIAGNOSTICS_OK')
