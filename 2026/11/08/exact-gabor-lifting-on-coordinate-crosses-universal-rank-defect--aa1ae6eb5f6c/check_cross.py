"""Reproducibility checks for the coordinate-cross Gabor lifting spectrum."""
import cmath
import math
from collections import Counter
import numpy as np

def exercise(p, include_dense=False):
    assert p >= 3 and p % 2 == 1
    N = p * p
    S = {(i, 0) for i in range(p)} | {(0, j) for j in range(p)}
    roots = [cmath.exp(2j * math.pi * k / p) for k in range(p)]
    obs = Counter()
    for u in range(p):
        for v in range(p):
            for r in range(p):
                for s in range(p):
                    z = sum(roots[(r * x + s * y) % p]
                            for x,y in S
                            if ((x - u) % p, (y - v) % p) in S)
                    if abs(z) < 1e-8:
                        obs['zero'] += 1
                    elif u == v == 0:
                        obs['origin_' + ('0' if (r,s)==(0,0) else 'axis' if (r==0 or s==0) else 'off')] += 1
                        expected = 2*p-1 if (r,s)==(0,0) else p-1 if (r==0 or s==0) else 1
                        assert abs(abs(z) - expected) < 1e-8
                    elif u == 0 or v == 0:
                        obs['axial'] += 1
                        assert abs(abs(z)-p)<1e-8
                    else:
                        t = (r*u-s*v)%p
                        j = min(t,p-t)
                        obs['mixed_'+str(j)] += 1
                        assert abs(abs(z)-2*math.cos(math.pi*j/p))<1e-8
    assert obs['zero'] == 2*p*(p-1)**2,(p,obs)
    assert obs['origin_0']==1
    assert obs['origin_axis']==2*(p-1)
    assert obs['origin_off']==(p-1)**2
    assert obs['axial']==2*p*(p-1)
    assert obs['mixed_0']==p*(p-1)**2
    for j in range(1,(p-1)//2+1):assert obs['mixed_'+str(j)]==2*p*(p-1)**2
    assert sum(obs.values())==N*N
    if include_dense:
        # Independent assembly of the full lifting matrix from the Gabor vectors.
        pts = [(i,j) for i in range(p) for j in range(p)]
        mat = np.zeros((N*N,N*N),complex)
        for ai,(u,v) in enumerate(pts):
            for bi,(r,s) in enumerate(pts):
                w=np.array([roots[(r*x+s*y)%p] if (((x-u)%p,(y-v)%p) in S) else 0j for x,y in pts])
                mat[ai*N+bi,:]=np.outer(np.conj(w),w).reshape(N*N) # conjugation orientation immaterial for SV
        singular=np.linalg.svd(mat,compute_uv=False)
        theoretical=[0.]*obs['zero']
        for key,cnt in obs.items():
            if key=='zero':continue
            if key=='origin_0':ampl=2*p-1
            elif key=='origin_axis':ampl=p-1
            elif key=='origin_off':ampl=1
            elif key=='axial':ampl=p
            else:ampl=2*math.cos(math.pi*int(key.split('_')[1])/p)
            theoretical += [p*ampl]*cnt
        assert np.allclose(sorted(singular), sorted(theoretical), atol=1e-7,rtol=1e-9)
    print('p',p,'N',N,'rank',N*N-obs['zero'],'nullity',obs['zero'],'verified coefficients',N*N,'dense',include_dense)

for p in [3,5,7]:exercise(p,include_dense=p==3)
print('ALL_CROSS_GABOR_SPECTRAL_CHECKS_OK')
