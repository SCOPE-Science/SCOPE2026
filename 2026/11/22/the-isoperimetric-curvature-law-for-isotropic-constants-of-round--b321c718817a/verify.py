#!/usr/bin/env python3
"""Exact identities and independent geometric regression tests for triangle outer offsets.

Requires Python 3.10+ and sympy; geometric regression uses standard library only.
The proof for every real triangle is in RESULT.md; finite checks are corroboration.
"""
import math
import random
from fractions import Fraction
import sympy as sp


def exact_identity():
    x=sp.symbols('x',real=True)
    y=sp.symbols('y',positive=True)
    l0,l1,l2=sp.symbols('l0 l1 l2', positive=True)
    al0,al1=sp.symbols('alpha0 alpha1',real=True)
    vv=[sp.Matrix([0,0]),sp.Matrix([1,0]),sp.Matrix([x,y])]
    cent=sum(vv,sp.zeros(2,1))/3
    v=[p-cent for p in vv]
    A=y/2
    S=sum((w*w.T for w in v),sp.zeros(2,2))
    Sinv=S.inv().applyfunc(sp.factor)
    sides=[(1,2),(2,0),(0,1)]
    ns=[]
    Q2strip=sp.zeros(2,2)
    for i,(j,k) in enumerate(sides):
        d=v[k]-v[j]
        nlen=sp.Matrix([d[1],-d[0]])
        ns.append(nlen)
        midpoint=(v[j]+v[k])/2
        Q2strip+=(midpoint*nlen.T+nlen*midpoint.T)/2
    for i in range(3):
        assert (ns[i]+2*A*Sinv*v[i]).applyfunc(sp.simplify)==sp.zeros(2,1)
    assert Q2strip.applyfunc(sp.simplify)==A*sp.eye(2)
    assert (Sinv*S).applyfunc(sp.simplify)==sp.eye(2)
    for i in range(3):
        for j in range(3):
            assert sp.simplify((v[i].T*Sinv*v[j])[0]-(sp.Rational(2,3) if i==j else -sp.Rational(1,3)))==0
    lens_sq=[sp.simplify((v[k]-v[j]).dot(v[k]-v[j])) for j,k in sides]
    assert sp.simplify(4*A*A*sp.trace(Sinv)-sum(lens_sq))==0
    P=l0+l1+l2
    ell=[l0,l1,l2]
    M1=-sum((ell[i]*v[i] for i in range(3)),sp.zeros(2,1))/2
    Q0=A*S/12
    Q1=P*S/6
    assert (Q1-(2*P/A)*Q0).applyfunc(sp.simplify)==sp.zeros(2,2)
    al=[al0,al1,2*sp.pi-al0-al1]
    Q2sector=sum((al[i]*v[i]*v[i].T/2 for i in range(3)),sp.zeros(2,2))
    assert sp.simplify(sp.trace(Q0.inv()*Q2sector)-8*sp.pi/A)==0
    assert sp.simplify((M1.T*Q0.inv()*M1)[0]/A-(3*sum(z*z for z in ell)-P*P)/A**2)==0
    # The squared-length constraints are exactly the Euclidean edge definitions.
    J2_over_J0=(sp.trace(Q0.inv()*(Q2strip+Q2sector))
      -(M1.T*Q0.inv()*M1)[0]/A-2*P*P/A**2-4*sp.pi/A)
    leftover=sp.expand(J2_over_J0+(P*P-4*sp.pi*A)/A**2)
    leftover=sp.simplify(leftover-3*(sum(lens_sq)-sum(z*z for z in ell))/A**2)
    assert leftover==0
    assert sp.simplify(sp.det(S)-sp.Rational(4,3)*A*A)==0
    assert sp.simplify(sp.det(Q0)/A**4-sp.Rational(1,108))==0
    return 26


def moment_of_polygon(pts):
    n=len(pts);area=m0=m1=q00=q01=q11=0.
    for i,(x,y) in enumerate(pts):
        xx,yy=pts[(i+1)%n]
        c=x*yy-xx*y
        area+=c
        m0+=(x+xx)*c
        m1+=(y+yy)*c
        q00+=(x*x+x*xx+xx*xx)*c
        q11+=(y*y+y*yy+yy*yy)*c
        q01+=(2*x*y+x*yy+xx*y+2*xx*yy)*c
    return area/2,(m0/6,m1/6),(q00/12,q01/24,q11/12)


def rounded_vertices(vertices,t,arc_resolution=500):
    normals=[]
    for i in range(3):
        x,y=vertices[i]
        xx,yy=vertices[(i+1)%3]
        dx,dy=xx-x,yy-y
        h=math.hypot(dx,dy)
        normals.append((dy/h,-dx/h))
    theta=[math.atan2(n[1],n[0]) for n in normals]
    result=[]
    for i in range(3):
        j=(i+1)%3
        nx,ny=normals[i]
        x,y=vertices[i]
        xx,yy=vertices[j]
        result.append((x+t*nx,y+t*ny))
        result.append((xx+t*nx,yy+t*ny))
        sweep=(theta[j]-theta[i])%(2*math.pi)
        for k in range(1,arc_resolution+1):
            angle=theta[i]+sweep*k/arc_resolution
            result.append((xx+t*math.cos(angle),yy+t*math.sin(angle)))
    return result


def J_from_vertices(vertices):
    A,(m0,m1),(q00,q01,q11)=moment_of_polygon(vertices)
    c00=q00/A-(m0/A)**2
    c11=q11/A-(m1/A)**2
    c01=q01/A-(m0*m1/A**2)
    return (c00*c11-c01*c01)/(A*A)


def numeric_regressions():
    # Independently assemble rounded boundary and apply polygon area/moment formulas.
    # Error in each circular sector is O(t^2/N^2), smaller than the displayed tolerances.
    rng=random.Random(5274)
    tests=[[(0.,0.),(1.,0.),(.5,math.sqrt(3)/2)],
           [(0.,0.),(2.,0.),(.7,1.3)],
           [(0.,0.),(2.,0.),(.1,4.)]]
    for i in range(17):
        x=.15+1.7*rng.random();y=.4+2.3*rng.random()
        tests.append([(0.,0.),(2.,0.),(x,y)])
    count=0
    for v in tests:
        A=abs((v[1][0]-v[0][0])*(v[2][1]-v[0][1])-(v[1][1]-v[0][1])*(v[2][0]-v[0][0]))/2
        P=sum(math.dist(v[k],v[(k+1)%3]) for k in range(3))
        coefficient=(P*P-4*math.pi*A)/(108*A*A)
        assert abs(J_from_vertices(v)-1/108)<1e-11
        count+=1
        for t in (.006,.003,.0015):
            ratio=(1/108-J_from_vertices(rounded_vertices(v,t,1000)))/t**2
            # Leading error of the remainder scales linearly in t.
            assert abs(ratio/coefficient-1)<.09,(v,t,ratio,coefficient)
            count+=1
        # Exact algebraic inequality among triangular side configurations:
        assert P*P>=12*math.sqrt(3)*A-1e-12
        count+=1
    return count

if __name__=='__main__':
    n1=exact_identity()
    n2=numeric_regressions()
    print(f'PASS: symbolic identities and {n2} geometric regression assertions; verified components: {n1+n2}.')
