#!/usr/bin/env python3
"""Finite exact tests of a nine-cycle coordinate-product obstruction."""
from itertools import product

def add(*vecs):
    return (sum(v[0] for v in vecs),sum(v[1] for v in vecs))

def scale(a,v):
    return (a*v[0],a*v[1])

for m in (-13,-3,-1,1,2,7,19):
    u,v,w=(1,4*m),(2,2*m),(4,m)
    assert u[0]*u[1]==v[0]*v[1]==w[0]*w[1]==4*m
    assert add(scale(2,u),scale(-5,v),scale(2,w))==(0,0)
    steps=[u,u]+[scale(-1,v)]*5+[w,w]
    pos=(0,0); vertices=[]
    for step in steps:
        vertices.append(pos)
        pos=add(pos,step)
    assert pos==(0,0) and len(set(vertices))==9
print('NINE_CYCLE_VECTOR_IDENTITY_OK multipliers=7 all_vertices_distinct')

cap=0; optimal=0
for z in product((0,1),repeat=9):
    if all(not (z[i] and z[(i+1)%9]) for i in range(9)):
        cap=max(cap,sum(z))
        if sum(z)==4:optimal+=1
assert cap==4 and optimal>0
print('CYCLIC_INDEPENDENCE_OK binary_words=512 independence_number=4')

allowed={0,1,2,3}
valid_delta={(a-b)%9 for a in allowed for b in allowed}
assert valid_delta=={0,1,2,3,6,7,8}
pairs=[(a,4//a) for a in (-4,-2,-1,1,2,4) if 4%a==0]
assert len(pairs)==6
assert all(((a+b)%9) not in valid_delta for a,b in pairs)
print('SHARP_PERIOD_NINE_EXAMPLE_OK density=4/9 forbidden_factor_pairs=6')

for x in range(-12,13):
    for y in range(-12,13):
        if (x+y)%2==0:
            assert (x*y)%4 != 2
for k,j in ((1,2),(2,1),(3,2)):
    assert k*j%4==2
print('CHECKERBOARD_OPTIMAL_MODULUS_TEST_OK range=-12..12')
print('FINITE_TESTS_ONLY_TRUE INFINITE_PROOF_SEPARATE_TRUE INDEPENDENT_AUDIT_NOT_PERFORMED')
