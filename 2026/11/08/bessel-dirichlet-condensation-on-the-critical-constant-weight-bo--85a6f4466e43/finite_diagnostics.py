"""Numerical finite-volume checks for the canonical critical-line expansion.

Run: python finite_diagnostics.py
"""
import math
import numpy as np
from scipy.stats import nbinom
from scipy.special import gammaln, logsumexp, iv


def log_binom(n,k):
    return gammaln(n+1)-gammaln(k+1)-gammaln(n-k+1)


def log_a(L,N,j,b,theta):
    if j==0: return nbinom.logpmf(N,L,1-b)
    m=L-j
    s=np.arange(N+1)
    if m:
        pmf=nbinom.logpmf(s,m,1-b)
    else:
        pmf=np.where(s==0,0,-np.inf)
    h=N-s
    logs=pmf+gammaln(h+j)-gammaln(j)-gammaln(h+1)
    return float(log_binom(L,j)+j*(math.log(theta)-2*math.log(L))+logsumexp(logs))


def main():
    b=.5; theta=1.; rho=2.; a=rho-b/(1-b)
    exact=math.sqrt(theta/a)*iv(1,2*math.sqrt(theta*a))
    for L in (50,100,200,400,800):
        N=int(rho*L)
        logs=np.array([log_a(L,N,j,b,theta) for j in range(13)])
        z=math.exp(logsumexp(logs))
        p=np.exp(logs-logsumexp(logs))
        print(f'L={L} LZ={L*z:.9f}; limit={exact:.9f}; P(J=1)={p[1]:.9f}; limit P1={theta/exact:.9f}; tail_approx={1-sum(p):.1e}')
        assert abs(L*z-exact) < 3.0/(L**.45)
    print('PASS: finite-volume diagnostics')

if __name__=='__main__':main()
