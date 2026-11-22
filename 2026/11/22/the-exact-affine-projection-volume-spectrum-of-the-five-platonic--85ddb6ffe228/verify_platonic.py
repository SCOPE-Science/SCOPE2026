#!/usr/bin/env python3
"""Exact quadratic-field certificates for Platonic projection-body volumes.

Requires SymPy, NumPy and SciPy. The finite determinant identities also
have hand-verifiable multiplicity tables in the accompanying proof.
"""
from collections import Counter
from itertools import combinations, product
from math import sqrt, pi
import sympy as sp
import numpy as np
from scipy.spatial import ConvexHull

s5=sp.sqrt(5); phi=(1+s5)/2

def pairs(vs):
    out={}
    for v in vs:
        vv=tuple(v)
        if float(next(q for q in vv if q!=0))<0:
            vv=tuple(-q for q in vv)
        out[vv]=1
    return list(out)

def solids():
    ico=[]; dod=[]
    for a,b in product([-1,1],repeat=2):
        ico.extend([(0,a,b*phi),(a,b*phi,0),(a*phi,0,b)])
        for c in [-1,1]: dod.append((a,b,c))
        dod.extend([(0,a/phi,b*phi),(a/phi,b*phi,0),(a*phi,0,b/phi)])
    return ico,dod

def signed_det(a,b,c):
    return sp.simplify(sp.det(sp.Matrix([a,b,c])))

def exact_minor_spectrum(vs):
    out=Counter(); total=0
    for a,b,c in combinations(vs,3):
        d=signed_det(a,b,c)
        if d==0: key='0'
        else:
            d=d if d.evalf()>0 else -d
            d=sp.simplify(d)
            key=str(d)
            total+=d
        out[key]+=1
    return out,sp.simplify(total)

def main():
    ico,dod=solids()
    assert len(ico)==12 and len(dod)==20
    I=pairs(ico);D=pairs(dod)
    assert (len(I),len(D))==(6,10)
    a,ti=exact_minor_spectrum(I)
    b,td=exact_minor_spectrum(D)
    assert a==Counter({'sqrt(5) + 3':10,'1 + sqrt(5)':10}),(a,ti)
    assert b==Counter({'-1 + sqrt(5)':30,'2':30,'1 + sqrt(5)':30,'4':20,'2*sqrt(5)':10}),(b,td)
    assert sp.simplify(ti-40-20*s5)==0
    assert sp.simplify(td-140-80*s5)==0
    face_d=5*(2/phi)**2/(4*sp.tan(sp.pi/5))
    face_i=sp.sqrt(3)
    Vd=10+2*s5
    Vi=sp.Rational(10,3)*(3+s5)
    pi_d=sp.simplify(8*face_d**3*ti/(phi+2)**sp.Rational(3,2))
    pi_i=sp.simplify(8*face_i**3*td/(3*sp.sqrt(3)))
    assert sp.simplify(pi_d-800*s5)==0,sp.simplify(pi_d-800*s5)
    assert sp.simplify(pi_i-(1120+640*s5))==0
    ratio_d=sp.simplify(pi_d/Vd**2)
    ratio_i=sp.simplify(pi_i/Vi**2)
    assert sp.simplify(ratio_d-(15*s5-25))==0
    assert sp.simplify(ratio_i-(63*s5-99)/5)==0
    # Independently form the Minkowski sums as the hulls of all signed
    # generator sums. Their areas from the original solids are not supplied.
    for name,normals,face,norm_sq,target in [
        ('dodecahedron',I,face_d,phi+2,pi_d),
        ('icosahedron',D,face_i,sp.Integer(3),pi_i),
    ]:
        vectors=np.array([[float(q*face/sp.sqrt(norm_sq)) for q in v] for v in normals])
        signs=np.array(list(product([-1,1],repeat=len(vectors))))
        points=signs @ vectors
        hull=ConvexHull(points)
        assert abs(hull.volume-float(target))/float(target)<1e-11,(name,hull.volume,float(target))
    cube=sp.Integer(8);octa=sp.Integer(9);tetra=sp.Integer(18)
    assert 3*pi*pi/4<float(cube)<float(ratio_i)<float(ratio_d)<float(octa)<float(tetra)
    print('PLATONIC_PROJECTION_OK minor_spectra=20+120 hull_vertices=64+1024 ratios=5')
    print('ratios:', [(v,float(v)) for v in (cube,ratio_i,ratio_d,octa,tetra)])

if __name__=='__main__':main()
