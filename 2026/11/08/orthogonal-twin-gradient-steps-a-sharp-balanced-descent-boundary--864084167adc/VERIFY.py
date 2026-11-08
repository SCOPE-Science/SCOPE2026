"""Exact-rational checks for a two-path gradient-distance step on planar SPD quadratics.

The analytic theorem in RESULT.md proves the quantified claims; these finite
checks independently exercise its formulas and boundary examples.
Requires only the Python standard library.
"""
from fractions import Fraction as F
from itertools import product


def matvec(A, x):
    return (A[0][0]*x[0]+A[0][1]*x[1], A[1][0]*x[0]+A[1][1]*x[1])


def inverse2(B):
    a,c=B[0]
    _,d=B[1]
    det=a*d-c*c
    assert a>0 and det>0
    return ((d/det, -c/det),(-c/det,a/det))


def add(x,y):
    return (x[0]+y[0],x[1]+y[1])


def scalar(t,x):
    return (t*x[0],t*x[1])


def quad(A,x):
    v=matvec(A,x)
    return (x[0]*v[0]+x[1]*v[1])/2


def verify_step(B,U,V,eta):
    A=inverse2(B)
    x=matvec(B,(U,F(0)))
    z=matvec(B,(F(0),V))
    p=(F(-1),F(0));q=(F(0),F(-1))
    alpha=x[0]-z[0]
    beta=z[1]-x[1]
    if alpha<=0 or beta<=0:
        return False
    y=add(x,scalar(alpha,p))
    assert y == add(z,scalar(beta,q))
    xp=add(x,scalar(eta*alpha,p))
    zp=add(z,scalar(eta*beta,q))
    assert add(xp,scalar(F(-1),zp))==scalar(1-eta,add(x,scalar(F(-1),z)))
    return quad(A,xp)/quad(A,x),quad(A,zp)/quad(A,z)


checks=0
for s,t in product([F(1),F(2),F(3,2)],[F(1),F(3),F(4,3)]):
    for r,eta in product([F(-4,5),F(-1,2),F(0),F(1,4),F(1,2),F(3,5),F(3,4)],
                         [F(1,5),F(1,2),F(3,4),F(1)]):
        a=s*s; d=t*t; c=-r*s*t
        B=((a,c),(c,d))
        rx,rz=verify_step(B,t,s,eta)
        R=1-2*eta*(1+r)+eta*eta*(1+r)/(1-r)
        assert rx==rz==R
        assert (R>1)==(r>1-eta/2)
        checks+=1

# For any chosen anisotropy, increasing the second gradient norm can
# make the first objective arbitrarily worse while the directions stay orthogonal.
for r,eta,M in product([F(1,100),F(1,5),F(1,2),F(4,5)],
                       [F(1,10),F(1,2),F(1)],range(1,35)):
    B=((F(1),-r),(-r,F(1)))
    rx,rz=verify_step(B,F(1),F(M),eta)
    R=1-2*eta*(1+r*M)+eta*eta*(1+r*M)**2/(1-r*r)
    assert rx==R
    checks+=1

# Exact sharp frontier: equal-energy unit gradients, with r=(kappa-1)/(kappa+1).
for k,eta in product([F(1),F(2),F(3),F(4),F(5),F(9),F(19)],
                     [F(1,4),F(1,2),F(3,4),F(1)]):
    r=(k-1)/(k+1)
    B=((F(1),-r),(-r,F(1)))
    rx,rz=verify_step(B,F(1),F(1),eta)
    assert (rx>1)==(k>4/eta-1)
    assert (rx==1)==(k==4/eta-1)
    assert rx==rz
    checks+=1

print('VERIFY_OK',checks,'exact-rational checks')
