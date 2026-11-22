"""Reproducibility checks for the exact two-sided location-standardized KS CDF.

Requires Python 3, SymPy and NumPy. The algebraic identities below are exact;
the seeded Monte Carlo comparison is a diagnostic, not part of the proof.
"""
import sympy as S
import numpy as np
from exact_ks_argmax import cdf_exact

checks=0
def verify(condition,msg):
    global checks
    if not bool(condition): raise AssertionError(msg)
    checks+=1

# Direct hand-checkable n=1 law, including its support edge.
for t in [S.Rational(1,2),S.Integer(1),S.Rational(3,2),S.Integer(2),S.Integer(3),S.Integer(9)]:
    expected=S.Integer(0) if t<=1 else 1-2/(1+t*t)
    verify(S.simplify(cdf_exact(1,t)-expected)==0,f'n=1, t={t}')

# Independent exact expressions for low sample sizes at t=2.
expected={
  1:S.Rational(3,5),
  2:S.Rational(43,25)-2*S.sqrt(5)/5,
  3:-S.Rational(8099,3375)+S.Rational(376,375)*S.sqrt(11),
  4:S.Rational(1554007,80000)-S.Rational(3681,1000)*S.sqrt(19)-S.Rational(27,25)*S.sqrt(5),
}
for n,v in expected.items():
    verify(S.simplify(cdf_exact(n,2)-v)==0,f'exact CDF n={n}')

# Rigorous rational bracket for the exact finite-n 95% quantile.
cL=cdf_exact(3,S.Rational(22981,10000))
cR=cdf_exact(3,S.Rational(22982,10000))
verify(S.sign(S.simplify(cL-S.Rational(19,20)))==-1,'lower critical bracket')
verify(S.sign(S.simplify(cR-S.Rational(19,20)))==1,'upper critical bracket')

# Check CDF bounds and monotonicity using exact algebraic sign comparisons.
for n in range(1,7):
    vals=[cdf_exact(n,S.Rational(t,2)) for t in range(1,9)]
    for v in vals:
        verify(S.sign(v)>=0 and S.sign(1-v)>=0,f'range n={n}')
    for a,b in zip(vals,vals[1:]):
        verify(S.sign(S.simplify(b-a))>=0,f'monotonicity n={n}')

# Independent direct-sample route.  Simulation is only a numerical diagnostic.
rng=np.random.default_rng(4312)
for n in range(1,7):
    u=np.sort(rng.random((200000,n)),axis=1)
    ranks=np.arange(1,n+1)
    ds=np.maximum(ranks/n-u,u-(ranks-1)/n)
    winners=ds.argmax(axis=1)
    K=ds[np.arange(u.shape[0]),winners]
    U=u[np.arange(u.shape[0]),winners]
    V=K/np.sqrt(U*(1-U))
    for t in (S.Rational(3,2),S.Integer(2),S.Integer(3)):
        exact=float(S.N(cdf_exact(n,t),25))
        empirical=float(np.mean(V<=float(t)))
        verify(abs(empirical-exact)<0.01,f'Monte Carlo n={n}, t={t}')
print(f'PASS: {checks} exact/sign/monotonicity/simulation assertions')
print('CDF n=2 t=2:',S.simplify(cdf_exact(2,2)))
print('CDF n=3 t=2:',S.simplify(cdf_exact(3,2)))
print('n=3 95% quantile lies in (2.2981,2.2982)')
