"""Numerical and symbolic corroboration of a triaugmented-prism inball theorem.

Requires Python 3, NumPy, SciPy, SymPy. The proof for all parameters is
algebraic and is supplied separately; finite tests do not replace it.
"""
from math import cos, sin, pi, sqrt
import numpy as np
from scipy.optimize import linprog, brentq
from scipy.spatial import ConvexHull
import sympy as sp


def data(r):
    assert 0.5 < r < 1.0
    h = sqrt(1-r*r)
    u = [np.array([cos(2*pi*i/3), sin(2*pi*i/3)]) for i in range(3)]
    v = [np.array([cos((2*i+1)*pi/3), sin((2*i+1)*pi/3)]) for i in range(3)]
    verts = np.array([list(p)+[0.] for p in u] +
                     [list(r*p)+[h] for p in v] +
                     [list(r*p)+[-h] for p in v])
    k = (1-r/2)/h
    m = (2-r)/(sqrt(3)*r)
    normal, const, kind = [], [], []
    for sign in (1,-1):
        normal.append(np.array([0.,0.,float(sign)]));const.append(h);kind.append('cap')
    for p in u:
        for sign in (1,-1):
            normal.append(np.array([*p,float(sign)*k]));const.append(1.);kind.append('slant')
    for i in range(3):
        for sign in (1,-1):
            t=np.array([cos(2*pi*i/3),sin(2*pi*i/3)])
            s=np.array([-t[1],t[0]])
            normal.append(np.array([*(t+sign*m*s),0.]));const.append(1.);kind.append('vertical')
    normal=np.array(normal);const=np.array(const)
    distance=const/np.linalg.norm(normal,axis=1)
    return h, verts, normal, const, kind, distance


def min_ball_lp(normal,const):
    c=np.array([0.,0.,0.,-1.])
    mat=np.column_stack([normal,np.linalg.norm(normal,axis=1)])
    sol=linprog(c,A_ub=mat,b_ub=const,bounds=[(None,None)]*4,method='highs')
    assert sol.success, sol.message
    return sol.x


checks=0
rho=brentq(lambda r:sqrt(1-r*r)-sqrt(3)*r/(2*sqrt(1-r+r*r)),2/3,2/sqrt(7),xtol=1.e-14)
assert 0.71786 < rho < 0.71788
checks+=1
rr=sp.symbols('r')
poly=sp.expand(4*(1-rr+rr**2)*(1-rr**2)-3*rr**2)
assert poly == -4*rr**4+4*rr**3-3*rr**2-4*rr+4
checks+=1
assert sp.factor(4*(1-rr+rr**2)*(1-rr**2) -
        3*rr**2*(2-rr-sp.Rational(3,4)*rr**2)) == -(rr-2)**2*(7*rr**2-4)/4
checks+=1
rstar=sqrt(3)-1
assert rstar>rho
checks+=1

samples = [0.5001,0.51,0.55,0.6,0.66,0.68,0.70,0.717,0.718,0.72,
           rstar,0.75,0.8,0.85,0.9,0.95,0.99,0.999]
for r in samples:
    h,V,A,b,kinds,dist=data(r)
    assert len(V)==9 and len(A)==14
    checks+=2
    # Every claimed facet supports the polytope and contains exactly 3 vertices.
    D=A@V.T-b[:,None]
    assert np.max(D)<2.e-12
    checks+=1
    for row in D:
        assert np.sum(np.abs(row)<2.e-10)==3
        checks+=1
    H=ConvexHull(V)
    assert len(H.vertices)==9 and len(H.simplices)==14
    checks+=2
    # The center and radius returned by independent linear programming.
    center=min_ball_lp(A,b)
    vertical=sqrt(3)*r/(2*sqrt(1-r+r*r))
    predicted=min(h,vertical)
    assert abs(center[-1]-predicted)<2.e-8,(r,center,predicted)
    checks+=1
    # Every planar-slanted facet lies farther away than the limiting orbit.
    slant=[d for d,t in zip(dist,kinds) if t=='slant']
    assert min(slant)>predicted-1.e-12
    checks+=1
    predicted_contacts=2 if r>rho else 6
    actual=sum(abs(d-predicted)<1.e-9 for d in dist)
    assert actual==predicted_contacts,(r,actual,predicted_contacts)
    checks+=1
    norm=np.linalg.norm(A,axis=1)
    if r < rho:
        # Extremal centers of the exact vertical incenter segment.
        for z in (-(h-vertical),0.,h-vertical):
            sl=A@np.array([0.,0.,z])+norm*vertical-b
            assert max(sl)<2.e-12,(r,z,max(sl))
            checks+=1
    else:
        # Nontrivial disk of planar centers (hence a 2D set).
        k=(1-r/2)/h; W=2*sqrt(1-r+r*r)/(sqrt(3)*r)
        epsilon=min((1-h*sqrt(1+k*k))/(1+sqrt(1+k*k)),
                    (1-h*W)/(1+W))*0.1
        for p in ((0.,0.),(epsilon,0.),(0.,epsilon),(-epsilon,-epsilon)):
            C=np.array([*p,0.]);
            assert np.max(A@C+norm*h-b)<2.e-12
            checks+=1

# A separate exact-parameter test at the transition.
h,V,A,b,kinds,dist=data(rho)
v=sqrt(3)*rho/(2*sqrt(1-rho+rho*rho))
assert abs(h-v)<1.e-12
assert sum(abs(d-h)<1.e-9 for d in dist)==8
checks+=2
print(f'PASS: {checks} checks; transition r={rho:.15f}, h={h:.15f}')
print(f'At volume maximizer: r={rstar:.15f}, inradius={sqrt(2*sqrt(3)-3):.15f}')
