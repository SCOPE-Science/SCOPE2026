#!/usr/bin/env python3
"""Independent high-precision finite-band checks for polar cap concentration.
The proof covers every fixed L. This code checks finite cases only.
Requires mpmath.
"""
from math import comb, factorial
import mpmath as mp
mp.mp.dps=110

def moments(L,m,h):
    n=L-m
    G=mp.matrix(n+1); E=mp.matrix(n+1)
    for i in range(n+1):
        for j in range(n+1):
            q=i+j+m
            G[i,j]=mp.power(2,i+j+2*m)*mp.beta(q+1,m+1)
            # Polynomial exact integration, finite sum.
            E[i,j]=mp.fsum([(-1)**k*comb(m,k)*mp.power(2,m-k-1)*h**(q+k+1)/(q+k+1)
                                  for k in range(m+1)])
    return G,E

def eigen(L,m,h):
    G,E=moments(L,m,h)
    C=mp.cholesky(G)
    I=C**-1
    A=I*E*I.T
    return list(mp.eigsy(A,eigvals_only=True))

def small_coefficient(L,m):
    n=L-m
    return 2**(m-1-2*L) / (mp.beta(2*L-m+1,m+1)*(2*L-m+1)*comb(2*L-m,n)**2)

max_error=mp.mpf('0')
for L in range(0,6):
    for m in range(L+1):
        h=mp.mpf('0.001')
        vals=eigen(L,m,h)
        assert all(z>0 for z in vals)
        scale=h**(2*L-m+1)*small_coefficient(L,m)
        ratio=vals[0]/scale
        # Fractional correction to limit should be under 3% for this h.
        assert abs(ratio-1)<mp.mpf('0.04'),(L,m,ratio)
        max_error=max(max_error,abs(ratio-1))
    if L:
        blocks=[eigen(L,m,h) for m in range(L+1)]
        assert min(z for row in blocks for z in row)==blocks[0][0]
        mx=max(z for row in blocks for z in row)
        assert abs(mx/(mp.mpf((L+1)**2)*h/2)-1)<mp.mpf('0.04')
        cond=mx/blocks[0][0]
        expected=(L+1)**2*(2**(2*L))*comb(2*L,L)**2*h**(-2*L)
        assert abs(cond/expected-1)<mp.mpf('0.04')
# Independently extract the least zonal eigenvector and compare its rescaled
# polynomial with the monic shifted Legendre polynomial.
node_error=mp.mpf('0')
for L in range(1,6):
    m=0; h=mp.mpf('0.001')
    G,E=moments(L,m,h)
    Ch=mp.cholesky(G); Inv=Ch**-1
    A=Inv*E*Inv.T
    vals,Vec=mp.eigsy(A)
    c=Inv.T*mp.matrix([Vec[j,0] for j in range(L+1)])
    den=c[L]*h**L
    assert abs(den)>mp.mpf('1e-80')
    for u in [mp.mpf('0.13'),mp.mpf('0.32'),mp.mpf('0.71'),mp.mpf('0.91')]:
        observed=mp.fsum(c[j]*(h*u)**j for j in range(L+1))/den
        predicted=mp.legendre(L,2*u-1)/comb(2*L,L)
        err=abs(observed-predicted)
        assert err<mp.mpf('0.02'),(L,u,err)
        node_error=max(node_error,err)
print('POLAR_CAP_FIXED_BAND_PASS')
print('L=0..5,m=0..L; h=1/1000; max_asymptotic_relative_error=',mp.nstr(max_error,8))
print('zonal_polynomial_shape_max_error=',mp.nstr(node_error,8))
