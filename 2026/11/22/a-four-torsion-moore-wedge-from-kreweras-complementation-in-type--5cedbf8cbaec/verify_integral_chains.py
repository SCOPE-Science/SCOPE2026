"""Independent integral cellular-boundary check of the Kreweras orbit complex.

Requires Python 3 and SymPy (for exact integer Smith form).
Run alongside verify.py: python3 verify_integral_chains.py
"""
from collections import Counter
from sympy import ZZ, Matrix
from sympy.matrices.normalforms import smith_normal_form
import verify

group=verify.check_group()
faces, action=verify.build_original_complex(group)
orbit,reps,groups=verify.quotient_simplices(faces,action)
vertices=groups[1]; edges=groups[2]; triangles=groups[3]
vid={o:i for i,o in enumerate(vertices)}
eid={o:i for i,o in enumerate(edges)}
d1=Matrix.zeros(len(vertices),len(edges))
d2=Matrix.zeros(len(edges),len(triangles))
for j,o in enumerate(edges):
    a,b=reps[o]
    d1[vid[orbit[(a,)]],j]-=1
    d1[vid[orbit[(b,)]],j]+=1
for j,o in enumerate(triangles):
    a,b,c=reps[o]
    d2[eid[orbit[(b,c)]],j]+=1
    d2[eid[orbit[(a,c)]],j]-=1
    d2[eid[orbit[(a,b)]],j]+=1
assert d1*d2==Matrix.zeros(len(vertices),len(triangles))
D1=smith_normal_form(d1,domain=ZZ)
D2=smith_normal_form(d2,domain=ZZ)
s1=Counter(abs(D1[i,i]) for i in range(min(d1.shape)))
s2=Counter(abs(D2[i,i]) for i in range(min(d2.shape)))
assert s1=={1:76,0:1},s1
assert s2=={1:187,4:1,0:4},s2
assert d1.rank()==76 and d2.rank()==188
assert len(triangles)-d2.rank()==4
assert len(edges)-d1.rank()-d2.rank()==0
print('B4_KREWERAS_INTEGRAL_SMITH_OK')
print('cells=77,264,192 chain_composition_zero=true')
print('nonzero_smith_d1='+str(sorted((k,v) for k,v in s1.items() if k)))
print('nonzero_smith_d2='+str(sorted((k,v) for k,v in s2.items() if k)))
print('integral_homology=Z, Z/4, Z^4')
