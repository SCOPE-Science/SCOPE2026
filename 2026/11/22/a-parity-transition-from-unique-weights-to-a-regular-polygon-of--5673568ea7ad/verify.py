#!/usr/bin/env python3
"""Finite numerical diagnostics for cycle-mask trace-norm weight classification."""
import numpy as np

def nuclear(a):
    return float(np.linalg.svd(a,compute_uv=False).sum())

count=0
for n in range(3,41):
    p=np.roll(np.eye(n),1,axis=1)
    B=np.eye(n)+p
    target=2/(n*np.sin(np.pi/(2*n))) if n%2 else 2/(n*np.tan(np.pi/(2*n)))
    assert abs(nuclear(B)/n-target)<1e-10
    count+=1
    idx=np.arange(n)
    for a,b in [(0,0),(.15,-.2),(.4,0),(-.12,.23)]:
        u=(1+a*np.cos(2*np.pi*idx/n)+b*np.sin(2*np.pi*idx/n))/n
        if n%2==0:
            v=(1+a*np.cos(2*np.pi*(idx-.5)/n)+b*np.sin(2*np.pi*(idx-.5)/n))/n
        else:
            v=u.copy()
        if n%2==1 and (a!=0 or b!=0):
            assert nuclear(np.sqrt(u)[:,None]*B*np.sqrt(v)[None,:])<target-1e-8
        else:
            assert abs(nuclear(np.sqrt(u)[:,None]*B*np.sqrt(v)[None,:])-target)<1e-10
        count+=1
print('CYCLE_SCHUR_NORMERS_DIAGNOSTIC_OK',count)
