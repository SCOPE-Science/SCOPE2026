#!/usr/bin/env python3
"""Reproducibility check for the exact FCC central-section correspondence."""
import itertools
import math
import numpy as np

v = [(2*s,0,0) for s in (-1,1)] + [(0,2*s,0) for s in (-1,1)] + [(0,0,2*s) for s in (-1,1)] + list(itertools.product((-1,1), repeat=3))
e = [(i,j) for i in range(6) for j in range(6,14) if sum(v[i][k]*v[j][k] for k in range(3))==2]
assert len(v)==14 and len(e)==24
# A section polygon vertex is an edge crossing the cutting plane.
rng=np.random.default_rng(77)
u=rng.normal(size=(150000,3))
sg=(u @ np.array(v,dtype=float).T)>0
n_r=sum((sg[:,i]!=sg[:,j]).astype(np.int16) for i,j in e)
a=np.abs(u)
tr=(2*a.max(axis=1)<a.sum(axis=1))
n_c=np.where(tr,6,4)
assert np.all(n_r+n_c==12)
assert np.all(n_r==np.where(tr,6,8))
prob=4/math.pi*math.atan(math.sqrt(2)/5)
assert abs(prob-(1-6/math.pi*math.asin(1/3)))<1e-14
assert abs(np.mean(tr)-prob)<.006
print('FCC_SECTION_CHECK_OK',len(e),'edges',len(u),'directions','p_hex=',prob)
