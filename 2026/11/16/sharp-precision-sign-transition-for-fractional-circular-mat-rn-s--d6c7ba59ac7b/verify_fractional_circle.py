#!/usr/bin/env python3
"""Standalone numerical corroboration for fractional circular covariance precision.

Nontrivial universal statements rest on the paper's proof, not these finite tests.
"""
import math
import mpmath as mp

mp.mp.dps = 60

def residue_sum(s, k, r, terms=45):
    """S_r=sum_{m congruent r (4)}(k^2+m^2)^(-s), for k<1."""
    r %= 4
    def b(p):
        if r == 0:
            return 2*mp.power(4, -p)*mp.zeta(p)
        if r == 2:
            return 2*mp.power(4, -p)*mp.zeta(p, mp.mpf('0.5'))
        return mp.power(4, -p)*(mp.zeta(p, mp.mpf('0.25'))+mp.zeta(p, mp.mpf('0.75')))
    val = mp.power(k, -2*s) if r == 0 else mp.mpf('0')
    coef = mp.mpf('1')
    for j in range(terms):
        val += coef * mp.power(k, 2*j) * b(2*s+2*j)
        coef *= -(s+j)/(j+1)
    return val

def opposite_precision(s,k):
    ss = [residue_sum(s,k,r) for r in range(4)]
    return (1/ss[0]+1/ss[2]-2/ss[1])/16

count = 0
print('Four-grid low-mass opposite-site precision checks (60-digit arithmetic)')
for s in [mp.mpf('0.625'), mp.mpf('0.75'), mp.mpf('0.9'), mp.mpf('1.0'), mp.mpf('1.1'), mp.mpf('1.5'), mp.mpf('2.0')]:
    k = mp.mpf('0.05')
    q = opposite_precision(s,k)
    O = (1-mp.power(2,-2*s))*mp.zeta(2*s)
    lim = (mp.power(2,2*s-1)-2)/(16*O)
    assert abs(q-lim)<mp.mpf('0.02')
    if s>1: assert q>0 and lim>0
    if s==1: assert q<0 and abs(lim)<mp.mpf('1e-40')
    if s<1: assert q<0 and lim<0
    count += 3
    print('s=',mp.nstr(s,5),'Q(0,2)=',mp.nstr(q,15),'limit=',mp.nstr(lim,15))

print('Unit-order exact cyclic precision cross-check for irregular sampling')
for n in [3,4,6,8]:
    pts = [mp.mpf('0.02') + 2*mp.pi*mp.mpf(j)/n + mp.mpf('0.08')*mp.sin(mp.mpf(j)+1) for j in range(n)]
    pts = sorted(pts)
    for kap in [mp.mpf('0.3'),mp.mpf('1.2')]:
        # K_{1,kappa}(theta) = pi/kappa*cosh(kappa*(pi-distance))/sinh(pi*kappa)
        def K(a,b):
            delta = abs(a-b)
            distance = min(delta,2*mp.pi-delta)
            return mp.pi/kap*mp.cosh(kap*(mp.pi-distance))/mp.sinh(mp.pi*kap)
        S = mp.matrix([[K(pts[i],pts[j]) for j in range(n)] for i in range(n)])
        Q = S**-1
        for i in range(n):
            for j in range(i+1,n):
                ell = (pts[(i+1)%n]-pts[i]) % (2*mp.pi)
                ell_back = (pts[(j+1)%n]-pts[j]) % (2*mp.pi)
                formula=mp.mpf('0')
                if j==(i+1)%n: formula-=kap/(2*mp.pi*mp.sinh(kap*ell))
                if i==(j+1)%n: formula-=kap/(2*mp.pi*mp.sinh(kap*ell_back))
                assert mp.almosteq(Q[i,j],formula, rel_eps=mp.mpf('1e-50'), abs_eps=mp.mpf('1e-50'))
                count += 1
print('PASS:',count,'standalone high-precision assertions; analytic universal proof independent.')
