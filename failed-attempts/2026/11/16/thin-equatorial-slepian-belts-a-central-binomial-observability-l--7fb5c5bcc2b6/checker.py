#!/usr/bin/env python3
"""Check fixed-band spherical-belt Slepian asymptotics by exact polynomial moments."""
import math
import mpmath as mp
mp.mp.dps=90

def even_moment(k,m,a):
    if k%2: return mp.mpf('0')
    return 2*sum([(-1)**r*math.comb(m,r)*a**(k+2*r+1)/mp.mpf(k+2*r+1) for r in range(m+1)])

def block_min(L,m,a):
    n=L-m
    W=mp.matrix([[even_moment(i+j,m,a) for j in range(n+1)] for i in range(n+1)])
    G=mp.matrix([[even_moment(i+j,m,mp.mpf(1)) for j in range(n+1)] for i in range(n+1)])
    B=mp.cholesky(G); Binv=B**-1
    S=Binv*W*(Binv.T)
    ev,_=mp.eigsy(S)
    return ev[0]

def asymptotic(L,m):
    n=L-m
    kap=mp.mpf(math.comb(2*n,n))/2**n
    return (2/(mp.mpf(2*n+1)*kap**2))/mp.beta(mp.mpf(n)+mp.mpf('0.5'),m+1)

for L in range(1,6):
    for a_s in ['0.18','0.10','0.05']:
        a=mp.mpf(a_s)
        eigs=[block_min(L,m,a) for m in range(L+1)]
        ratio=eigs[0]/(a**(2*L+1)*asymptotic(L,0))
        assert eigs[0] == min(eigs), (L,a,[float(x) for x in eigs])
        assert mp.fabs(ratio-1)<mp.mpf('.14'),(L,a,ratio)
        print('L=',L,'a=',a_s,'zonal_ratio=',mp.nstr(ratio,12),'next_m_ratio=',mp.nstr(eigs[1]/eigs[0],8))
print('SPHERICAL_THIN_BELT_PASS')
