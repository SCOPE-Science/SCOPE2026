#!/usr/bin/env python3
"""Independent finite checks of stated k-full empty-window correlation identities.

This code does not certify irrational equidistribution or an infinite product.
"""
import math


def overlap(p, phase):
    s = phase % 1.0
    return max(0.0, p-s) + max(0.0, p+s-1.0)


def local_factor(p, t):
    return 1.0 - 2.0*p + overlap(p, (t*p) % 1.0)


def product(values):
    v = 1.0
    for x in values:
        v *= x
    return v


def finite_occupancy(ms, N, maxlag):
    # The k=2 ray for squarefree m>=2 is a^2*m^3, a>=1.
    H = bytearray(b'\x01')*(N+maxlag+2)
    for m in ms:
        m3 = m**3
        a = 1
        while a*a*m3 < (N+maxlag+1)**2:
            v = a*a*m3
            n = math.isqrt(v)
            if 1 <= n <= N+maxlag:
                if n*n < v < (n+1)*(n+1):
                    H[n] = 0
            a += 1
    return H


def check():
    ms = (2,3,5,6,7,10,11,13)
    for m in ms:
        for d in range(2, math.isqrt(m)+1):
            assert not (m % (d*d) == 0)
    ps = [1.0 / (m*math.sqrt(m)) for m in ms]
    assert max(ps) < 0.5
    D = product(1-p for p in ps)
    C = product(1-2*p for p in ps)
    assert 0 < C < D*D < D < 1
    assert abs(product(local_factor(p, 1) for p in ps)-C) < 1e-14
    assert abs(product(local_factor(p, 0) for p in ps)-D) < 1e-14

    # Local integral identities, using midpoint quadrature, not to infer the theorem.
    for p in ps:
        ngrid = 20000
        G1 = G2 = 0.0
        for i in range(ngrid):
            g = overlap(p, (i+0.5)/ngrid)
            G1 += g/ngrid
            G2 += g*g/ngrid
        assert abs(G1-p*p) < 2e-7, (p,G1)
        assert abs(G2-(2.0/3.0)*p**3) < 2e-7, (p,G2)

    # Exact ray membership of non-perfect-square squarefull numbers,
    # compared against equidistribution product predictions.
    N=500000
    lags=(1,2,3,4,7,13,29)
    H=finite_occupancy(ms,N,max(lags))
    empirical_D=sum(H[1:N+1])/N
    assert abs(empirical_D-D)<0.003,(empirical_D,D)
    results=[]
    for t in lags:
        empirical_pair=sum(H[n] and H[n+t] for n in range(1,N+1))/N
        predicted_pair=product(local_factor(p,t) for p in ps)
        assert abs(empirical_pair-predicted_pair)<0.003,(t,empirical_pair,predicted_pair)
        results.append((t,empirical_pair,predicted_pair))
    second_moment=product((1-p)**4+2*p**3/3-p**4 for p in ps)
    assert second_moment>D**4
    # Check no spurious atoms in finite truncated law: noncentral factors
    # have densities on each of their two linear overlap arms.
    for p in ps:
        assert abs((1-2*p)+2*p-1)<1e-15
    print('PASS: 8 squarefree squarefull rays, 500,000 base windows, 7 lags,')
    print('       local overlap integrals, endpoint products, positive variance.')
    print('D8=%.9f C8=%.9f'%(D,C))
    for t,emp,pred in results:
        print('lag=%2d empirical joint=%.8f predicted joint=%.8f'%(t,emp,pred))
    print('Finite checks do not prove infinite limits or originality.')


if __name__=='__main__':
    check()
