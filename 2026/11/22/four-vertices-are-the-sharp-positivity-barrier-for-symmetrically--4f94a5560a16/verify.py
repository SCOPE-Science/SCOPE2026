#!/usr/bin/env python3
"""Exact symbolic regression checks for the resolvent-sandwich graph step.
Requires Python 3 and SymPy. The analytic proof is in RESULT.md.
"""
import sympy as s
z=s.symbols('z',positive=True)

def lap(n,triangle=False):
    W=s.zeros(n)
    for i in range(n-1):
        W[i,i+1]=W[i+1,i]=1
    if triangle: W[0,2]=W[2,0]=1
    return s.diag(*[sum(W[i,j] for j in range(n)) for i in range(n)])-W

def hz(L):
    B=(s.eye(L.rows)+z*L).inv()
    return (z*B*L*B).applyfunc(s.factor)

nchecks=0
def check(x):
    global nchecks
    assert bool(x)
    nchecks+=1

a=hz(lap(2));check(s.factor(a[0,1]+z/(1+2*z)**2)==0)
a=hz(lap(3))
check(s.factor(a[0,1]+z/(1+3*z)**2)==0)
check(s.factor(a[0,2]+2*z**2*(2*z+1)/((z+1)**2*(3*z+1)**2))==0)
a=hz(lap(3,True));check(s.factor(a[0,1]+z/(1+3*z)**2)==0)
a=hz(lap(4))
D=(2*z+1)**2*(2*z**2+4*z+1)**2
forms={
(0,1):z*(z+1)*(2*z**3-6*z**2-5*z-1)/D,
(0,2):-z**2*(6*z**3+12*z**2+9*z+2)/D,
(0,3):-z**3*(10*z**2+12*z+3)/D,
(1,2):-z*(z+1)*(2*z**3+2*z**2+3*z+1)/D,
}
for (i,j),f in forms.items():check(s.factor(a[i,j]-f)==0)
for val in [s.Rational(1,4),s.Rational(1),s.Rational(3),s.Rational(4),s.Rational(10),s.Rational(100)]:
    b=a.subs(z,val)
    check(b==b.T)
    check(all(s.factor(sum(b[i,j] for j in range(4)))==0 for i in range(4)))
    check((b[0,1]>0)==(val>=4))
    check(all(b[i,j]<0 for i,j in [(0,2),(0,3),(1,2),(1,3)]))
    check(all(0 <=b[i,i] <=s.Rational(1,4) for i in range(4)))
for x in [s.Rational(1,4),s.Rational(1),s.Rational(3),s.Rational(4),s.Rational(10)]:
    check((2*x**3-6*x**2-5*x-1>0)==(x>=4))
print('VERIFY_OK',nchecks)
