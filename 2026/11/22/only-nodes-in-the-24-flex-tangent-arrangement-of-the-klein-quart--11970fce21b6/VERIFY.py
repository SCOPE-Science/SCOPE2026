#!/usr/bin/env python3
"""Exact finite arithmetic certificate for the 24 Klein flex tangents."""
from collections import Counter
from itertools import combinations

def projective_normalize(coords, p):
    for first in coords:
        if first % p:
            inv = pow(first, -1, p)
            return tuple((v * inv) % p for v in coords)
    raise AssertionError("zero projective vector")

def cross(a, b, p):
    return projective_normalize((a[1]*b[2]-a[2]*b[1],
                                 a[2]*b[0]-a[0]*b[2],
                                 a[0]*b[1]-a[1]*b[0]), p)

def point_on_line(point, line, p):
    return sum(x*y for x,y in zip(point,line)) % p == 0

def check(p):
    points = ([(1,a,b) for a in range(p) for b in range(p)]
              + [(0,1,a) for a in range(p)] + [(0,0,1)])
    assert len(points) == p*p+p+1
    def F(v):
        x,y,z=v
        return (x**3*y+y**3*z+z**3*x)%p
    def H(v):
        x,y,z=v
        return (x**5*z-5*x*x*y*y*z*z+x*y**5+y*z**5)%p
    def gradient(v):
        x,y,z=v
        return projective_normalize((3*x*x*y+z**3,
                            x**3+3*y*y*z, y**3+3*z*z*x),p)
    flexes=[v for v in points if F(v)==0 and H(v)==0]
    assert len(flexes)==24, (p, len(flexes))
    lines=[gradient(v) for v in flexes]
    assert len(set(lines)) == 24, (p, 'repeated tangent')
    crossings=[]
    for line_a,line_b in combinations(lines,2):
        pt=cross(line_a,line_b,p)
        assert sum(point_on_line(pt,line,p) for line in lines)==2, (p,pt)
        crossings.append(pt)
    assert len(crossings)==276 and len(set(crossings))==276
    return len(points),len(flexes),len(set(lines)),len(set(crossings))

if __name__=='__main__':
    assert check(29)==(871,24,24,276)
    assert check(43)==(1893,24,24,276)
    assert check(71)==(5113,24,24,276)
    print('KLEIN_FLEX_TANGENT_NODAL_ARRANGEMENT_OK')
