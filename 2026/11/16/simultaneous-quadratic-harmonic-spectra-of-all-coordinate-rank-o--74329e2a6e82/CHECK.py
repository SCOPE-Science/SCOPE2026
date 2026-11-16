"""Reproduce the scalar spectra for coordinate-order observation masks.
Run with Python 3.10+; standard library only. Quadrature is numerical, not a proof.
"""
import math
import random

SQRT2PI = math.sqrt(2 / math.pi)

def spectral_rank(d, r, panels=100000):
    assert isinstance(d, int) and d >= 4 and 1 <= r <= d
    assert panels % 2 == 0
    n, k, ell = d-1, r-1, d-r
    dt = 12.0/panels
    accum = [0.0]*4
    norm = 0.0
    for i in range(panels):
        u = (i+0.5)*dt
        f = SQRT2PI*math.exp(-u*u/2)
        F = math.erf(u/math.sqrt(2))
        U = math.erfc(u/math.sqrt(2))
        if F == 0 or U == 0: continue
        w = d*math.comb(n,k)*(U**k)*(F**ell)*f*dt
        lower1 = F-u*f
        lower2 = 3*F-u*f*(u*u+3)
        a1 = (1-lower1)/U if k else 0.0
        b1 = lower1/F if ell else 0.0
        a2 = (3-lower2)/U if k else 0.0
        b2 = lower2/F if ell else 0.0
        m = k*a1+ell*b1
        var = k*(a2-a1*a1)+ell*(b2-b1*b1)
        Q = (k*a2+ell*b2)/n
        P = (k*(k-1)*a1*a1+ell*(ell-1)*b1*b1+2*k*ell*a1*b1)/(n*(n-1))
        z = ((n*u*u-m)**2+var)/(2*d*n)
        vals = [z, u*u*m/n, P, (Q-P)/2]
        for j in range(4): accum[j] += w*vals[j]/(2*d)
        norm += w
    assert abs(norm-1) < 2.e-4, (d,r,norm)
    return accum

def test_sums():
    for d in (4,5,6,8,12):
        all_lam = [spectral_rank(d,r,panels=12000) for r in range(1,d+1)]
        for j in range(4):
            assert abs(sum(z[j] for z in all_lam)-0.5) < 5.e-5, (d,j)
        weights = [1,d-1,(d-1)*(d-2)//2,d-2]
        assert sum(weights) == d*(d+1)//2-1
        for r,row in enumerate(all_lam,1):
            assert all(0 < x < 1 for x in row)
            assert abs(sum(a*b for a,b in zip(weights,row))-(sum(weights)/(2*d))) < 2.e-5,(d,r,row)
    print('Partition completeness, exact multiplicity counts and area trace: PASS')

def independent_gaussian_test(d=4,r=2,samples=450000):
    rng=random.Random(20261114)
    accum=[0.0]*4
    count=0
    for z in range(samples):
        g=[rng.gauss(0,1) for i in range(d)]
        y=[t*t for t in g]
        if g[0] <= 0 or sum(y[j]>y[0] for j in range(1,d)) != r-1:continue
        count += 1
        # Representatives for zonal, mixed, transverse off-diagonal, transverse diagonal.
        x=[(d-1)*y[0]-sum(y[1:]),g[0]*g[1],g[1]*g[2],y[1]-y[2]]
        denom=[2*d*(d-1),1,1,4]
        for i in range(4): accum[i]+=x[i]*x[i]/denom[i]
    empirical=[q/samples for q in accum]
    exact=spectral_rank(d,r)
    print('Gaussian samples inside rank cell:',count,'of',samples)
    print('Direct Gaussian-moment estimate:',empirical)
    print('One-dimensional quadrature:',exact)
    for a,b in zip(empirical,exact):
        assert abs(a-b)<0.011,(a,b)
    print('Independent direct-sample comparison: PASS')

if __name__ == '__main__':
    test_sums()
    independent_gaussian_test()
    for d,r in [(4,2),(5,2),(8,2),(20,2)]:
        print('Example dimension/rank',d,r, spectral_rank(d,r))
