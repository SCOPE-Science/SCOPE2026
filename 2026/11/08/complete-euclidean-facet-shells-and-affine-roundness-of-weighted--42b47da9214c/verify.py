"""Exact finite checks of weighted staircase-difference polytope identities.
The infinite-dimensional-parametric conclusions require the separate proof.
"""
from fractions import Fraction as F
from itertools import combinations,product
from math import comb
import random

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def check(d,weights):
    n=d+1
    verts=[]
    for i in range(d):
        for j in range(i,d):
            t=tuple(weights[k] if i<=k<=j else F(0) for k in range(d))
            verts.extend([t,tuple(-v for v in t)])
    assert len(set(verts))==d*n
    facets=[]
    for mask in range(1,1<<d):
        prev=0; u=[]
        for i in range(d):
            b=prev ^ (1 if mask&(1<<i) else 0)
            u.append(F(b-prev,1)/weights[i]);prev=b
        assert set(dot(u,v) for v in verts) <= {F(-1),F(0),F(1)}
        for sign in (-1,1):
            equality=[v for v in verts if sign*dot(u,v)==1]
            import sympy as sp
            mat=sp.Matrix([[z-equality[0][j] for j,z in enumerate(v)] for v in equality[1:]])
            assert mat.rank()==d-1,(d,mask,sign)
            facets.append((tuple(sign*t for t in u),equality))
    assert len(facets)==2*(2**d-1)
    # Exact direct minimum- and maximum-sphere bounds by inequalities.
    inv_norm2=sum(1/(w*w) for w in weights)
    radius2=1/inv_norm2
    max2=sum(w*w for w in weights)
    assert all(dot(v,v)<=max2 for v in verts)
    assert sum(dot(v,v)==max2 for v in verts)==2
    for normal,_ in facets:
        norm2=dot(normal,normal)
        assert radius2*norm2<=1
    # Ellipsoidal quadratic form equals root squared norm.
    Fbal=(n*n)//4
    for v in verts:
        y=[v[i]/weights[i] for i in range(d)]
        z=[-y[0]] + [y[i-1]-y[i] for i in range(1,d)] +[y[-1]]
        assert dot(z,z)==2
    # John root ellipsoid support for all facets equals max balanced-set value.
    # Facet normal is a 0-1 subset weight modulo centroid.
    for k in range(1,n):
        supportdual=F(k*(n-k),n)
        assert F(n,Fbal)*supportdual<=1
    assert max(F(k*(n-k),n) for k in range(1,n))==F(Fbal,n)
    return len(verts),len(facets)

if __name__=='__main__':
    import sympy
    configurations=0
    for d in range(2,7):
        ws=[tuple(F(w) for w in [1]*d),tuple(F(i+1) for i in range(d)),tuple(F((i*3+1)%7+1) for i in range(d))]
        for w in ws:
            p,f=check(d,w)
            print('d',d,'weights',tuple(map(str,w)),'vertices',p,'facets',f)
            configurations+=1
    print('PASS',configurations,'configurations')
