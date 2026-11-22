#!/usr/bin/env python3
"""Independent floating-point diagnostics (NOT a substitute for exact certificate)."""
from itertools import combinations
import numpy as np
N=25
F=np.exp(2j*np.pi*np.outer(np.arange(N),np.arange(N))/N)
cols=list(combinations(range(N),3))
for k in (2,3,4):
    row=(0,1,k)
    eig=[]
    for c in cols:
        M=F[np.ix_(row,c)]
        eig.append((float(np.linalg.eigvalsh(M.conj().T@M)[0]),c))
    eig.sort()
    minimum=eig[0][0]
    worst=[c for v,c in eig if abs(v-minimum)<1e-9]
    expected=[tuple((j+t)%N for j in (0,1,2)) for t in range(N)]
    expected={tuple(sorted(x)) for x in expected}
    assert set(worst)==expected,(k,worst)
    other=next((v for v,c in eig if c not in expected))
    print('row',row,'min eigen',format(minimum,'.15g'),'next distinct',format(other,'.15g'),'minimizer columns',len(worst))
print('PASS independent direct complex double-precision diagnostic on 6900 restrictions')
