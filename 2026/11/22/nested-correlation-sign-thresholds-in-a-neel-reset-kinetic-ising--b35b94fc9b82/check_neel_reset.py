#!/usr/bin/env python3
"""Independent finite-state generator checks for a zero-temperature spin chain."""
import math
import numpy as np
from scipy.sparse import coo_matrix, csc_matrix
from scipy.sparse.linalg import spsolve


def analytic_c(N, n, r):
    kappa = math.acosh(1 + r / 2)
    # log-sum-exp stable enough for the finite test grids.
    q = math.exp(-kappa)
    h = (q**n + q**(N-n)) / (1 + q**N)
    return (r * ((-1)**n) + 4 * h) / (r + 4)


def finite_state_c(N, r):
    assert N % 2 == 0
    S = 2**N
    rows, cols, data = [], [], []
    for mask in range(S):
        spins = [1 if mask >> j & 1 else -1 for j in range(N)]
        tot = 0.0
        for i in range(N):
            rate = .5 * (1 - .5 * spins[i] * (spins[(i-1)%N] + spins[(i+1)%N]))
            if rate:
                rows.append(mask ^ (1 << i)); cols.append(mask); data.append(rate)
                tot += rate
        for neel in [sum(1 << j for j in range(0,N,2)),sum(1 << j for j in range(1,N,2))]:
            if neel != mask:
                rows.append(neel); cols.append(mask); data.append(r / 2)
                tot += r / 2
        rows.append(mask); cols.append(mask); data.append(-tot)
    qtr = coo_matrix((data,(rows,cols)),shape=(S,S)).tolil()
    # Q^T here already acts on a column probability vector.
    qtr[0,:] = np.ones(S)
    rhs = np.zeros(S); rhs[0] = 1.0
    pi = spsolve(qtr.tocsc(), rhs)
    assert min(pi) > -1e-10
    assert abs(pi.sum()-1) < 1e-10
    Cs=[]
    for n in range(1,N):
        cs = 0.0
        for mask, prob in enumerate(pi):
            s0 = 1 if mask&1 else -1
            sn = 1 if mask&(1<<n) else -1
            cs += prob*s0*sn
        Cs.append(cs)
    return Cs


def root(N,n):
    a,b=1e-8,10.0
    for _ in range(100):
        m=(a+b)/2
        if analytic_c(N,n,m)>0:a=m
        else:b=m
    return (a+b)/2


def main():
    ncheck=0
    for N in [4,6,8]:
        for r in [.1,.5,1.0,1.6,4.0]:
            Cs = finite_state_c(N,r)
            for n,actual in enumerate(Cs,1):
                pred = analytic_c(N,n,r)
                assert abs(actual-pred)<2e-9, (N,n,r,actual,pred)
                ncheck+=1
            print(f'N={N}, r={r:.1f}: all {N-1} pair correlations verified')
    for N in [4,6,8,10,12,20,40,100]:
        odds = range(1,N//2+1,2)
        thresholds=[]
        for n in odds:
            z=root(N,n)
            assert abs(analytic_c(N,n,z))<1e-12
            assert analytic_c(N,n,z*.9)>0
            assert analytic_c(N,n,z*1.1)<0
            thresholds.append(z)
            ncheck+=3
        assert all(a>b for a,b in zip(thresholds,thresholds[1:])), (N,thresholds)
        print(f'N={N}: odd-distance thresholds', [(n,round(z,8)) for n,z in zip(odds,thresholds)])
    for n in [1,3,5,9,21,51,101]:
        def Cinf(r):
            q=math.exp(-math.acosh(1+r/2))
            return (4*q**n-r)/(r+4)
        a,b=1e-12,10.0
        for _ in range(100):
            m=(a+b)/2
            if Cinf(m)>0:a=m
            else:b=m
        z=(a+b)/2
        assert abs(Cinf(z))<1e-11
        if n==1: assert abs(z-4/3)<1e-12
        if n==3: assert abs(z-1/2)<1e-12
        if n>=5:
            from scipy.special import lambertw
            approx = 4*(lambertw(n).real/n)**2
            if n>=51: assert abs(z/approx-1)<.2
        ncheck+=4
        print(f'infinite n={n}: crossing r={z:.12f}')
    # Independent discrete Fourier check of the exact structure factor.
    for N in [4,6,8,10,20]:
        for r in [.1,.5,2.0]:
            q=math.exp(-math.acosh(1+r/2))
            p=r/(r+4)
            a=4/(r+4)
            cs=[analytic_c(N,n,r) for n in range(N)]
            for j in range(N):
                k=2*math.pi*j/N
                re=sum(cs[n]*math.cos(k*n) for n in range(N))
                im=-sum(cs[n]*math.sin(k*n) for n in range(N))
                predicted=(a*(1-q**N)/(1+q**N)*(1-q*q)/
                           (1-2*q*math.cos(k)+q*q)+p*N*(j==N//2))
                assert abs(re-predicted)<2e-10
                assert abs(im)<2e-10
                ncheck+=1
    print('TOTAL numeric assertions groups:', ncheck)

if __name__ == '__main__': main()
