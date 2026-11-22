"""Reproduce finite algebra and finite-n numerical checks for a geometric zero-frequency statistic.
Run: python check.py ; only standard library plus NumPy (for supplementary Monte Carlo).
"""
from fractions import Fraction as F
from itertools import product
from math import comb, exp, sqrt

assertions=0

def verify(condition, description):
    global assertions
    if not condition: raise AssertionError(description)
    assertions += 1

# The exact standardized statistic is Z=(H-K)/(qhat*sqrt(H)),
# where H=n^2/(n+S), qhat=S/(n+S), K=#zeros.
# The numerator is equal to S^2/(n+S)-D, D=sum(max(Xi-1,0)).
for n in range(2,6):
    for xs in product(range(5),repeat=n):
        S=sum(xs); K=sum(x==0 for x in xs); D=sum(max(x-1,0) for x in xs)
        H=F(n*n,n+S)
        verify(H-K == F(S*S,n+S)-D, 'exact numerator decomposition')
        if S:
            mu=F(S,n); p_hat=1/(1+mu)
            sig2=mu*mu/(1+mu)**3
            # compare Z^2 to avoid square roots of rational numbers
            z2= F(n)*(p_hat-F(K,n))**2/sig2
            z2_reduced=(H-K)**2*F((n+S)**3,S*S*n*n)
            verify(z2==z2_reduced,'exact studentization algebra')

# Independent elementary moment check. P(X=0)=p, E X=q/p, Var X=q/p^2,
# Cov(X,1_0)=-q. Y=p^2(X-mu)+(1_0-p).
for numerator in range(1,20):
    for denom in range(numerator+1,21):
        p=F(numerator,denom); q=1-p
        mu=q/p; varx=q/p**2
        vary=p**4*varx+p*q-2*p**2*q
        verify(vary==p*q*q, 'variance of centered score')
        verify(mu*mu/(1+mu)**3==p*q*q,'variance in published form')

# Exact finite joint PMF P(K=k,S=s) and conditional K|S=s: two independent derivations
# using weak compositions and sum over K.
for n in range(2,8):
    for s in range(1,20):
        normalizer=comb(n+s-1,n-1)
        total=sum(comb(n,k)*comb(s-1,n-k-1) for k in range(n) if n-k<=s)
        verify(total==normalizer,'Vandermonde composition identity')
        for k in range(n):
            if n-k<=s:
                conditional=F(comb(n,k)*comb(s-1,n-k-1),normalizer)
                verify(0<=conditional<=1,'valid conditional mass')


# Exact conditional p-value for observed (s,k), parameter-free under the geometric model.
for n in range(2,10):
    for s in range(1,30):
        den=comb(n+s-1,n-1)
        pmf={k:F(comb(n,k)*comb(s-1,n-k-1),den)
             for k in range(n) if n-k<=s}
        H=F(n*n,n+s)
        pvals={k:sum((v for j,v in pmf.items()
                      if abs(j-H)>=abs(k-H)),F(0)) for k in pmf}
        for alpha_index in range(0,21):
            alpha=F(alpha_index,20)
            size=sum((v for k,v in pmf.items() if pvals[k]<=alpha),F(0))
            verify(size<=alpha,'conditional exact-p superuniformity')

# Existence of a concrete overrejection critical window in both endpoint regimes.
from statistics import NormalDist
c=NormalDist().inv_cdf(.975)
lam_star=((sqrt(c*c+4)-c)/2)**2
verify(0.176<lam_star<0.177,'critical lambda window')
verify(.16 <1-exp(-lam_star)<.163,'Poisson upper-tail size')
lam=F(1,6)
verify((1-float(lam))/sqrt(float(lam))>c,'one-zero rejection')
verify(sqrt(float(lam))<c,'zero-zero acceptance')
verify(1-exp(-float(lam))>.15,'size inflation at rational intensity')

try:
    import numpy as np
    rng=np.random.default_rng(20261115)
    m=40000
    for direction in ('p_to_zero','p_to_one'):
        n=20000 if direction=='p_to_zero' else 100000000
        intensity=1/6
        if direction=='p_to_zero': p=intensity/n
        else: p=1-sqrt(intensity/n)
        k=rng.binomial(n,p,size=m)
        positive=n-k
        S=positive+rng.negative_binomial(positive,p)
        D=S-positive
        H=n*n/(n+S)
        denominator=(S*n)/(n+S)**1.5
        Z=np.where(denominator>0,(S*S/(n+S)-D)/denominator,0)
        empirical=float(np.mean(np.abs(Z)>c))
        expected=1-exp(-intensity)
        verify(abs(empirical-expected)<.025, 'rare boundary MC size')
        print(f'{direction}: n={n}, nominal=.05, simulated rejection={empirical:.6f}, asymptotic={expected:.6f}')
except ImportError:
    print('NumPy missing: finite algebra checks passed; Monte Carlo skipped')

print(f'ALL {assertions} CHECKS PASSED; lambda_star={lam_star:.12f}; limiting_size_sup_lower_bound={1-exp(-lam_star):.12f}')
