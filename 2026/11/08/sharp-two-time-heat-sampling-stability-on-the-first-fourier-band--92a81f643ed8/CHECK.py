#!/usr/bin/env python3
"""Independent numerical checks of two-sensor cycle-heat frame bounds.

Run: python CHECK.py. Dependency: numpy>=1.24.
Finite checks corroborate but do not prove the all-order theorem.
"""
import math
import numpy as np


def formula(q, c):
    h = 1.0 + q*q
    k = (1.0 - q)**2
    t = 4.0 + 2.0*h*(1.0+c)
    disc = t*t - 16.0*k*(1.0+c)
    lower = 8.0*k*(1.0+c)/(t+math.sqrt(max(0.0, disc)))
    anti = 2.0*h*(1.0-c)
    upper = (t+math.sqrt(max(0.0, disc)))/2.0
    return min(anti, lower), tuple(sorted((anti, lower, upper)))


def optimum(q):
    h = 1.0+q*q
    beta = 1.0-q*q-2.0*q-2.0*q**4
    return (-beta+math.sqrt(beta*beta+8*h*h*(1.0+q)**2))/(4*h*h)


def directly(N, d, q):
    lam = 1.0-math.cos(2.0*math.pi/N)
    t = -math.log(q)/lam
    # Three orthonormal graph Fourier eigenvectors, i.e. the exact low-pass space.
    grid = np.arange(N)
    columns = np.column_stack((np.ones(N)/math.sqrt(N),
            np.sqrt(2.0/N)*np.cos(2.0*math.pi*grid/N),
            np.sqrt(2.0/N)*np.sin(2.0*math.pi*grid/N)))
    # The two nonconstant eigenmodes have the same heat damping q.
    rows = np.vstack((columns[[0,d],:],
            columns[[0,d],:]*np.array([1.0, math.exp(-t*lam), math.exp(-t*lam)])))
    return np.linalg.eigvalsh(rows.T@rows)


def run():
    count = 0
    for N in range(5,91):
        for q in (0.05,0.2,0.5,0.8,0.95):
            cstar=optimum(q)
            assert 0.5 < cstar < 1
            h=1+q*q
            beta=1-q*q-2*q-2*q**4
            assert abs(2*h*h*cstar*cstar + beta*cstar-(1+q)**2)<2e-12
            vals=[]
            for d in range(1,N//2+1):
                c=math.cos(2.0*math.pi*d/N)
                af,spec=formula(q,c)
                measured=directly(N,d,q)*N
                assert np.allclose(measured,spec,rtol=1e-9,atol=1e-10),(N,d,q,measured,spec)
                vals.append((d,c,af))
                count+=1
            optimum_discrete=max(v[2] for v in vals)
            left=[v for v in vals if v[1]<=cstar]
            right=[v for v in vals if v[1]>=cstar]
            bracket = ((max(left,key=lambda v:v[1]) if left else None),
                    (min(right,key=lambda v:v[1]) if right else None))
            candidates=[v for v in bracket if v is not None]
            assert abs(optimum_discrete-max(v[2] for v in candidates))<1e-10
            count+=2
    # Exact spectral identity at challenging offsets, including antipodal pairs.
    assert abs(optimum(0)-0.5)<1e-15
    for q in (0.99,0.999,0.9999):
        scale=(1-optimum(q))/(1-q)**2
        assert abs(scale-1/6)<0.005,(q,scale)
        count+=1
    print('CYCLE_TWO_TIME_FRAME_CHECKS_PASSED',count)

if __name__=='__main__':
    run()
