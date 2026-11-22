"""Independent finite spectral tests for the one-atom Hardy average.

The infinite-dimensional statements are proved analytically; these computations
only test root locations, trace identities, and finite Galerkin compressions.
"""
import math


def root(T, j):
    def phase(k):
        return T*k+3*math.atan(2*k)-j*math.pi
    lo, hi = 0.0, max(1.0, j*math.pi/T)
    while phase(hi)<0.0:
        hi *= 2
    for _ in range(100):
        mid=(lo+hi)/2
        if phase(mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def singular(T,j):
    k=root(T,j)
    return 2/math.sqrt(1+4*k*k)


def run():
    n=0
    # Spectral quantization, root simplicity, ordering, and exact trace.
    for beta in (0.001,0.01,0.1,1,10,100):
        T=math.log1p(1/beta)
        ss=[singular(T,j) for j in range(1,1001)]
        for j,s in enumerate(ss,1):
            k=root(T,j)
            assert abs(T*k+3*math.atan(2*k)-j*math.pi)<2e-11*(1+j)
            n+=1
            if j>1:
                assert ss[j-2]>s
                n+=1
        partial=sum(s*s for s in ss)
        target=1+T
        assert 0 < target-partial < 1.5*T*T/1000
        n+=1
        for j in (5,7,9):
            assert 0 < ss[j-1] < 2
            n+=1
    # Limit of the logarithmic edge at fixed rank.
    for T in (1000,3000,10000):
        for j in range(1,7):
            s=singular(T,j)
            target=4*math.pi**2*j*j
            scaled=T*T*(2-s)
            assert abs(scaled/target-1)<0.03
            n+=1
    # Large-atom limit: rank-one top and inverse-half-integer tail.
    for T in (0.001,0.003,0.01):
        s1=singular(T,1)
        assert abs((s1-1)/T-0.5)<0.005
        n+=1
        for j in (2,3,4,5):
            target=1/((j-1.5)*math.pi)
            assert abs(singular(T,j)/T/target-1)<0.02
            n+=1
    try:
        import numpy as np
        from scipy.linalg import svdvals
        # Exact matrix of Galerkin compression onto atom + interval-step functions.
        for beta in (0.1,1,10):
            T=math.log1p(1/beta)
            for m in (80,160):
                mat=np.zeros((m+1,m+1))
                mat[0,0]=1.0
                for i in range(1,m+1):
                    left=(i-1)/m;right=i/m
                    d=math.log1p(1/(m*(beta+left)))
                    mat[i,0]=math.sqrt(beta*m)*d
                    mat[i,1:i]=d
                    mat[i,i]=1-m*(beta+left)*d
                vals=svdvals(mat)
                for j in (1,2,3):
                    assert abs(vals[j-1]-singular(T,j))<0.06
                    n+=1
    except ImportError:
        pass
    print('ATOMIC_HARDY_SPECTRAL_DIAGNOSTIC_OK', n)


if __name__=='__main__':
    run()
