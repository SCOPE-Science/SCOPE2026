"""Reproduce exact block reduction and numerical singular spectra for prime fields.
Uses standard Python and NumPy; no external source files.
"""
import numpy as np
from math import pi

def blocks(p,b=1):
    vals=range(1,p)
    z=np.exp(2j*pi*b/p)
    A=np.array([[z**((a*c+pow(a*c,-1,p))%p) for c in vals] for a in vals])
    J=np.ones_like(A)
    H=np.block([[A,J],[J,A]])
    X=[]
    for a in vals:
        X.append((a,0,0,pow(a,-1,p)))
    for a in vals:
        X.append((0,a,-pow(a,-1,p)%p,0))
    D=np.array([[z**(sum((u*v)%p for u,v in zip(x,y))%p) for y in X] for x in X])
    assert np.max(np.abs(H-D))<1e-9,(p, 'block identity')
    omega=np.exp(2j*pi/(p-1)) if p>2 else 1.
    # Find generator of multiplicative group to index characters.
    def is_generator(g):
        return len({pow(g,k,p) for k in range(p-1)})==p-1
    g=next(g for g in vals if is_generator(g))
    logs={pow(g,k,p):k for k in range(p-1)}
    twisted=[sum(omega**(r*logs[t])*z**((t+pow(t,-1,p))%p) for t in vals) for r in range(p-1)]
    expected=[abs(twisted[0]+(p-1)),abs(twisted[0]-(p-1))]+sum(([abs(x)]*2 for x in twisted[1:]),[])
    sv=np.linalg.svd(H,compute_uv=False)
    assert np.max(np.abs(np.sort(sv)-np.sort(expected)))<1e-8,(p,'spectrum')
    # Compare determinant factorization on small-to-moderate matrices.
    if p in (3,5,7,11):
        predicted_det=(twisted[0]**2-(p-1)**2)*np.prod(np.asarray(twisted[1:])**2)
        actual_det=np.linalg.det(H)
        assert abs(predicted_det-actual_det)/max(1,abs(actual_det)) < 1e-10,(p,'determinant')
    rank=np.sum(sv>1e-8)
    if p>2: assert rank==2*(p-1),(p,rank)
    else: assert rank==1,(p,rank)
    print(f'p={p}; b={b}; dimension={len(X)}; rank={rank}; min_singular={min(sv):.8g}; max_diff={np.max(np.abs(np.sort(sv)-np.sort(expected))):.2e}')

if __name__=='__main__':
    for p in [2,3,5,7,11,13,17,19]:
        for b in [1] if p==2 else [1,2]: blocks(p,b)
    print('NORMALIZER_FOURIER_PASS')
