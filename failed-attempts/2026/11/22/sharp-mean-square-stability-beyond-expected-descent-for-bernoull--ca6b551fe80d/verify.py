#!/usr/bin/env python3
"""Independent checks of the mean-square stability criterion for masked coordinate descent."""
import itertools
import sympy as s

def exact_transfer(n, p, c, h):
    H=(1-c)*s.eye(n)+c*s.ones(n)
    T=s.eye(n)-s.ones(n)/n
    U=s.ones(n)/n
    expected=[]
    for C in (T,U):
        out=s.zeros(n)
        for bits in itertools.product((0,1),repeat=n):
            k=sum(bits)
            prob=p**k*(1-p)**(n-k)
            M=s.eye(n)-h*s.diag(*bits)*H
            out+=prob*M*C*M.T
        expected.append(out.applyfunc(s.factor))
    a=1-c; L=1+(n-1)*c
    A=s.Matrix([
       [1-2*h*p*a+h*h*p*a*a*(n-1+p)/n, h*h*L*L*p*(1-p)/n],
       [h*h*a*a*(n-1)*p*(1-p)/n, (1-h*p*L)**2+h*h*L*L*p*(1-p)/n]
    ])
    for j in range(2):
        predicted=A[0,j]*T + A[1,j]*U
        assert expected[j]==predicted.applyfunc(s.factor),('covariance',n,p,c,h,j)
    return A

def symbolic():
    n,p,c,h=s.symbols('n p c h',positive=True)
    a=1-c; L=1+(n-1)*c; K=a*L; S=1+p+p*(n-2)*c
    A=s.Matrix([
      [1-2*h*p*a+h*h*p*a*a*(n-1+p)/n, h*h*L*L*p*(1-p)/n],
      [h*h*a*a*(n-1)*p*(1-p)/n, (1-h*p*L)**2+h*h*L*L*p*(1-p)/n]
    ])
    F=4-2*S*h+p*K*h*h
    assert s.factor((s.eye(2)-A).det()-p*p*h*h*K*F)==0
    assert s.factor(F.subs(h,2)+4*p*(n-1)*c*c)==0
    W=1+p*(n-1)*c
    assert s.factor(F.subs(h,2/W)-4*(n-1)*c*(1-c)*p*(1-p)/W**2)==0
    assert s.factor(s.diff(F,p)-h*(-2*(1+(n-2)*c)+h*K))==0
    assert s.factor(s.diff(F,c)-p*h*((n-2)*(h-2)-2*h*(n-1)*c))==0
    assert s.factor(s.diff(F,n)-p*h*c*(h*(1-c)-2))==0
    print('symbolic identities PASS (determinant, boundary, strict-gap, three monotonic derivatives)')

def numeric():
    from math import sqrt
    checks=0
    for n in [2,3,4,8,15,100]:
      for p in [0.01,0.12,0.5,0.93,0.999]:
        for c in [0.001,0.2,0.6,0.95]:
          a=1-c; L=1+(n-1)*c; K=a*L; S=1+p+p*(n-2)*c
          root=4/(S+sqrt(S*S-4*p*K))
          W=1+p*(n-1)*c
          assert 2/W < root < 2
          for h,stable in [(root*0.9,True),(root*1.1,False),(2.2,False)]:
            AA=1-2*h*p*a+h*h*p*a*a*(n-1+p)/n
            BB=h*h*L*L*p*(1-p)/n
            CC=h*h*a*a*(n-1)*p*(1-p)/n
            DD=(1-h*p*L)**2+h*h*L*L*p*(1-p)/n
            rho=(AA+DD+sqrt((AA-DD)**2+4*BB*CC))/2
            assert (rho<1)==stable, (n,p,c,h,rho)
            checks+=1
    print('numeric stability-side comparisons PASS',checks)

def enumeration():
    cases=0
    for n in (2,3,4,5):
      for p in (s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)):
        for c in (s.Rational(1,5),s.Rational(1,2),s.Rational(4,5)):
          for h in (s.Rational(1,3),s.Rational(7,5)):
            exact_transfer(n,p,c,h)
            cases+=1
    print('complete-mask covariance enumerations PASS',cases,'cases')

if __name__=='__main__':
    symbolic()
    enumeration()
    numeric()
    print('PASS: all tests')
