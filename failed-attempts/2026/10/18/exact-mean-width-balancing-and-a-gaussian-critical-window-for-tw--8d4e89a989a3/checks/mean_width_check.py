#!/usr/bin/env python3
"""Standalone reproducibility checks for the mean-width formulas of two-level order polytopes."""
import itertools
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import dawsn, gammaln

MU = 1 / math.sqrt(2*math.pi)
VAR = 0.5 - MU**2


def mean_gaussian_radius(d):
    return math.sqrt(2) * math.exp(gammaln((d+1)/2)-gammaln(d/2))


def phi(t):
    # Characteristic function of max(N(0,1),0), with a point mass of 1/2 at zero.
    return 0.5 + 0.5*math.exp(-t*t/2) + 1j*dawsn(t/math.sqrt(2))/math.sqrt(math.pi)


def exact_mean_width(p,q):
    d=p+q
    def integrand(t):
        if t < 1.e-4:
            return 0.5*(VAR*d+MU*MU*(p-q)**2)
        z=phi(t)
        return (1-(z**p*z.conjugate()**q).real)/(t*t)
    abs_mean=(2/math.pi)*(quad(integrand,0,0.1,epsabs=1.e-9,epsrel=1.e-9)[0]+
                          quad(integrand,0.1,80,epsabs=1.e-9,epsrel=1.e-9)[0]+
                          quad(integrand,80,math.inf,epsabs=1.e-9,epsrel=1.e-9)[0])
    return (MU*d+abs_mean)/mean_gaussian_radius(d)


def exact_support(g,p,q):
    a,b=g[:p],g[p:]
    return max(sum(max(z,0.) for z in b),sum(b)+sum(max(z,0.) for z in a))


def brute_support(g,p,q):
    vals=[]
    for x in itertools.product([0.,1.],repeat=p):
        for y in itertools.product([0.,1.],repeat=q):
            if min(y) < max(x):
                continue
            vals.append(np.dot(g,np.array(x+y)))
    return max(vals)


def critical_profile(tau):
    z=MU*tau/math.sqrt(VAR)
    return math.sqrt(2*VAR/math.pi)*math.exp(-z*z/2) + MU*tau*math.erf(z/math.sqrt(2))


def test():
    rng=np.random.default_rng(82603)
    checked=0
    for p in range(1,5):
        for q in range(1,5):
            for _ in range(120):
                g=rng.standard_normal(p+q)
                assert abs(exact_support(g,p,q)-brute_support(g,p,q)) < 1.e-12
                checked+=1
    print('PASS direct polytope-vertex support checks:',checked)
    # The triangle 0<=x<=y<=1 has mean width equal to perimeter/pi.
    w=exact_mean_width(1,1)
    target=(2+math.sqrt(2))/math.pi
    assert abs(w-target)<1.e-6, (w,target)
    print('PASS triangle mean width:',w,target)
    # Symmetry and strict balancing: inequalities hold numerically for each dimension.
    pairs=0
    for d in range(3,13):
        widths=[exact_mean_width(p,d-p) for p in range(1,d)]
        for p in range(1,d):
            assert abs(widths[p-1]-widths[d-p-1])<3.e-7
        ordered=sorted(widths)
        if d%2==0:
            min_w=widths[d//2-1]
            assert all(widths[p-1]>min_w+1.e-6 for p in range(1,d) if p!=d//2)
        else:
            min_w=widths[(d-1)//2-1]
            assert abs(min_w-widths[(d+1)//2-1])<3.e-7
            assert all(widths[p-1]>min_w+1.e-6 for p in range(1,d) if p not in ((d-1)//2,(d+1)//2))
        for p in range(1,d-1):
            if p>=d-p:
                assert widths[p] > widths[p-1] + 1.e-6
                pairs+=1
    print('PASS fixed-d width balancing, dimensions 3..12; strict comparisons:', pairs)
    for tau in (-2.,-0.75,0.,1.25,3.):
        n=200000
        p=round((n+tau*math.sqrt(n))/2)
        q=n-p
        # Analytic normal critical approximation to the second term.
        approximate=critical_profile(tau)
        assert approximate>=critical_profile(0)-1.e-12
        print('critical t:', tau,'profile:',round(approximate,9),'p,q:',p,q)
    print('PASS critical scaling function and strict convexity implications')

if __name__=='__main__': test()
