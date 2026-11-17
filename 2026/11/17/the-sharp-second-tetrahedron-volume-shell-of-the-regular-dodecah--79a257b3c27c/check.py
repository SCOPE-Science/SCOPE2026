#!/usr/bin/env python3
"""Exact certificate for tetrahedron volume shells in a regular dodecahedron.
Python 3 standard library only; exact arithmetic in Z[phi], phi^2=phi+1.
"""
from collections import Counter
from itertools import combinations, product
from functools import cmp_to_key

zero=(0,0)
one=(1,0)
phi=(0,1)
inv=(-1,1)

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def sign(x):
    a,b=x
    A=2*a+b
    if b==0: return (A>0)-(A<0)
    if A==0: return (b>0)-(b<0)
    if A*b>0: return (b>0)-(b<0)
    comparison=A*A-5*b*b
    assert comparison!=0  # sqrt(5) irrational and A,b nonzero integers
    return ((A>0)-(A<0)) if comparison>0 else ((b>0)-(b<0))
def absolute(x): return x if sign(x)>=0 else neg(x)
def sqdist(u,v):
    w=[sub(u[j],v[j]) for j in range(3)]
    return add(add(mul(w[0],w[0]),mul(w[1],w[1])),mul(w[2],w[2]))
def det3(m):
    a,b,c=m
    return add(sub(mul(a[0],sub(mul(b[1],c[2]),mul(b[2],c[1]))),
                   mul(a[1],sub(mul(b[0],c[2]),mul(b[2],c[0])))),
               mul(a[2],sub(mul(b[0],c[1]),mul(b[1],c[0]))))
def sq(x):return mul(x,x)

vertices=[]
for x,y,z in product((-1,1),repeat=3): vertices.append(((x,0),(y,0),(z,0)))
for a,b in product((-1,1),repeat=2):
    A=(a,0);B=(b,0)
    vertices.extend(((zero,mul(A,phi),mul(B,inv)),
                     (mul(B,inv),zero,mul(A,phi)),
                     (mul(A,phi),mul(B,inv),zero)))
assert len(vertices)==len(set(vertices))==20

shells=Counter()
models={}
second_signature_count=0
max_signature_count=0
for indices in combinations(range(20),4):
    p=vertices[indices[0]]
    vec=[tuple(sub(vertices[i][j],p[j]) for j in range(3)) for i in indices[1:]]
    d=absolute(det3(vec))
    shells[d]+=1
    models.setdefault(d,indices)
    sides=Counter(sqdist(vertices[i],vertices[j]) for i,j in combinations(indices,2))
    second_sides = (sides == {(8,0):4,(4,0):1,(4,4):1})
    max_sides = (sides == {(8,0):6})
    assert (d==(0,8)) == second_sides, (indices,d,sides)
    assert (d==(16,0)) == max_sides, (indices,d,sides)
    second_signature_count += int(second_sides)
    max_signature_count += int(max_sides)
    # Independent Cayley-Menger/Gram check: det(Gram)=(det V)^2.
    g=[]
    for u in vec:
        g.append([add(add(mul(u[0],v[0]),mul(u[1],v[1])),mul(u[2],v[2])) for v in vec])
    assert sq(d)==det3(g), (indices,d)

expected={
    (0,0):495, (8,-4):320, (-4,4):900, (4,0):1110,
    (-8,8):120,(0,4):900,(8,0):400,(-4,8):150,
    (4,4):320,(0,8):120,(16,0):10
}
assert shells==expected,(shells-expected, expected-shells)
assert sum(shells.values())==4845
levels=sorted(shells,key=cmp_to_key(lambda a,b: sign(sub(a,b))))
# Exhaustive exact pairwise order verification, not reliance on float sort:
for i in range(len(levels)-1): assert sign(sub(levels[i+1],levels[i]))>0
assert levels[-2:]==[(0,8),(16,0)]
assert shells[(16,0)]==10 and shells[(0,8)]==120
assert max_signature_count==10 and second_signature_count==120
print('DODECAHEDRON_TETRAHEDRON_SPECTRUM_PASSED vertices=20 configurations=4845 levels=11 runners_up=120 maxima=10 gram_checks=4845')
for d in levels:
    print(f'{d[0]:+d}{d[1]:+d}phi : {shells[d]:4d}; example {models[d]}')
