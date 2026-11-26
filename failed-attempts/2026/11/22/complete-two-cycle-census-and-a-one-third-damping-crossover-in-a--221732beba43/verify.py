#!/usr/bin/env python3
"""Reproduce the algebra and exact orbit checks for an axially symmetric map.

Requires Python 3 and SymPy. All algebraic checks are exact (no floats).
"""
from fractions import Fraction as F
import sympy as S

n, r, alpha, q, b = S.symbols('n r alpha q b', nonzero=True)
A = 1-n
J0 = S.Matrix([[0,1,0], [n,A*q,b], [0,2*alpha*b,r]])
J1 = S.Matrix([[0,1,0], [n,A/q,q*b], [0,2*alpha*q*b,r]])
D = S.factor((J1*J0-S.eye(3)).det())
assert S.factor(D-2*alpha*b*b*(A*r*q**4+2*A*q**2+A*r-2*alpha*b*b*q**3)/q)==0
assert S.simplify(D.subs(b*b,A*(1+r)/(alpha*q))-
                  2*r*A*A*(1+r)*(q*q-1)**2/q**2)==0
print('Exact symbolic Floquet identity: PASS')

def map_F(p,n,m,r,alpha):
    x,y,z=p
    return (y,n*x+m*y+y*z,r*z+alpha*y*y)

def jac_F(p,n,m,r,alpha):
    x,y,z=p
    return [[F(0),F(1),F(0)], [n,m+z,y], [F(0),2*alpha*y,r]]

def product(M,N):
    return [[sum(M[i][k]*N[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def determinant(M):
    a,b,c=M[0]; d,e,f=M[1]; g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def exact_example(n,r,alpha,a,b):
    assert 0<n<1 and 0<r<1 and a*a!=b*b
    A=1-n
    assert a*b == A*(1+r)/alpha
    m=-alpha*r*(a*a+b*b)/(1-r*r)
    z0=alpha*(a*a+r*b*b)/(1-r*r)
    z1=alpha*(b*b+r*a*a)/(1-r*r)
    p=(a,b,z0); v=(b,a,z1)
    assert map_F(p,n,m,r,alpha)==v
    assert map_F(v,n,m,r,alpha)==p
    flip=lambda p:(-p[0],-p[1],p[2])
    assert map_F(flip(p),n,m,r,alpha)==flip(v)
    assert map_F(flip(v),n,m,r,alpha)==flip(p)
    Q=product(jac_F(v,n,m,r,alpha),jac_F(p,n,m,r,alpha))
    delta=determinant([[Q[i][j]-F(int(i==j)) for j in range(3)]for i in range(3)])
    assert delta==2*r*(a*a-b*b)**2/(1+r)>0
    Ssq=a*a+b*b; P=a*b
    assert Ssq>2*abs(P)
    assert alpha*m < -2*r*A/(1-r)
    return m,delta

# Several exact rational points for both signs and different damping values.
count=0
for r in [F(1,5),F(1,3),F(1,2),F(3,5)]:
    for alpha in [F(1),F(-1)]:
        for q in [F(2)/alpha,F(1,2)/alpha]:
            # Choose b rational, then enforce n via the product constraint.
            bval=F(1,2) if abs(q)==2 else F(1)
            nval=1-alpha*q*bval*bval/(1+r)
            if not F(0)<nval<F(1):
                continue
            mval,delta=exact_example(nval,r,alpha,q*bval,bval)
            count+=1
            print(f'Exact orbit {count}: n={nval}, r={r}, alpha={alpha}, m={mval}, det(P-I)={delta}')
assert count>=8

# Elementary exact phase ordering, including the 1/3 crossover.
for r in [F(1,6),F(1,4),F(1,3),F(1,2),F(3,4)]:
    A=F(3,4)
    threshold=-2*r*A/(1-r)
    if r<F(1,3): assert threshold > -A
    elif r==F(1,3): assert threshold == -A
    else: assert threshold < -A
print('Parameter order and boundary tests: PASS')
