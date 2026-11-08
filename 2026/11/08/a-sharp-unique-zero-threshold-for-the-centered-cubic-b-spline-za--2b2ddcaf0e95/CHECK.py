"""Exact Bernstein certificate for the cubic B-spline Zak zero theorem.

Run with Python 3 and SymPy. All branch decisions and coefficients are rational.
The certificate checks strict positivity throughout the relevant trapezoid;
there is no numerical sampling, tolerance, or floating-point test.
"""
from fractions import Fraction as F
from math import factorial
from sympy import symbols, expand, Poly, Rational

U,V = symbols('u v')
a,b,c = symbols('a b c')

def rat(z):
    return Rational(z.numerator, z.denominator)

def polygon_area(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]
                   -poly[i][1]*poly[(i+1)%len(poly)][0]
                   for i in range(len(poly)))) / 2

def cut(poly, A, B, C, sign):
    result=[]
    for p,q in zip(poly, poly[1:]+poly[:1]):
        x0,y0=p; x1,y1=q
        d0=sign*(A*x0+B*y0-C)
        d1=sign*(A*x1+B*y1-C)
        if d0 >= 0:
            result.append(p)
        if d0*d1 < 0:
            t=d0/(d0-d1)
            result.append((x0+t*(x1-x0),y0+t*(y1-y0)))
        elif d0 < 0 and d1 == 0:
            result.append(q)
    out=[]
    for p in result:
        if not out or out[-1] != p:
            out.append(p)
    if len(out)>1 and out[-1]==out[0]:
        out.pop()
    if len(out)<3 or polygon_area(out)==0:
        return []
    return out

# The transform has terms only for k in {-3,...,3} on this trapezoid.
base=[(F(4,7),F(0)),(F(1),F(0)),
      (F(1),F(1,2)),(F(4,7),F(2,7))]
cells=[base]
for j in (1,2,3):
    for s in (-1,1):
        for threshold in (1,2):
            nxt=[]
            for pol in cells:
                for side in (1,-1):
                    piece=cut(pol,j,s,F(threshold),side)
                    if piece:
                        nxt.append(piece)
            cells=nxt
assert sum(map(polygon_area,cells),F(0))==polygon_area(base)
assert len(cells)==8

def bspline_piece(t, location):
    if location>=2:
        return 0
    if location>=1:
        return (2-t)**3/6
    return (4-6*t*t+3*t**3)/6

def inequalities(poly):
    x=sum(p[0] for p in poly)/len(poly)
    y=sum(p[1] for p in poly)/len(poly)
    delta=[]
    for j in (1,2,3):
        delta.append(bspline_piece(j*U-V,j*x-y)
                     -bspline_piece(j*U+V,j*x+y))
    return [expand(delta[1]-4*delta[2]),
            expand(delta[0]-2*delta[1]+3*delta[2])]

def bernstein(tri,f):
    # Homogenize a polynomial in (u,v) to degree 3 after its exact
    # affine pullback to barycentric coordinates a,b,c.
    pu=sum(t*rat(tri[j][0]) for j,t in enumerate((a,b,c)))
    pv=sum(t*rat(tri[j][1]) for j,t in enumerate((a,b,c)))
    hom=sum(coef*pu**i*pv**j*(a+b+c)**(3-i-j)
            for (i,j),coef in Poly(f,U,V).terms())
    P=Poly(expand(hom),a,b,c)
    return {(i,j,k):P.coeff_monomial(a**i*b**j*c**k)
            *factorial(i)*factorial(j)*factorial(k)/6
            for i in range(4) for j in range(4-i)
            for k in [3-i-j]}

tris=0; coeffs=0; zeros=0; strict_vertices=0
for cell in cells:
    pair=inequalities(cell)
    for i in range(1,len(cell)-1):
        tr=[cell[0],cell[i],cell[i+1]]
        assert polygon_area(tr)>0
        tris+=1
        for f in pair:
            bern=bernstein(tr,f)
            coeffs+=len(bern)
            zeros+=sum(v==0 for v in bern.values())
            assert all(v>=0 for v in bern.values())
            # Every point with v>0 has a positive barycentric weight
            # at a vertex with v>0.  Its positive Bernstein pure-cube
            # coefficient proves strict interior/boundary positivity.
            for j,p in enumerate(tr):
                if p[1]>0:
                    mon=tuple(3 if i==j else 0 for i in range(3))
                    assert bern[mon]>0
                    strict_vertices+=1
assert tris>=8
assert coeffs==20*tris
print('CHECK_OK cells=%s triangles=%s bernstein_coefficients=%s zero_coefficients=%s strict_vertex_tests=%s'
      %(len(cells),tris,coeffs,zeros,strict_vertices))
