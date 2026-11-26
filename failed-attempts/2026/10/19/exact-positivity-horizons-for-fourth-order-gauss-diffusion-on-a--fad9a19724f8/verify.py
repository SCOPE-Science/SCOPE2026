"""Exact arithmetic checks for Gauss-Pade positivity on a one-defect weighted star.

Run: python verify.py    Requires SymPy 1.12 or newer.
This program verifies algebraic identities and finite samples; the written proof
establishes the parameter-uniform sign analysis.
"""
from fractions import Fraction
import sympy as sp

k, x, h = sp.symbols('k x h', positive=True)
a = k + 1 + 2*x
b = (k+2)*x
Delta = 144 + 72*a*h + 12*(a*a+b)*h*h + 6*a*b*h**3 + b*b*h**4
p = 12 + 6*x*h + x*(2*x-1)*h*h
r = 12 + 6*h + (k+1-k*x)*h*h
q = (72+(12*k+48*x+24)*h+(6*k*x+12*x*x+12*x)*h*h
     + x*((k+4)*x-1)*h**3)
M = sp.Matrix([[k+x,-k,-x],[-1,1,0],[-x,0,x]])
D = 12*sp.eye(3)+6*h*M+h*h*M*M
U = 12*sp.eye(3)-6*h*M+h*h*M*M
T = U*D.inv()
assert sp.factor(D.det()-12*Delta)==0
assert sp.cancel(T[0,1]/k - 12*h*p/Delta)==0
assert sp.cancel(T[0,2] - 12*h*x*r/Delta)==0
assert sp.cancel(T[1,2] - 12*h*h*x*(6+a*h)/Delta)==0
f1=(12-6*h+h*h)/(12+6*h+h*h)
assert sp.cancel((T[1,1]-f1)/k - 12*h*h*q/((h*h+6*h+12)*Delta))==0
# The crucial remainder is positive at the first center/ordinary zero
# for 0<x<1/2. It excludes earlier ordinary/ordinary negativity.
expected_rem = 12*(1-x)*((k*(1+x)+1+6*x-4*x*x)*h+6*k+12)/(1-2*x)**2
assert sp.cancel(sp.rem(q,p,h)-expected_rem)==0
checks=6

def direct(n, xx, hh):
    global checks
    L=sp.zeros(n)
    for i in range(1,n):
        w=xx if i==n-1 else sp.Integer(1)
        L[0,0]+=w; L[i,i]+=w; L[0,i]-=w; L[i,0]-=w
    A=12*sp.eye(n)+6*hh*L+hh*hh*L*L
    B=12*sp.eye(n)-6*hh*L+hh*hh*L*L
    C=A.inv()*B
    kval=sp.Integer(n-2)
    sub={k:kval,x:xx,h:hh}
    entries={(0,1):12*h*p/Delta,(0,n-1):12*h*x*r/Delta,
             (1,n-1):12*h*h*x*(6+a*h)/Delta,
             (1,2):12*h*h*q/((h*h+6*h+12)*Delta)}
    for (i,j), expression in entries.items():
        assert C[i,j] == sp.factor(expression.subs(sub)), (n,xx,hh,i,j)
        checks+=1
    for i in range(n):
        assert sum(C[i,j] for j in range(n))==1
        assert C[i,i]>0
        checks+=2
    # Exact orbit invariance, not a floating-point tolerance.
    for i in range(n):
        for j in range(i+1,n):
            if i and j!=n-1: target=C[1,2]
            elif i==0 and j!=n-1: target=C[0,1]
            elif i==0:target=C[0,n-1]
            else:target=C[1,n-1]
            assert C[i,j]==target
            checks+=1

for n in (4,5,6,7,8):
    for xx in map(sp.Rational, ['1/4','1/2','3/4','1','5/4','2']):
        for hh in map(sp.Rational, ['1/3','2','12']):
            direct(n,xx,hh)
print('VERIFY_OK',checks,'exact symbolic, quotient, direct-matrix and orbit identities')
