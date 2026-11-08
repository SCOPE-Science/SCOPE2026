"""Finite independent geometric checks for diagonal-slab Mahler profiles.
Usage: python slab_mahler_checker.py
Requires Python >=3.10, NumPy, SciPy, and SymPy.
"""
from fractions import Fraction
from math import comb, factorial
from itertools import combinations, product
import numpy as np
from scipy.spatial import ConvexHull
import sympy as sp


def exact_volumes(d, t):
    t = Fraction(t)
    pos=lambda a:max(a,Fraction(0))
    vol=sum((-1)**j*comb(d,j)*(pos(d+t-2*j)**d-pos(d-t-2*j)**d)
            for j in range(d+1))/factorial(d)
    polar=(Fraction(2**d)+2*sum(comb(d,k)*pos(Fraction(d-2*k,t)-1)
                                        for k in range(d+1)))/factorial(d)
    return vol,polar


def vertices_of_slab(d,t):
    normals=[]
    for i in range(d):
        for sg in (1,-1):
            v=np.zeros(d);v[i]=sg;normals.append((v,1.0))
    normals.extend([(np.ones(d),float(t)),(-np.ones(d),float(t))])
    points={}
    for combo in combinations(range(len(normals)),d):
        aa=np.array([normals[i][0] for i in combo]);bb=np.array([normals[i][1] for i in combo]);
        if np.linalg.matrix_rank(aa)<d:continue
        v=np.linalg.solve(aa,bb)
        if all(np.dot(a,v)<=b+1e-8 for a,b in normals):
            points[tuple(np.round(v,9))]=v
    return np.array(list(points.values()))

count=0
for d in (2,3,4,5):
    for t in (Fraction(1,3),Fraction(1,1),Fraction(7,4),Fraction(5,2)):
        if t>=d:continue
        v,w=exact_volumes(d,t)
        hull=ConvexHull(vertices_of_slab(d,t)).volume
        verts=np.vstack((np.eye(d),-np.eye(d),np.ones((1,d))/float(t),-np.ones((1,d))/float(t)))
        dualhull=ConvexHull(verts).volume
        assert abs(hull-float(v))<1e-7,(d,t,hull,v)
        assert abs(dualhull-float(w))<1e-7,(d,t,dualhull,w)
        count+=1

x=sp.symbols('x', positive=True)
Plo=12-sp.Rational(4,3)*x**2
Phi=(8-(3-x)**3/sp.Integer(3))*(1+1/x)
assert sp.factor(Phi-(x+1)*(x**3-9*x**2+27*x-3)/(3*x))==0
assert sp.simplify(x**2*sp.diff(Phi,x)-(3*x**4-16*x**3+18*x**2+3)/3)==0
assert sp.factor(Phi-sp.Rational(32,3))==(x-3)*(x-1)*(x**2-4*x-1)/(3*x)
assert sp.factor(3*x*(12-Phi))==-x**4+8*x**3-18*x**2+12*x+3
assert sp.factor(Plo.subs(x,1)-Phi.subs(x,1))==0
assert sp.factor(Phi.subs(x,3)-sp.Rational(32,3))==0
assert sp.simplify(sp.diff(3*x**2*sp.diff(Phi,x),x)-12*x*(x-1)*(x-3))==0
for d in range(2,11):
    ve,we=exact_volumes(d,Fraction(d))
    assert ve==2**d and we==Fraction(2**d,factorial(d))
    B=sum(comb(d,k)*abs(d-2*k) for k in range(d+1))
    assert B==2*d*comb(d-1,(d-1)//2)
    if d%2:
        for t in (Fraction(1,4),Fraction(1,2),Fraction(1,1)):
            v,w=exact_volumes(d,t)
            assert w==Fraction(B,factorial(d))/t
    else:
        C=comb(d,d//2)
        for t in (Fraction(1,4),Fraction(1,2),Fraction(1,1)):
            v,w=exact_volumes(d,t)
            assert w==Fraction(C,factorial(d))+Fraction(B,factorial(d))/t
print('DIAGONAL_SLAB_MAHLER_CHECKS_PASSED',count,9)
