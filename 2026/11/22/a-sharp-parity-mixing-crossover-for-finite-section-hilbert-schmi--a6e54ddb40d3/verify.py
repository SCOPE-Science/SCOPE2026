"""Finite diagnostics for the two-shift Hilbert--Schmidt condenser theorem.

Requires Python 3 and numpy. Finite checks do not prove asymptotics.
"""
import numpy as np
import math


def solve(N, eps):
    assert N % 2 == 0 and N >= 4 and eps >= 0
    # Dirichlet graph, grounded at j>=N, with d_0 = 1.
    A = np.zeros((N-1, N-1))
    b = np.zeros(N-1)
    for gap, conductance in ((1, eps*eps), (2, 1.0)):
        for j in range(N):
            k = j + gap
            if conductance == 0:
                continue
            if j >= 1:
                A[j-1, j-1] += conductance
            if 1 <= k < N:
                A[k-1, k-1] += conductance
            if j >= 1 and k < N:
                A[j-1, k-1] -= conductance
                A[k-1, j-1] -= conductance
            if j == 0 and k < N:
                b[k-1] += conductance
    d = np.concatenate(([1.], np.linalg.solve(A, b), [0., 0.]))
    ds = np.zeros(N+2)
    ds[:N] = d[:N]
    E = sum((ds[j]-ds[j+2])**2 for j in range(N))
    E += eps*eps * sum((ds[j]-ds[j+1])**2 for j in range(N))
    assert np.min(ds) >= -1e-10 and np.max(ds) <= 1+1e-10
    assert np.linalg.norm(A @ ds[1:N]-b) < 1e-8
    return E, ds


def phi(c):
    if c == 0:
        return 2.
    k = c / math.tanh(c)
    return 4*k/(1+k)


def profile(c, t):
    if c == 0:
        return (1-t, 0.)
    k = c/math.tanh(c)
    u = k/(1+k)*(1-t)
    v = math.sinh(c*(1-t))/math.sinh(c)/(1+k)
    return u+v, u-v


def main():
    count=0
    for c in (0., 0.4, 1., 2., 4.):
        for N in (40, 100, 200):
            E,d=solve(N,c/N)
            expected=phi(c)
            # O(1/N) mesh accuracy, finite diagnostics only
            assert abs(N*E-expected) < 30/N, (N,c,N*E,expected)
            count += 1
            for k in (0, N//8, N//4, 3*N//8, N//2):
                x,y=profile(c, 2*k/N)
                assert abs(d[2*k]-x) < 12/N, (N,c,k,d[2*k],x)
                if 2*k+1<N:
                    assert abs(d[2*k+1]-y) < 12/N, (N,c,k,d[2*k+1],y)
                count+=1
    for N in (20,40,100):
        E,d=solve(N,0)
        assert abs(E-2/N) < 1e-10
        assert max(abs(d[j]-(1-j/N)) for j in range(0,N,2))<1e-10
        assert max(abs(d[j]) for j in range(1,N,2))<1e-10
        count += 3
    for N in (40,100,200):
        eps=1/math.sqrt(N)
        E,_=solve(N,eps)
        assert abs(N*E-4)<8/math.sqrt(N), (N,N*E)
        count+=1
    print('VERIFY_OK',count,'finite assertions')

if __name__=='__main__':
    main()
