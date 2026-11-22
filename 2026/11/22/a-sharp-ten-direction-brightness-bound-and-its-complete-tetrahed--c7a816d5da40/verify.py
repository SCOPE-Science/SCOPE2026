#!/usr/bin/env python3
"""Exact algebra and independent geometric checks for tetrahedral brightness extrema.
Requires Python 3, SymPy, and NumPy. Run: python verify.py
"""
import itertools
import math
import numpy as np
import sympy as S

rt3 = S.sqrt(3)
e = S.Matrix([1, 0, 0]); f = S.Matrix([-S.Rational(1, 2), rt3/2, 0]); g = S.Matrix([0, 0, 1]); w = e + f

def square(v):
    return S.simplify(v.dot(v))

for t in [S.Rational(1, 10), S.Rational(1, 3), S.Rational(1, 2), S.Rational(2, 3), S.Rational(9, 10)]:
    faces = [e, f, -t*w + S.sqrt(t*(1-t))*g, -(1-t)*w - S.sqrt(t*(1-t))*g]
    assert sum(faces, S.zeros(3,1)) == S.zeros(3,1)
    assert S.simplify(S.Matrix.hstack(*faces[:3]).det()) != 0
    vectors = [faces[0], faces[1], faces[2], faces[3], faces[0]+faces[1], faces[0]+faces[2], faces[0]+faces[3]]
    norms = [square(v) for v in vectors]
    assert norms == [1, 1, t, 1-t, 1, 1, 1], norms
    assert sum([square(faces[0]+faces[j]) for j in (1,2,3)]) == sum(square(v) for v in faces)

faces = [e,f,-w/2+g/2,-w/2-g/2]
maxaxes = [faces[0], faces[1], faces[0]+faces[1], faces[0]+faces[2], faces[0]+faces[3]]
assert all(square(v)==1 for v in maxaxes)
centers=maxaxes+[-v for v in maxaxes]
assert max(S.simplify(a.dot(b)) for a,b in itertools.combinations(centers,2))==S.Rational(3,4)
critical=S.sqrt(S.Rational(7,8))
assert critical>1/S.sqrt(2)

# Construct an actual tetrahedron with exactly the prescribed outward face-area vectors.
# The face containing the origin and two edge vectors has outward normal -cross/2.
G=S.Matrix.hstack(faces[0],faces[1],faces[3])
cofactor=-2*G
assert cofactor.det()>0
E=S.sqrt(cofactor.det())*cofactor.T.inv()
a,b,c=[E[:,j] for j in range(3)]
assert all(S.simplify((u-v).dot(u-v))==0 for u,v in [
    (-b.cross(c)/2,faces[0]),
    (-c.cross(a)/2,faces[1]),
    (-a.cross(b)/2,faces[3])
])
assert S.simplify(E.det())>0

# Independent numerical verification: Cauchy facet expression equals all-subset support.
rng=np.random.default_rng(20261115)
for _ in range(100):
    first=rng.normal(size=(3,3)); fourth=-first.sum(axis=0)
    F=np.vstack((first,fourth))
    u=rng.normal(size=3);u=u/np.linalg.norm(u)
    brightness=np.sum(np.abs(F@u))/2
    subset=max(sum(F[list(ids)],np.zeros(3)).dot(u) for count in range(5) for ids in itertools.combinations(range(4),count))
    assert abs(brightness-subset)<1e-11

F=np.array([[float(x) for x in v] for v in faces]);U=rng.normal(size=(250000,3));U/=np.linalg.norm(U,axis=1)[:,None]
B=np.sum(np.abs(U@F.T),axis=1)/2
for z in (.96,.98):
    predicted=5*(1-z)
    observed=np.mean(B>z)
    standard=math.sqrt(predicted*(1-predicted)/len(U))
    assert abs(predicted-observed)<5*standard,(z, observed, predicted)
print('PASS: exact five-parameter instances, sharp contact Gram matrix, random direction support and two upper-tail checks')
print('sharp first-cap overlap height:',S.simplify(critical))
