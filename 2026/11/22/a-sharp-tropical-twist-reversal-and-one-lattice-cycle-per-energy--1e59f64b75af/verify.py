"""Exact independent arithmetic controls for the three-season tropical Lyness map.

Run with: python verify.py   (SymPy is needed only for the rational-source invariant check).
Finite tests check the algebra/proof inputs; the all-level theorem is proved analytically.
"""
from fractions import Fraction as Q
from math import gcd


def T(a, z):
    x, y = z
    return (y, max(Q(a), y) - x)


def F(z):
    for a in (0, 0, 1):
        z = T(a, z)
    return z


def H(z):
    x, y = z
    return max(-x, -y, -x-y, x-y-1, x, y-1, y-x-1)


def vertices(h):
    h = Q(h)
    if h <= 0:
        raise ValueError('positive levels only')
    if h <= 1:
        return [(-h,Q(0)), (Q(0),-h), (h,-h), (h,h+1),
                (Q(0),h+1),(-h,Q(1))]
    return [(-h,Q(0)),(Q(0),-h),(Q(1),-h),(h,Q(-1)),
            (h,h+1),(Q(0),h+1),(-h,Q(1))]


def lattice_length(a, b):
    dx,dy = b[0]-a[0],b[1]-a[1]
    # Sides have directions (1,0), (0,1), (1,-1), (1,1).
    assert (dx==0 or dy==0 or abs(dx)==abs(dy)), (a,b)
    return max(abs(dx),abs(dy))


def perimeter(h):
    v=vertices(h)
    return sum((lattice_length(a,b) for a,b in zip(v,v[1:]+v[:1])), Q(0))


def area(h):
    v=vertices(h)
    return sum((a[0]*b[1]-a[1]*b[0] for a,b in zip(v,v[1:]+v[:1])),Q(0))/2


def expected_period(p,q):
    h=Q(p,q)
    return (6*p+2*q)//gcd(q,2) if h<=1 else 5*p+3*q


def algebraic_source_identity():
    try:
        import sympy as s
    except ImportError:
        print('SYMPY_SOURCE_IDENTITY_NOT_RUN (install sympy)')
        return
    x,y,a,b,c = s.symbols('x y a b c')
    def R(alpha,z):
        X,Y=z
        return Y,(alpha+Y)/X
    def V(z):
        X,Y=z
        N = c*X**2*Y+a*X*Y**2+b*X**2+b*Y**2+(a+b*c)*X+(c+a*b)*Y+a*c
        return N/(X*Y)
    z=(x,y)
    for alpha in (a,b,c):
        z=R(alpha,z)
    assert s.factor(V(z)-V((x,y))) == 0
    print('RATIONAL_THREE_SEASON_INVARIANT_IDENTITY_OK')


def verify():
    algebraic_source_identity()
    for xx in range(-39,40):
        for yy in range(-39,40):
            z=(Q(xx,7),Q(yy,7))
            assert H(F(z)) == H(z)
    print('TROPICAL_H_CONSERVATION_RATIONAL_GRID_OK',79*79)
    polygons=0
    rational_orbits=0
    for p in range(1,30):
        for q in range(1,18):
            if gcd(p,q)>1:
                continue
            h=Q(p,q)
            v=vertices(h)
            assert all(H(x)==h for x in v)
            assert perimeter(h)==(6*h+2 if h<=1 else 5*h+3)
            assert area(h)==(3*h*h+2*h if h<=1 else (5*h*h+6*h-1)/2)
            assert F(v[0]) == ((h,1-h) if h<=1 else (h,Q(0)))
            P=expected_period(p,q)
            initial=v[0]
            point=initial
            for t in range(1,P+1):
                point=F(point)
                assert H(point)==h
                if point==initial:
                    break
            assert point==initial and t==P, (p,q,t,P)
            polygons+=1
            rational_orbits+=P
    print('RATIONAL_POLYGON_AND_PRIME_PERIOD_TESTS_OK',polygons,rational_orbits)
    for m in range(1,101):
        v=vertices(Q(m))
        # Independent generation of *all* lattice boundary points.
        boundary=set()
        for a,b in zip(v,v[1:]+v[:1]):
            d=(int(b[0]-a[0]),int(b[1]-a[1]))
            g=gcd(abs(d[0]),abs(d[1]))
            assert g>0
            step=(d[0]//g,d[1]//g)
            for t in range(g):
                boundary.add((a[0]+t*step[0],a[1]+t*step[1]))
        assert len(boundary)==5*m+3
        assert all(H(z)==m for z in boundary)
        z=(-Q(m),Q(0))
        observed=set()
        for i in range(5*m+3):
            assert z not in observed
            observed.add(z)
            z=F(z)
        assert z==(-Q(m),Q(0))
        assert observed==boundary
    assert F((Q(0),Q(0)))==(Q(0),Q(1))
    assert F((Q(0),Q(1)))==(Q(0),Q(0))
    assert F((Q(0),Q(1,2)))==(Q(0),Q(1,2))
    print('ALL_INTEGER_SHELLS_SINGLE_ORBIT_OK',100, sum(5*m+3 for m in range(1,101)))
    h1=Q(2,3);h2=Q(3)
    assert (2*h1+1)/perimeter(h1) == (2*h2+1)/perimeter(h2) == Q(7,18)
    print('TWO_DISTINCT_18_CYCLES_SAME_ROTATION_OK')
    print('VERIFY_OK')

if __name__=='__main__':
    verify()
