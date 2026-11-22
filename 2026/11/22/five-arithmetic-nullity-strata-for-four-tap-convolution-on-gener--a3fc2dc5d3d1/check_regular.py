"""Independent finite matrix consistency test for the stated dihedral-convolution theorem.
Requires Python 3 and NumPy; finite tests do not prove universal quantifiers.
"""
import itertools
import math
import numpy as np


def witness(m, defect):
    inner = [2 * math.cos(2 * math.pi * k / m) for k in range(1, (m - 1) // 2 + 1)] if m % 2 else [2 * math.cos(2 * math.pi * k / m) for k in range(1, m // 2)]
    if defect == 0:
        roots = (3., 4.)
    elif defect == 1:
        roots = (2., 3.)
    elif defect == 2:
        roots = (inner[0], 3.)
    elif defect == 3:
        roots = (2., inner[0])
    elif defect == 4 and len(inner) >= 2:
        roots = (inner[0], inner[1])
    else:
        raise ValueError((m, defect))
    u, v = roots
    if abs(u + v) > 1.e-10:
        a, b, c, d = 1., -(u + v) / 2, 1., (u - v) / 2
    else:
        a, b, c, d = 1., 2., -1., math.sqrt(8-u*u)
    assert min(abs(z) for z in (a, b, c, d)) > 1e-8
    return a, b, c, d


def regular_matrix(moduli, h, coeffs):
    H = list(itertools.product(*(range(n) for n in moduli)))
    group = [(x, e) for e in range(2) for x in H]
    id_of = {g:i for i,g in enumerate(group)}
    zero = tuple(0 for n in moduli)
    twoh = tuple((2*x) % n for x,n in zip(h,moduli))
    taps = [((zero,0),coeffs[0]),((h,0),coeffs[1]),((twoh,0),coeffs[2]),((zero,1),coeffs[3])]
    assert len({z for z,c in taps})==4
    M = np.zeros((len(group),len(group)),dtype=float)
    for j,(v,f) in enumerate(group):
        for (u,e),c in taps:
            target = (tuple((u[k]+(-1)**e*v[k])%moduli[k] for k in range(len(moduli))), (e+f)%2)
            M[id_of[target],j] += c
    return M


cases = [((3,),(1,)),((4,),(1,)),((5,),(1,)),((6,),(1,)),
         ((9,),(3,)),((12,),(3,)),((3,3),(1,0)),((4,2),(1,0)),((5,3),(1,0)),((6,2),(1,0))]
count=0
for moduli,h in cases:
    N=math.prod(moduli)
    m=next(k for k in range(1,N+1) if all((k*x)%n==0 for x,n in zip(h,moduli)))
    q=N//m
    for j in range(4 if m in (3,4) else 5):
        M=regular_matrix(moduli,h,witness(m,j))
        s=np.linalg.svd(M,compute_uv=False)
        err=sum(z<1.e-7 for z in s)
        assert err==q*j, (moduli,h,m,j,q,err,s)
        nonzero=s[s>=1.e-7]
        assert len(nonzero)>0 and nonzero.min()>1.e-4
        count+=1
        print('PASS',moduli,h,'order',m,'index',q,'defect-index',j,'nullity',err,'minpositive',round(float(nonzero.min()),6))
print('PASS direct matrices:',count)
