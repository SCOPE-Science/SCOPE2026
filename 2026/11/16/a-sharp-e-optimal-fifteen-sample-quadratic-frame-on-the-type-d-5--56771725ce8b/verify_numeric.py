"""Independent floating-point exhaustive cross-check of the D5 15-sample theorem.
Needs NumPy; exact proof is in RESULT.md and verify_exact.py.
"""
import itertools
from collections import Counter
import numpy as np
n=5
edges=list(itertools.combinations(range(n),2))
rows=[]
for e,(i,j) in enumerate(edges):
    pair=[]
    for sign in (1,-1):
        a=np.zeros(15)
        a[i]=a[j]=0.5
        a[5+e]=sign/(2**0.5)
        pair.append(a)
    rows.append(pair)
counts=Counter()
for double in itertools.combinations(range(10),5):
    doubled=set(double)
    incidence=np.zeros((5,5))
    for j,e in enumerate(double):
        i,k=edges[e]; incidence[i,j]=incidence[k,j]=1
    if abs(np.linalg.det(incidence)) < 0.5:
        continue
    for signs in itertools.product((0,1),repeat=5):
        selected=[];sk=0
        for e in range(10):
            if e in doubled: selected.extend(rows[e])
            else:
                selected.append(rows[e][signs[sk]]);sk+=1
        mat=np.asarray(selected)
        eig=np.linalg.eigvalsh(mat@mat.T)
        assert eig[0]>0
        assert abs(np.linalg.det(mat@mat.T)-1/256)<1e-9
        counts[round(float(eig[0]),10)]+=1
assert counts=={
    round(0.07517120105906895,10):2304,
    round(0.049327534803371605,10):960,
    round(0.0438500230162984,10):1920
}, counts
print('PASS: all 5184 nonsingular selections cross-checked by direct eigensolvers and Gram determinants')
