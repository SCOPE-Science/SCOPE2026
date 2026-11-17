"""Reproducibility checks for invariant affine regular-simplex section face-vector laws.
Requires NumPy and SciPy. Execute: python check_affine_simplex_section.py
"""
from math import comb, log, pi, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr

rng = np.random.default_rng(20261102)

def face_count(k, n, j):
    l = n-k
    return sum(comb(k,a)*comb(l,j+2-a)
               for a in range(1,j+2) if a<=k and 1<=j+2-a<=l)

def exact_probabilities(n):
    gaps=np.array([comb(n,k)*quad(lambda x: ndtr(x)**k*ndtr(-x)**(n-k),
                                   -12,12,epsabs=2.e-11)[0]
                   for k in range(1,n)])
    return gaps/gaps.sum(),gaps.sum()

for n in [3,4,6,8]:
    pmf,mean_range=exact_probabilities(n)
    assert abs(pmf.sum()-1)<1.e-10
    assert np.max(np.abs(pmf-pmf[::-1]))<1.e-10
    exact_mean=sum(face_count(k,n,0)*pmf[k-1] for k in range(1,n))
    crofton_mean=n*(n-1)/(sqrt(pi)*mean_range)
    assert abs(exact_mean-crofton_mean)<1.e-8
    for k in range(1,n):
        # Independent face counts: choose any source-simplex face with
        # at least one vertex on each side; its section dimension is size-2.
        labels=np.arange(n)
        for j in range(n-1):
            brute=sum(0<sum(x<k for x in subset)<len(subset)
                      for size in [j+2]
                      for subset in __import__('itertools').combinations(labels,size))
            assert face_count(k,n,j)==brute,(n,k,j)
    z=rng.standard_normal((140000,n))
    rad=np.linalg.norm(z-z.mean(axis=1,keepdims=True),axis=1)
    weights=np.ptp(z,axis=1)/rad  # Correct Crofton normal-direction bias.
    u=rng.random(len(z))
    offsets=z.min(axis=1)+u*np.ptp(z,axis=1)
    ranks=(z<offsets[:,None]).sum(axis=1)
    pmf_mc=np.bincount(ranks,weights=weights,minlength=n+1)[1:n]/weights.sum()
    assert max(abs(pmf-pmf_mc))<.009
    print(f'n={n}; exact E vertices={exact_mean:.9f}; maximal PMF MC error={max(abs(pmf-pmf_mc)):.5f}')

for n in [300,1200,4800]:
    reps=6500 if n<4800 else 2600
    g=rng.standard_normal((reps,n))
    u=rng.uniform(-1,1,reps)
    t=(1-u)*g.min(axis=1)/2+(1+u)*g.max(axis=1)/2
    k=(g<t[:,None]).sum(axis=1)
    for j in range(3):
        powers=np.array([log(face_count(int(ki),n,j))/log(n) for ki in k])
        residual=np.abs(powers-(j+2-u*u))
        print(f'n={n}, face_dim={j}, mean log-exponent error={residual.mean():.5f}')
        assert residual.mean()<.55
print('AFFINE_SIMPLEX_SECTION_FACE_VECTOR_CHECKS_PASSED')
