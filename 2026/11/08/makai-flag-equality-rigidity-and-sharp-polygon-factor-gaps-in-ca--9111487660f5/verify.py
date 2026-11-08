"""Exact-rational planar and product checks for Makai/flag polygon products.

Only the Python standard library is needed. The finite checks below corroborate
explicit formulas; the dimension-free assertions require the written proof.
"""
from fractions import Fraction as Q
from math import factorial, pi, prod, sin


def area(v):
    return abs(sum(x * Y - y * X for (x, y), (X, Y)
                   in zip(v, v[1:] + v[:1]))) / 2


def clip(poly, a, b, c):
    out=[]
    for U,V in zip(poly,poly[1:]+poly[:1]):
        f=a*U[0]+b*U[1]-c
        g=a*V[0]+b*V[1]-c
        if f<=0: out.append(U)
        if (f<0<g) or (g<0<f):
            t=f/(f-g)
            out.append((U[0]+t*(V[0]-U[0]),U[1]+t*(V[1]-U[1])))
        elif f>0 and g==0: out.append(V)
    return out


def makai(v):
    diffs=[(a[0]-b[0],a[1]-b[1]) for a in v for b in v]
    B=Q(4)
    polar=[(-B,-B),(B,-B),(B,B),(-B,B)]
    for u,vv in diffs:
        polar=clip(polar,u,vv,Q(1))
    return area(v)*area(polar)

checks=0
for p in [Q(1),Q(6,5),Q(3,2),Q(2),Q(5),Q(11)]:
    for q in [Q(1),Q(7,6),Q(5,4),Q(3),Q(7)]:
        if p<q: continue
        vertices=[(Q(1),Q(0)),(Q(0),Q(1)),(-p,Q(0)),(Q(0),-q)]
        direct=makai(vertices)
        formula=Q(2)-(q*(p-q)**2+(p*q-1)**2)/(2*p*q*(p+1)*(q+1))
        assert direct==formula,(p,q,direct,formula)
        assert (direct==2)==(p==q==1)
        checks+=2

tri=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(0),Q(1))]
square=[(Q(1),Q(1)),(-Q(1),Q(1)),(-Q(1),-Q(1)),(Q(1),-Q(1))]
hexagon=[(Q(2),Q(0)),(Q(1),Q(1)),(-Q(1),Q(1)),(-Q(2),Q(0)),(-Q(1),-Q(1)),(Q(1),-Q(1))]
assert (makai(tri),makai(square),makai(hexagon))==(Q(3,2),Q(2),Q(9,4))
checks+=3

# Flag and beta-factor bookkeeping in dimension four.
for A,nA,B,nB,expect in [(square,4,square,4,Q(1)),
                           (tri,3,tri,3,Q(1)),
                           (square,4,hexagon,6,Q(3,4)),
                           (hexagon,6,hexagon,6,Q(9,16))]:
    volume_product=Q(2)*Q(2)/Q(24)*makai(A)*makai(B)
    flags=factorial(4)*nA*nB
    ratio=factorial(4)**2*volume_product/flags
    assert ratio==expect,(nA,nB,ratio,expect)
    checks+=1

# Strictly decreasing sharp even-gon factor from n=4 onward.
last=2.0
for n in range(4,202,2):
    z=(n/2)*sin(pi/n)**2
    assert z < last
    assert z <= (1 if n==4 else .75)+1e-13
    last=z
    checks+=1
print('MAKAI_POLYGON_PRODUCT_OK',checks)
