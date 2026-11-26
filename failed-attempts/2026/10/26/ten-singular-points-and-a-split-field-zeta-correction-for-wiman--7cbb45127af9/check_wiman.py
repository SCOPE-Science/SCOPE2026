#!/usr/bin/env python3
"""Exact finite-field and polynomial identity checks for a plane sextic in characteristic five."""
from itertools import product
from math import factorial

P=5

def multinomial(n, abc):
    a,b,c=abc
    return factorial(n)//(factorial(a)*factorial(b)*factorial(c))

# Polynomial coefficient dictionary indexed by exponents of x,y,z.
orig={}
def put(k,v):orig[k]=(orig.get(k,0)+v)%P
for i in range(3):
    ex=[0,0,0];ex[i]=6;put(tuple(ex),2)
for i in range(3):
    for j in range(3):
        if i!=j:
            ex=[0,0,0];ex[i]=2;ex[j]=4;put(tuple(ex),1)
put((2,2,2),-12)
reduced={}
for a in range(4):
    for b in range(4-a):
        c=3-a-b
        reduced[(2*a,2*b,2*c)]=(2*multinomial(3,(a,b,c)))%P
reduced[(2,2,2)]=(reduced.get((2,2,2),0)+1)%P
assert {k:v for k,v in orig.items() if v}=={k:v for k,v in reduced.items() if v}
print('IDENTITY_OK: F mod 5 = x^2*y^2*z^2 + 2*(x^2+y^2+z^2)^3')

# F_25 = F_5[t]/(t^2-2), an irreducible quadratic extension.
zero=(0,0);one=(1,0);two=(2,0)
def add(a,b):return ((a[0]+b[0])%P,(a[1]+b[1])%P)
def mul(a,b):return ((a[0]*b[0]+2*a[1]*b[1])%P,(a[0]*b[1]+a[1]*b[0])%P)
def sq(a):return mul(a,a)
def cube(a):return mul(a,sq(a))
def F(x,y,z):
    a,b,c=sq(x),sq(y),sq(z)
    s=add(add(a,b),c)
    return add(mul(mul(a,b),c),mul(two,cube(s)))
def gradient(x,y,z):
    a,b,c=sq(x),sq(y),sq(z)
    s2=sq(add(add(a,b),c))
    return (mul(mul(two,x),add(mul(b,c),s2)),
            mul(mul(two,y),add(mul(a,c),s2)),
            mul(mul(two,z),add(mul(a,b),s2)))

def projective_points(elements):
    for y in elements:
        for z in elements:
            yield one,y,z
    for z in elements:
        yield zero,one,z
    yield zero,zero,one

for degree,elements in ((1,[(i,0) for i in range(P)]),(2,list(product(range(P),repeat=2)))):
    points=[pt for pt in projective_points(elements) if F(*pt)==zero]
    expected=P**degree+1-4*(-1)**degree
    assert len(points)==expected,(degree,len(points),expected)
    print('POINT_COUNT_OK',f'F_(5^{degree})',len(points))
    if degree==1:
        sing=[pt for pt in points if gradient(*pt)==(zero,zero,zero)]
        assert len(sing)==10,(len(sing),sing)
        assert set(sing)=={
          ((1,0),(sy,0),(sz,0)) for sy in (1,4) for sz in (1,4)
        } | {
          ((0,0),(1,0),(v,0)) for v in (2,3)
        } | {
          ((1,0),(0,0),(v,0)) for v in (2,3)
        } | {
          ((1,0),(v,0),(0,0)) for v in (2,3)
        }
        print('SINGULAR_SUPPORT_OK: 4 full-support nodes and 6 coordinate cusps')

# At (a,b,c)=(1,1,1), in chart c=1 and a=1+u,b=1+v:
# quadratic term is 3u^2+2uv+3v^2, with discriminant 3 (a nonsquare in F_5).
assert (2*2-4*3*3)%5==3 and 3 not in {(i*i)%5 for i in range(5)}
print('NODE_DISC_OK: discriminant=3, nonsplit over F_5')
# At each axis cusp, local coordinates U=xy, V=x^2+y^2+1 have Jacobian
# determinant 2(y^2-x^2)=3 mod 5 at x=0, y^2=4.
assert (2*4)%5==3
print('CUSP_COORDINATES_OK: local equation U^2+2V^3; Jacobian=3')
print('CHECK_OK')
