"""Independent finite-matrix checks of Fourier exceptional-point identities.

Requires Python 3 and NumPy/SciPy.  This checker is illustrative:
finite numerical comparisons do not substitute for the all-size proof.
"""
import cmath
import math
import numpy as np
from scipy.linalg import expm


def block(k, n, p, r, s):
    z = cmath.exp(2j * math.pi * k / n)
    return np.array([[p * z-p-r, s], [r, -s]], dtype=complex)


def generator(n, p, r, s):
    G = np.zeros((2*n, 2*n), dtype=float)
    for j in range(n):
        G[(j+1) % n, j] += p
        G[n+j, j] += r
        G[j, j] -= p+r
        G[j, n+j] += s
        G[n+j, n+j] -= s
    return G


n_block = n_propagation = n_off = 0
for n in range(3, 43):
    for k in range(1, (n-1)//2+1):
        p = 1.37
        theta = 2*math.pi*k/n
        t = math.sin(math.pi*k/n)
        r, s = p*t*(1-t), p*t*(1+t)
        B = block(k, n, p, r, s)
        lam = complex(-s, p*math.sin(theta)/2)
        N = B - lam*np.eye(2)
        assert 0 < r < p/4+1e-12 and 0 < s < 2*p
        assert abs((np.trace(B)/2) - lam) < 2e-14
        assert np.linalg.norm(N@N, ord=np.inf) < 3e-13
        assert abs(N[1,0]-r) < 1e-14
        assert np.linalg.norm(N,ord=np.inf) > r
        # No other Fourier sector has this eigenvalue:
        z = cmath.exp(1j*theta)
        z_back = (lam + p + r - r*s/(lam+s))/p
        assert abs(z-z_back) < 2e-13
        n_block += 1
    # All Fourier discriminants nonzero at a nonresonant pair.
    r,s=.423,.817
    for k in range(n):
        B=block(k,n,1.,r,s)
        disc=(B[0,0]-B[1,1])**2+4*r*s
        assert abs(disc)>1e-4
        n_off+=1

# Compare full generator exponential against Fourier Jordan formula.
for n in range(3, 12):
    p=1.3
    for k in range(1, (n-1)//2+1):
        theta=2*math.pi*k/n
        t=math.sin(math.pi*k/n)
        r,s=p*t*(1-t),p*t*(1+t)
        lam=-s+1j*p*math.sin(theta)/2
        G=generator(n,p,r,s)
        assert np.linalg.norm(G.sum(axis=0),ord=np.inf) < 2e-15
        initial=np.zeros(2*n); initial[0]=1
        for time in [.11,.47,1.2,3.0]:
            probs=expm(time*G)@initial
            assert min(probs)>-2e-14
            fsum=sum(cmath.exp(1j*theta*j)*probs[n+j] for j in range(n))
            exact=r*time*cmath.exp(lam*time)
            assert abs(fsum-exact)<3e-13,(n,k,time,fsum,exact)
            n_propagation+=1

print(f'PASS: {n_block} defective Fourier-mode identities; {n_off} off-locus discriminants; {n_propagation} independent full-generator propagations.')
