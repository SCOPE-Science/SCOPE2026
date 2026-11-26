"""Reproducible checks for rare one-gap and two-gap circular exceedances.

These finite checks complement, but do not replace, the analytic Poisson proof.
"""
import math
import numpy as np


def overlap_12(u, v):
    assert v >= u >= 0
    return (v-u+1)*math.exp(-v)


def overlap_22(v):
    assert v >= 0
    return 2*math.exp(-v)-math.exp(-2*v)


def check_geometry(gaps, ell):
    """Return (complete coverage, coverage after every one-site deletion)."""
    n=len(gaps)
    assert n>=3 and all(g>0 for g in gaps) and abs(sum(gaps)-1)<1e-10
    ordinary=max(gaps)<=ell
    robust=all(max(gaps[(j-1)%n]+gaps[j], max(gaps[k] for k in range(n) if k not in ((j-1)%n,j)))<=ell for j in range(n))
    assert robust == (max(gaps[j]+gaps[(j+1)%n] for j in range(n))<=ell)
    return ordinary, robust


def main():
    rng=np.random.default_rng(20261120)
    tests=0
    for n in range(3,14):
        for _ in range(30):
            e=rng.exponential(size=n)
            g=(e/e.sum()).tolist()
            for ell in (0.04,0.1,0.2,0.3,0.5,0.8,1.0):
                check_geometry(g,ell)
                tests+=1
    # Compare the analytic overlapping-pair integrals against direct quadrature.
    from scipy.integrate import quad
    for u,v in [(0.2,0.3),(2,2.5),(5,8),(10,13),(16,19)]:
        p,_=quad(lambda t: math.exp(-t)*math.exp(-(v-t)),u,v,epsabs=1e-14)
        p+=math.exp(-v)
        assert abs(p-overlap_12(u,v))<2e-12
        tests+=1
        p,_=quad(lambda t: math.exp(-t)*math.exp(-2*(v-t)),0,v,epsabs=1e-14)
        p+=math.exp(-v)
        assert abs(p-overlap_22(v))<2e-12
        tests+=1
    # Verify the mixed overlap contribution vanishes at the claimed logarithmic scales.
    vals=[]
    for n in [10000,100000,1000000,10000000]:
        u=math.log(n)
        v=math.log(n)+math.log(math.log(n))
        vals.append(n*(overlap_12(u,v)+overlap_22(v)))
    assert all(vals[j+1]<vals[j] for j in range(3))
    tests+=3
    # Random checks are descriptive only, and use the exact exponential-spacings coupling.
    n=2000
    R=6000
    e=rng.exponential(size=(R,n))
    g=e/e.sum(axis=1)[:,None]
    c1=np.max(n*g,axis=1)-math.log(n)
    c2=np.max(n*(g+np.roll(g,1,axis=1)),axis=1)-math.log(n)-math.log(math.log(n))
    for x,y in [(0,0),(-0.2,0.4),(0.6,-0.1)]:
        observed=np.mean((c1<=x)&(c2<=y))
        expected=math.exp(-math.exp(-x)-math.exp(-y))
        assert abs(observed-expected)<0.13, (x,y,observed,expected)
        tests+=1
    print(f'PASS: {tests} deterministic/analytic geometry, integration, and simulation checks')
    print('finite simulation is not a proof of weak convergence')
    print('overlap bounds',vals)

if __name__=='__main__': main()
