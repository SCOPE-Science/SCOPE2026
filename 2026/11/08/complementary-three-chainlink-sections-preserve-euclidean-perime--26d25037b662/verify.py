"""Standalone checks of the three-coordinate chainlink section perimeter identity.

Uses only the Python standard library. Polygon vertices are reconstructed from
exact half-plane intersections, independently of the analytical perimeter profile.
Run: python verify_chainlink_perimeter.py
"""
from fractions import Fraction as F
from itertools import combinations
from math import atan2, sqrt
from random import Random


def section_vertices(a, ell, t):
    a, b, c = map(F, a)
    ell, t = F(ell), F(t)
    # The first two coordinates are u,v; the third is t-u-v.
    constraints = [
        (-1, 0, 0), (1, 0, a),
        (0, -1, 0), (0, 1, b),
        (-1, -1, c-t), (1, 1, t),
        (1, -1, a-ell), (1, 2, b-ell+t), (-2, -1, c-ell-t),
    ]
    vertices = set()
    for (p, q, r), (s, w, z) in combinations(constraints, 2):
        det = p*w-q*s
        if det == 0:
            continue
        u, v = F(r*w-q*z, det), F(p*z-r*s, det)
        if all(alpha*u+beta*v <= gamma for alpha,beta,gamma in constraints):
            vertices.add((u,v))
    if len(vertices) < 3:
        return sorted(vertices)
    cu = sum(u for u,v in vertices)/len(vertices)
    cv = sum(v for u,v in vertices)/len(vertices)
    return sorted(vertices, key=lambda x: atan2(float(x[1]-cv), float(x[0]-cu)))


def perimeter(vertices):
    if len(vertices) < 3:
        return 0.
    return sum(sqrt(float((u-x)**2+(v-y)**2+(u+v-x-y)**2))
               for (x,y),(u,v) in zip(vertices,vertices[1:]+vertices[:1]))


def g(ell, z):
    return max(F(0), min(2*ell, z+ell))


def k(ell, z):
    return max(F(0), ell-abs(z))


def interval_length(b, c, z):
    return max(F(0), min(b, z)-max(F(0), z-c))


def profiles(a, ell, t):
    a = tuple(map(F, a)); ell, t = F(ell), F(t)
    n = sum(a)
    box = sum(interval_length(a[(i+1)%3],a[(i+2)%3],t) +
              interval_length(a[(i+1)%3],a[(i+2)%3],t-a[i])
              for i in range(3))*sqrt(2)
    s = sum(g(ell,t-ai)-g(ell,t-(n-ai)) for ai in a)
    q = sum(k(ell,t-ai)+k(ell,t-(n-ai)) for ai in a)
    diag = sqrt(6)/2*float(s)
    coordinate = box-sqrt(2)*float(s)-sqrt(2)/2*float(q)
    return coordinate, diag


def squared_edges(vertices):
    return sorted((u-x)**2+(v-y)**2+(u+v-x-y)**2
                  for (x,y),(u,v) in zip(vertices,vertices[1:]+vertices[:1]))


def assert_close(x,y,tol=1e-8):
    assert abs(x-y)<tol, (x,y)


def main():
    rng=Random(89371)
    count=0
    for test in range(250):
        ell=F(rng.randint(1,4),rng.randint(1,3))
        a=tuple(2*ell+F(rng.randint(0,10),rng.randint(1,3)) for _ in range(3))
        n=sum(a)
        t=n*F(rng.randint(1,49),50)
        for h in (t,n-t):
            coords,diag=profiles(a,ell,h)
            actual=perimeter(section_vertices(a,ell,h))
            assert_close(actual,coords+diag)
            assert coords >= -1e-8 and diag>=-1e-8
        p1=sum(profiles(a,ell,t))
        p2=sum(profiles(a,ell,n-t))
        assert_close(p1,p2)
        for u,v in zip(profiles(a,ell,t),profiles(a,ell,n-t)):
            assert_close(u,v)
        count+=1
    # Different (squared) edge-length multisets despite matching perimeters.
    a=(F(6),F(4),F(5));ell=F(2)
    v=section_vertices(a,ell,F(5))
    w=section_vertices(a,ell,F(10))
    assert len(v)==len(w)==6
    assert squared_edges(v)!=squared_edges(w)
    assert_close(perimeter(v),6*sqrt(2)+3*sqrt(6))
    assert_close(perimeter(w),6*sqrt(2)+3*sqrt(6))
    # The half-size hypothesis is substantive, not an assertion beyond its domain.
    bad=(F(3),F(4),F(5)); bad_l=F(2)
    p=perimeter(section_vertices(bad,bad_l,F(5)))
    q=perimeter(section_vertices(bad,bad_l,F(7)))
    assert_close(p,(9*sqrt(6)+3*sqrt(2))/2)
    assert_close(q,4*sqrt(6)+2*sqrt(2))
    assert_close(p-q,(sqrt(6)-sqrt(2))/2)
    print('THREE_CHAINLINK_SECTION_PERIMETER_CHECKS_PASSED',count)

if __name__=='__main__':
    main()
