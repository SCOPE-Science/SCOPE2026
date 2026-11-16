#!/usr/bin/env python3
"""Exact full monomial Gram determinant versus the six-sector slab theorem."""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import factorial
from sympy import Rational, Matrix, Symbol, factor, simplify

D=3
A=F(1,2)

def rising_half(k):
    r=F(1)
    for j in range(k): r*=F(2*j+1,2)
    return r

def rising_integer(b,k):
    r=F(1)
    for j in range(k): r*=b+j
    return r

def moment(exp, a):
    if any(j%2 for j in exp):return F(0)
    k=[j//2 for j in exp]
    k0=k[0]; other=sum(k[1:])
    # For D=3: X1 marginal is 3/4*(1-z^2) on [-1,1],
    # and conditional (X2,X3) is a uniform disk.
    c=F(3,2)*rising_half(k[1])*rising_half(k[2])/rising_integer(2,other)
    out=F(0)
    for j in range(other+2):
        out+=F((-1)**j*__import__('math').comb(other+1,j),2*k0+2*j+1)*a**(2*k0+2*j+1)
    return c*out

exps=[(0,0,0)]
for degree in (1,2):
  for inds in combinations_with_replacement(range(D),degree):
    e=[0]*D
    for i in inds:e[i]+=1
    exps.append(tuple(e))
assert len(exps)==10
G=Matrix([[Rational(moment(tuple(x+y for x,y in zip(e,f)),F(1))) for f in exps] for e in exps])
H=Matrix([[Rational(moment(tuple(x+y for x,y in zip(e,f)),A)) for f in exps] for e in exps])
assert G.det()!=0
L=Symbol('L')
poly=factor((H-L*G).det()/G.det())
# Compute sector eigenvalues directly from the one-dimensional Jacobi marginal.
def bmoment(j, a):
    return moment((2*j,0,0),a)
m1=bmoment(1,F(1));m2=bmoment(2,F(1))
M0=bmoment(0,A);M1=bmoment(1,A);M2=bmoment(2,A)
S=Matrix([[1,Rational(m1)],[Rational(m1),Rational(m2)]])
C=Matrix([[Rational(M0),Rational(M1)],[Rational(M1),Rational(M2)]])
even=factor((C-L*S).det()/S.det())
def scalar(exp):return Rational(moment(exp,A))/Rational(moment(exp,F(1)))
ax=scalar((2,0,0))
mix=scalar((2,2,0))
tr=scalar((0,2,0))
quad=scalar((0,2,2))
pred=factor(even*(L-ax)*(L-mix)**2*(L-tr)**2*(L-quad)**3)
assert simplify(poly-pred)==0,(poly,pred)
# Exact strict ordering: quadratic eigenvalue roots via discriminant and rational comparisons.
lo,hi=sorted([float(x) for x in __import__('numpy').roots([float(z) for z in __import__('sympy').Poly(even,L).all_coeffs()])])
assert lo<float(ax)<float(mix)<float(tr)<float(quad)<hi
print('PASS: complete 10 x 10 exact rational monomial determinant equals predicted six-sector factorization, d=3, a=1/2')
print('Exact eigenvalue data:',{'ax':str(ax),'mixed':str(mix),'transverse_linear':str(tr),'transverse_quadratic':str(quad),'even_polynomial':str(even)})
