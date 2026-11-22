#!/usr/bin/env python3
"""Exact verification of the finite tour-witness and nonnegative-cone certificate.
Run: python3 verify_cube_prism.py
Requires only the standard library; certificate.json in the same directory.
"""
from pathlib import Path
from fractions import Fraction
import json

records=json.loads((Path(__file__).parent/'certificate.json').read_text())
def vec(**kw):return tuple(kw.get(c,0) for c in 'ABCDE')
zeros=[tuple(int(j==i) for j in range(5)) for i in range(5)]
common=[vec(A=-1,B=-1,D=1),vec(B=-1,C=-1,E=1),vec(A=-1,D=-1,E=1),vec(A=-2,C=1),*zeros]
phases={'lo':(common+[vec(A=1,B=-1),vec(C=1,D=-1),vec(C=-1,D=-2,E=2)],[vec(D=4),vec(E=2)]),
        'hi':(common+[vec(A=-1,B=1),vec(C=-1,D=1),vec(A=-1,B=-1,C=-1,E=1)],[vec(C=2,D=2),vec(E=2)])}
def isom(mask,translation,swap):
    out=0
    for x in range(8):
        if mask>>x&1:
            y=x^translation
            if swap:y=(y&4)|((y&1)<<1)|((y&2)>>1)
            out|=1<<y
    return out

def typ(x,y):
    z=x^y; n=(z&3).bit_count()
    return (0 if n==1 else 2) if not(z&4) else (1,3,4)[n]
covered=set()
for rec in records:
    mask=rec['mask']; vertices={i for i in range(8) if mask>>i&1}
    orbit={isom(mask,t,swap) for t in range(8) for swap in (0,1)}
    assert len(orbit)==rec['orbit_size']
    assert not covered.intersection(orbit)
    covered.update(orbit)
    assert len(vertices)==rec['size']
    for phase,(generators,targets) in phases.items():
        c=rec[phase];tour=c['tour']
        assert len(tour)==len(vertices) and set(tour)==vertices
        counts=[0]*5
        for x,y in zip(tour,tour[1:]+tour[:1]):
            assert x!=y
            counts[typ(x,y)]+=1
        target=targets[c['target']]
        weights=[Fraction(x) for x in c['weights']]
        assert len(weights)==len(generators) and all(v>=0 for v in weights)
        for i in range(5):
            assert sum(weights[j]*generators[j][i] for j in range(len(weights)))==target[i]-counts[i]
assert covered==set(range(1,256))-set(1<<i for i in range(8))
print('PASS: 32 two-through-eight-vertex symmetry orbits cover 247 subsets; 64 exact tour/cone certificates')
