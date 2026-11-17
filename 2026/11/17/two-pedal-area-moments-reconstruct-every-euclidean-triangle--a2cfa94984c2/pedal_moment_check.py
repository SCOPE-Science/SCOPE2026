"""Exact arithmetic checks for normalized pedal-area moments.
Run: python pedal_moment_check.py
The proof is in RESULT.md; these checks do not certify all triangles.
"""
from fractions import Fraction as F
from math import factorial


def dot(u, v):
    return u[0]*v[0]+u[1]*v[1]


def sub(u, v):
    return (u[0]-v[0], u[1]-v[1])


def cross(u, v):
    return u[0]*v[1]-u[1]*v[0]


def circumcenter(A,B,C):
    x1,y1=A; x2,y2=B; x3,y3=C
    aa=2*(x2-x1); bb=2*(y2-y1)
    cc=2*(x3-x1); dd=2*(y3-y1)
    ee=dot(B,B)-dot(A,A); ff=dot(C,C)-dot(A,A)
    D=aa*dd-bb*cc
    assert D != 0
    return ((ee*dd-bb*ff)/D,(aa*ff-ee*cc)/D)


def project(P,A,B):
    v=sub(B,A)
    t=dot(sub(P,A),v)/dot(v,v)
    return (A[0]+t*v[0],A[1]+t*v[1])


def pedal_area_ratio(P,A,B,C):
    H1=project(P,B,C)
    H2=project(P,C,A)
    H3=project(P,A,B)
    return cross(sub(H2,H1),sub(H3,H1))/cross(sub(B,A),sub(C,A))


def dmom(a,b,c):
    # E[U1^a U2^b U3^c], U~Dirichlet(1,1,1).
    return F(2*factorial(a)*factorial(b)*factorial(c),factorial(a+b+c+2))


def check_triangle(A,B,C):
    O=circumcenter(A,B,C)
    radius2=dot(sub(A,O),sub(A,O))
    squared=[dot(sub(B,C),sub(B,C))/radius2,
             dot(sub(C,A),sub(C,A))/radius2,
             dot(sub(A,B),sub(A,B))/radius2]
    e1=sum(squared)
    e2=sum(squared[i]*squared[j] for i in range(3) for j in range(i+1,3))
    e3=squared[0]*squared[1]*squared[2]
    assert e3==4*e2-e1*e1
    # By barycentric identity, Q = (a U2 U3 + b U3 U1 + c U1 U2)/4.
    mu=(squared[0]*dmom(0,1,1)+squared[1]*dmom(1,0,1)+squared[2]*dmom(1,1,0))/4
    assert mu == e1/48
    exponents=[(0,1,1),(1,0,1),(1,1,0)]
    nu=F(0)
    for i in range(3):
        for j in range(3):
            aa=tuple(exponents[i][k]+exponents[j][k] for k in range(3))
            nu+=squared[i]*squared[j]*dmom(*aa)/16
    assert nu == (e1*e1-e2)/1440
    assert e1 == 48*mu
    assert e2 == (48*mu)**2-1440*nu
    assert e3 == 4*e2-e1*e1
    for i,j in [(F(0),F(0)),(F(1,3),F(1,3)),(F(1,2),F(1,4)),(F(1,7),F(2,7))]:
        k=1-i-j
        P=(i*A[0]+j*B[0]+k*C[0],i*A[1]+j*B[1]+k*C[1])
        actual=pedal_area_ratio(P,A,B,C)
        theoretical=(1-dot(sub(P,O),sub(P,O))/radius2)/4
        assert actual==theoretical, (A,B,C,P,actual,theoretical)
    return (mu,nu,tuple(squared))

# Acute, right, obtuse: exact rational coordinates.
for coordinates in [((0,0),(4,0),(1,3)),
                    ((0,0),(4,0),(0,3)),
                    ((0,0),(4,0),(1,F(1,2)))]:
    values=check_triangle(*[tuple(map(F,v)) for v in coordinates])
    print('checked:', values)

# Two non-similar isosceles triangles with identical first moment.
def isosceles_squared(x):
    u=4*(1-x)
    v=16*x*(1-x)
    return (u,u,v)

p=isosceles_squared(F(1,8))
q=isosceles_squared(F(3,8))
assert p!=q and sum(p)==sum(q)==F(35,4)
assert sum(p[i]*p[j] for i in range(3) for j in range(i+1,3))!=sum(q[i]*q[j] for i in range(3) for j in range(i+1,3))
print('one-moment collision:',p,q,'mean',F(35,192))
print('PEDAL_MOMENT_TOMOGRAPHY_CHECKS_OK')
