"""Finite consistency checks for the axial Hartogs kernel and moment-variance formula.

Numerical truncation is not a proof of any asserted asymptotic theorem.
"""
import math
import numpy as np
from scipy.special import roots_legendre, logsumexp


def estimate(alpha, delta, quadrature_order=280):
    # q=exp(1-t), so dq=exp(1-t) dt, integrate t from 1 to 41.
    # For alpha>=1.5 the excluded tail decays below working precision.
    nodes, weights = roots_legendre(quadrature_order)
    t = 21 + 20*nodes
    w = 20*weights
    logu = np.log1p(-np.exp(1-t))
    constant = 1-t-2*t**alpha + np.log(w)
    x = -np.log1p(-delta)
    leading_B = 2*alpha * math.log(math.e/delta)**(alpha-1)
    nmax = int(8*leading_B / delta + 1000)
    nums = np.arange(nmax+1, dtype=float)
    chunks=[]
    for lo in range(0, nmax+1, 600):
        n=nums[lo:lo+600]
        logmu=logsumexp(n[:,None]*logu[None,:]+constant[None,:],axis=1)
        chunks.append(-logmu -n*x)
    a=np.concatenate(chunks)
    peak=int(np.argmax(a))
    logZ=logsumexp(a)
    p=np.exp(a-logZ)
    mean=float(p@nums)
    var=float(p@((nums-mean)**2))
    # Check truncation is negligible and the variance is positive.
    assert np.isfinite(var) and var>0
    assert peak>200 and peak<nmax-500
    assert p[-1]<1e-16 and p[0]<1e-8
    # The variance is also the curvature of log(sum s^n/mu_n), as shown exactly
    # by differentiating the finite sum: this is checked with finite differences.
    h = min(x*2e-4, 5e-7)
    # For fixed coefficients at the same n, log Z(x±h) differs by ∓nh.
    logs_plus=logsumexp(a-nums*h)
    logs_minus=logsumexp(a+nums*h)
    fd=(logs_plus-2*logZ+logs_minus)/h**2
    assert abs(fd/var-1)<0.015, (fd, var)
    predicted=leading_B/delta**2
    return var/predicted,peak,nmax


def main():
    outputs=[]
    for alpha in (1.5,2.0):
        prev=None
        for delta in (0.02,0.01,0.005):
            ratio,peak,nmax=estimate(alpha,delta)
            assert 0.9<ratio<2.0
            if prev is not None:
                assert ratio<prev, (alpha,delta,ratio,prev)
            outputs.append((alpha,delta,ratio,peak,nmax))
            prev=ratio
    for row in outputs:
        print('alpha delta variance_over_asymptotic mode cutoff:', row)
    print('6 finite curvature/variance checks completed; not a proof of the limit.')

if __name__=='__main__':
    main()
