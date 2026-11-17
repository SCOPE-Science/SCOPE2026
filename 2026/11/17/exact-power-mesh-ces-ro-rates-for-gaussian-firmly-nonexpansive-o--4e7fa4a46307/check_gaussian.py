#!/usr/bin/env python3
"""Reproducible finite diagnostics for a power-mesh Gaussian Gram asymptotic.
These finite experiments do not prove the limiting theorem.
"""
import math
import numpy as np
from scipy.special import zeta


def finite_sum(alpha, delta, n):
    j = np.arange(1, n+1, dtype=float)
    steps = delta*j**(-alpha)
    t = np.zeros(n, dtype=float)
    t[1:] = np.cumsum(steps[:-1])
    rho = np.exp(-np.r_[0., np.cumsum(steps[:-1]**2)])
    total = 0.
    for i in range(n):
        total += rho[i] * float(np.dot(rho, np.exp(-(t[i]-t)**2)))
    return total/n**2


def limit(alpha, delta):
    return math.exp(-2*delta*delta*float(zeta(2*alpha, 1.0))) * math.sqrt(math.pi)/(delta*(1+alpha))


def main():
    trials = [(0.6, 0.3, (256, 1024, 4096)), (0.75, 0.4, (256, 1024, 4096)), (0.55, 0.07, (256, 1024))]
    for alpha, delta, ns in trials:
        c = limit(alpha,delta)
        vals=[]
        for n in ns:
            val=finite_sum(alpha,delta,n)*n**(1-alpha)
            assert 0 < val < float('inf')
            vals.append(val/c)
            print(f'alpha={alpha} delta={delta} n={n} normalized={val:.10f} predicted={c:.10f} ratio={val/c:.8f}')
        if delta>=0.3: assert abs(vals[-1]-1) < abs(vals[0]-1) and abs(vals[-1]-1) < 0.25
    for alpha in (0.51, 0.6, 0.75, 0.99):
        delta = math.sqrt(alpha*2**(alpha-1))/8
        for n in range(1, 10001):
            d_n=delta*n**(-alpha)
            d_next=delta*(n+1)**(-alpha)
            assert d_n<=.125 and (1/d_next-1/d_n+1.e-11)>=64*d_n
    print('PASS: finite Gaussian Gram diagnostics and 40000 admissible-mesh checks')


if __name__=='__main__':main()
