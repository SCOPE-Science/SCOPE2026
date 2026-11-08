#!/usr/bin/env python3
"""Independent numerical checks of the sharp path-tetrahedron dihedral law.

Only standard Python; an analytic proof is supplied separately.
"""
import math
import random

PHI = (1.0 + math.sqrt(5.0))/2.0
THETA = math.acos(1.0/PHI)


def sub(u,v):
    return tuple(x-y for x,y in zip(u,v))


def cross(u,v):
    return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])


def dot(u,v):
    return sum(x*y for x,y in zip(u,v))


def direct_dihedrals(a,b,c):
    pts = [(0.,0.,0.),(a,0.,0.),(a,b,0.),(a,b,c)]
    normals=[]
    for omit in range(4):
        idx=[j for j in range(4) if j!=omit]
        x,y,z=(pts[j] for j in idx)
        N=cross(sub(y,x),sub(z,x))
        if dot(N,sub(pts[omit],x))>0:
            N=tuple(-z for z in N)
        norm=math.sqrt(dot(N,N))
        normals.append(tuple(z/norm for z in N))
    return sorted(math.acos(max(-1.,min(1.,-dot(normals[i],normals[j])))) for i in range(4) for j in range(i+1,4))


def formulas(a,b,c):
    return sorted([math.pi/2]*3 + [math.atan(a/b), math.atan(c/b),
                                  math.acos((a/b)*(c/b)/(math.hypot(1,a/b)*math.hypot(1,c/b)))])


def quality(a,b,c):
    return min(formulas(a,b,c))


def analytic_feasible(a,b,c,t):
    x,y=a/b,c/b
    return x>=math.tan(t)-1e-10 and y>=math.tan(t)-1e-10 and (x*y/math.hypot(1,x)/math.hypot(1,y))<=math.cos(t)+1e-10


def main():
    random.seed(129582)
    checks=0
    for _ in range(2500):
        a,b,c=(10.0**random.uniform(-2.0,2.0) for _ in range(3))
        direct=direct_dihedrals(a,b,c)
        predicted=formulas(a,b,c)
        assert max(abs(x-y) for x,y in zip(direct,predicted))<2e-11,(a,b,c,direct,predicted)
        assert quality(a,b,c)<=THETA+1e-12
        checks+=2
        t=random.uniform(0.001, THETA+.07)
        assert (quality(a,b,c)>=t-1e-10)==analytic_feasible(a,b,c,t)
        checks+=1
    assert abs(math.sin(THETA)**2-math.cos(THETA))<1e-14
    assert abs(math.tan(THETA)-math.sqrt(PHI))<1e-14
    assert abs(quality(math.sqrt(PHI),1.,math.sqrt(PHI))-THETA)<1e-14
    checks+=3
    for j in range(1,1001):
        t=math.pi/4+j*(THETA-math.pi/4)/1000
        lo=math.tan(t)
        up=math.cos(t)/math.sqrt(math.sin(t)**2-math.cos(t)**2)
        assert lo<=up+1e-9
        alpha=math.atan(up)
        assert abs(min(alpha, t, math.acos(math.sin(alpha)*math.sin(t)))-t)<3e-12
        checks+=2
    for t in [0.1,0.5,math.pi/4]:
        assert analytic_feasible(1e8,1,math.tan(t),t)
        checks+=1
    print('PATH_TETRA_DIHEDRAL_CHECKS_OK',checks)


if __name__=='__main__':
    main()
