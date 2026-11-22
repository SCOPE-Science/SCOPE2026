#!/usr/bin/env python3
"""Reproducible numerical diagnostics for logarithmic-endpoint Poisson-mixture extremes.

The infinite limits are proved analytically; these finite diagnostics do not certify them.
Requires mpmath. Run: python mixed_poisson_endpoint_checker.py
"""
import mpmath as mp
mp.mp.dps = 175


def tc(c):
    c=mp.mpf(c)
    return mp.findroot(lambda t:t*mp.log(t/c)-t+c-1,
                       (c+mp.sqrt(c), c+2+mp.sqrt(c)))


def params(c, alpha=1, H=1):
    c=mp.mpf(c); a=mp.mpf(alpha); H=mp.mpf(H)
    t=tc(c); r=mp.log(t/c)
    K=H*mp.gamma(a)*mp.sqrt(t)/(mp.sqrt(2*mp.pi)*(t-c)**(a+1))
    return t,r,K


def poi_tail(k,L):
    return mp.gammainc(k,0,L,regularized=True)


def unif_mix_tail(k,L):
    return poi_tail(k,L)-mp.mpf(k)/L*poi_tail(k+1,L)


def asympt_tail(k,L,c=1,alpha=1,H=1):
    ell=L/mp.mpf(c);t,r,K=params(c,alpha,H)
    return mp.exp(-ell)*K*ell**(-mp.mpf(alpha)-mp.mpf('0.5'))*mp.exp(-r*(k-t*ell))


def unif_mix_pmf(k,L):
    return poi_tail(k+1,L)/L


def verify():
    checks=0
    for c in [mp.mpf('0.5'),mp.mpf(1),mp.mpf(2)]:
        t,r,K=params(c)
        assert t>c and r>0 and K>0;checks+=3
        assert abs(t*mp.log(t/c)-t+c-1)<mp.mpf('1e-55');checks+=1
        for ell in [mp.mpf(50),mp.mpf(120),mp.mpf(250)]:
            L=c*ell
            b=t*ell-mp.mpf('1.5')*mp.log(ell)/r+mp.log(K)/r
            k=int(mp.ceil(b))
            actual=unif_mix_tail(k,L)
            ap=asympt_tail(k,L,c)
            rat=actual/ap
            # Convergence is slow but unmistakable by these large-log samples.
            assert mp.mpf('0.75')<rat<mp.mpf('1.3'),(c,ell,rat)
            checks+=1
            # Density ratio for adjoining lattice exceedances is geometric.
            tail_next=unif_mix_tail(k+1,L)/actual
            assert abs(tail_next-c/t)<mp.mpf('0.07'), (c,ell,tail_next,c/t)
            checks+=1
            # Exact mixing identity by integrating the conditional Poisson tail.
            if ell == 50:
                quadrature=mp.quad(lambda lam:poi_tail(k,lam)/L,[0,L/2,L])
                assert abs(quadrature/actual-1)<mp.mpf('1e-32')
                checks+=1
    # General Beta(1, alpha) endpoint shapes, including a singular density.
    # If V is uniform then U=1-V**(1/alpha) has Beta(1,alpha) density.
    for alpha in [mp.mpf('0.5'), mp.mpf(2)]:
        t,r,K=params(1,alpha,H=alpha)
        for ell in [mp.mpf(50),mp.mpf(120)]:
            b=t*ell-(alpha+mp.mpf('0.5'))*mp.log(ell)/r+mp.log(K)/r
            k=int(mp.ceil(b))
            actual=mp.quad(lambda v:poi_tail(k,ell*(1-v**(1/alpha))),[0,mp.mpf('0.5'),1])
            ap=asympt_tail(k,ell,c=1,alpha=alpha,H=alpha)
            assert mp.mpf('0.8')<actual/ap<mp.mpf('1.2'),(alpha,ell,actual/ap)
            checks+=1
    # The c=1 saddle is exactly Euler's number.
    assert abs(tc(1)-mp.e)<mp.mpf('1e-55');checks+=1
    # Check the independent Gamma/Geometric limit via normalized joint kernels.
    c=mp.mpf(1);ell=mp.mpf(250);L=c*ell
    t,r,K=params(c)
    b=t*ell-mp.mpf('1.5')*mp.log(ell)/r+mp.log(K)/r
    k=int(mp.ceil(b)); tail=unif_mix_tail(k,L)
    for s in [mp.mpf('0.5'),mp.mpf(1),mp.mpf(2)]:
        # Uniform intensity mixing: joint density of S=L-Lambda and X=k+j.
        for j in range(4):
            lam=L-s
            exact=(mp.exp(-lam)*lam**(k+j)/mp.factorial(k+j))/L/tail
            pred=(t/c-1)*mp.exp(-(t/c-1)*s)*(1-c/t)*(c/t)**j
            assert abs(exact/pred-1)<mp.mpf('0.12'),(s,j,exact/pred)
            checks+=1
    print('PASS:',checks,'numerical assertions; limits require the analytical proof')
    print('c=1 threshold t=',mp.nstr(t,22),'K=',mp.nstr(K,22))
    print('example b_n = e log n - 1.5 log log n + log K')


if __name__=='__main__':
    verify()
