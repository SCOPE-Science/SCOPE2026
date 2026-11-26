#!/usr/bin/env python3
"""Independent full-configuration checks of a two-hard-core-particle pairing law.

Requires Python 3, NumPy and SciPy. Run: python verify.py
The full Hamiltonian and Markov generator are built from allowed single hops.
"""
from itertools import combinations
from math import exp, pi, sqrt
import numpy as np
from scipy.linalg import expm


def full_matrices(m):
    vertices = range(2*m)
    pairs = list(combinations(vertices, 2))
    pos = {p: j for j, p in enumerate(pairs)}
    N = len(pairs)
    H = np.zeros((N, N), dtype=float)
    # Work from each configuration, with no quotient or preassigned spectrum.
    for j, (u, v) in enumerate(pairs):
        for mover, other in ((u, v), (v, u)):
            for w in vertices:
                if w != other and w//2 != mover//2:
                    i = pos[tuple(sorted((w, other)))]
                    H[i,j] += 1.0
    assert np.allclose(H, H.T)
    paired = [pos[(2*i, 2*i+1)] for i in range(m)]
    # Each permitted move has independent classical rate one.
    G = H.copy()
    np.fill_diagonal(G, -np.sum(G, axis=0))
    assert np.allclose(np.sum(G, axis=0), 0.0)
    return H, G, paired, pos[(0,1)]


def f(q, t):
    return 4*q/(q*q+4) * np.sin(t*sqrt(q*q+4))**2


def quantum_probability(m,t):
    return 1 - f(2*m-2,t)/m - (m-1)*f(m-2,t)/m


def classical_probability(m,t):
    return 1/(2*m-1) + (2*m-2)/(2*m-1)*exp(-(4*m-2)*t)


def sharp_bounds(m):
    q0=2*m-2; q1=m-2
    hi=4*q0/(m*(q0*q0+4)) + 4*(m-1)*q1/(m*(q1*q1+4))
    tm=pi/(2*sqrt(q1*q1+4))
    lo=1-quantum_probability(m,tm)
    return lo,hi,tm


def main():
    max_q=max_c=0.0
    cases=0
    for m in range(3,9):
        H,G,paired,start=full_matrices(m)
        for t in (0.0,0.017,0.079,0.23,0.51,pi/(2*sqrt((m-2)**2+4))):
            state=expm(-1j*t*H)[:,start]
            full_quantum=float(np.sum(np.abs(state[paired])**2))
            full_classical=float(np.sum(expm(t*G)[paired,start]))
            assert abs(float(np.sum(abs(state)**2))-1)<2e-12
            assert abs(float(np.sum(expm(t*G)[:,start]))-1)<2e-12
            qerr=abs(full_quantum-quantum_probability(m,t))
            cerr=abs(full_classical-classical_probability(m,t))
            max_q=max(max_q,qerr); max_c=max(max_c,cerr)
            assert qerr<2e-11,(m,t,qerr)
            assert cerr<2e-11,(m,t,cerr)
            cases+=1
        lo,hi,_=sharp_bounds(m)
        assert lo>=-1e-12 and lo<=hi+1e-12
    print('Full matrix comparisons:',cases)
    print('Max quantum deviation:',format(max_q,'.4g'))
    print('Max classical deviation:',format(max_c,'.4g'))
    print('m   m * lower leakage   m * upper leakage   classical at tau')
    for m in (16,32,64,128,256,512,1024,4096,16384):
        lo,hi,tm=sharp_bounds(m)
        print(m,format(m*lo,'.11g'),format(m*hi,'.11g'),format(classical_probability(m,tm),'.11g'))
    assert abs(4096*sharp_bounds(4096)[0]-4)<0.01
    assert abs(4096*sharp_bounds(4096)[1]-4)<0.01
    assert abs(classical_probability(4096,sharp_bounds(4096)[2])-exp(-2*pi))<0.001
    print('PASS: full-configuration and asymptotic corroboration')

if __name__=='__main__':
    main()
