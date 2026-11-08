#!/usr/bin/env python3
"""Optional independent implementation cross-check (requires NumPy)."""
import numpy as np
from CHECK import GRID, Q, maps, N
staged,one=maps()
bits=np.arange(N,dtype=np.uint16)
x=bits.view(np.float16)
with np.errstate(all='ignore'):
    y=np.float16(np.float16(np.float16(4.0)*x)*np.float16(np.float16(1.0)-x))
    z=np.float16((4.0*x.astype(np.float64))*(1.0-x.astype(np.float64)))
ys=y.view(np.uint16).astype(int).tolist()
zs=z.view(np.uint16).astype(int).tolist()
assert ys==staged, [(i,a,b) for i,(a,b) in enumerate(zip(ys,staged)) if a!=b][:8]
assert zs==one, [(i,a,b) for i,(a,b) in enumerate(zip(zs,one)) if a!=b][:8]
print('NUMPY_OK bitwise_transition_match=30722 binary16_double_independent=1')
