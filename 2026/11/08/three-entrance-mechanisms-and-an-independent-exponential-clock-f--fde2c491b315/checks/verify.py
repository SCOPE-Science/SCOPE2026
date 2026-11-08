#!/usr/bin/env python3
"""Exact finite-horizon identities and limiting-regime checks for a dyadic random interval map."""
from fractions import Fraction as F
from math import isclose

checks=0

def assert_eq(x,y):
    global checks
    assert x==y,(x,y)
    checks+=1

def assert_close(x,y,tol):
    global checks
    assert abs(float(x)-float(y))<=tol,(x,y,tol)
    checks+=1

def h_and_marks(p,m):
    q=1-p; t=p/q
    # C denotes immediate contraction and E,k immediate expanding reset to shell k.
    w={('C',1):q*(t-1)/(t**m-1)}
    for k in range(1,m): w[('E',k)]=p*F(1,2**(k+1))*(t**k-1)/(t**m-1)
    for k in range(m,m+40): w[('E',k)]=p*F(1,2**(k+1))
    # The omitted geometric tail from k=m+40 onward.
    tail=p*F(1,2**(m+40))
    return w,tail

def exact(p,m):
    q=1-p;t=p/q
    return q*(t-1)/(t**m-1)+p*sum((F(1,2**(k+1))*(t**k-1)/(t**m-1) for k in range(1,m)),F())+p*F(1,2**m)

for p in (F(3,5),F(2,3),F(3,4),F(4,5)):
 for m in range(2,22):
    q=1-p;t=p/q
    h=exact(p,m)
    w,tail=h_and_marks(p,m)
    assert_eq(sum(w.values(),F())+tail,h)
    assert_eq(h>0,True)
    # Gambler-ruin finite-difference formula at k<m.
    for k in range(1,m):
        H=lambda j:(t**j-1)/(t**m-1)
        assert_eq(H(k),q*(H(k+1) if k+1<m else 1)+p*(H(k-1) if k>1 else 0))
    # Strict success probability equals renewal hitting probability via mean hitting time:
    # E0[T_m] = E[L_m]/h_m, where E[L_m] is one stopped excursion.
    # Exact finite-state linear equations for E[T_m] from j=0..m-1 are checked below for small m.
    if m<=8:
        import sympy as S
        mat=[];rhs=[]
        for j in range(m):
            row=[S.Rational(int(i==j)) for i in range(m)]
            if j==0:
                row[1]-=S.Rational(q.numerator,q.denominator)
                for k in range(m):row[k]-=S.Rational(p.numerator,p.denominator)*S.Rational(1,2**(k+1))
            else:
                if j+1<m:row[j+1]-=S.Rational(q.numerator,q.denominator)
                row[j-1]-=S.Rational(p.numerator,p.denominator)
            mat.append(row);rhs.append(S.Integer(1))
        ans=S.Matrix(mat).inv()*S.Matrix(rhs)
        assert_eq(ans[0]>0,True)
        # Hitting-time/rare-excursion exact renewal ratio requires first-step truncation to m;
        # compute expected stopped cycle L_m using nearest-neighbor time-to-{0,m}.
        ell=[F(0)]+[F(0)]*(m-1)+[F(0)]
        # Sympy expectations solve e_j=1+q e_{j+1}+p e_{j-1}, boundaries e0=em=0.
        mm=[];rr=[]
        for j in range(1,m):
            row=[S.Rational(int(k==j)) for k in range(1,m)]
            if j+1<m:row[j]-=S.Rational(q.numerator,q.denominator)
            if j>1:row[j-2]-=S.Rational(p.numerator,p.denominator)
            mm.append(row);rr.append(S.Integer(1))
        out=S.Matrix(mm).inv()*S.Matrix(rr)
        ev={k:out[k-1] for k in range(1,m)}
        L=S.Integer(1)+S.Rational(q.numerator,q.denominator)*ev[1]
        for k in range(1,m): L+=S.Rational(p.numerator,p.denominator)*S.Rational(1,2**(k+1))*ev[k]
        assert_eq(F(ans[0]),F(L)/h)

# Exact asymptotic profiles at m=200, by rational arithmetic converted to floats only for comparing profiles.
m=200
p=F(3,5);q=1-p;t=p/q;C=(t-1)*(q+p/(2-t));h=exact(p,m)
assert_close(h*t**m/C,1,1e-10)
for k in (1,2,3,5,10):
    target=p*F(1,2**(k+1))*(t**k-1)/C
    mark=p*F(1,2**(k+1))*(t**k-1)/(t**m-1)/h
    assert_close(mark,target,1e-9)
assert_close(q*(t-1)/(t**m-1)/h,q*(t-1)/C,1e-9)

p=F(2,3);h=exact(p,m)
assert_close(h/(F(m,3)*F(1,2**m)),1,0.03)
for a,b in ((0.1,0.3),(0.2,0.6),(0.55,0.9)):
    numer=sum((p*F(1,2**(k+1))*(2**k-1)/(2**m-1) for k in range(1,m) if a<=k/m<=b),F())
    assert_close(numer/h,b-a,0.025)

p=F(3,4);q=1-p;t=p/q;h=exact(p,m);D=p*(t-1)/(t-2)
assert_close(h/(D*F(1,2**m)),1,1e-10)
A=(t-2)/(2*(t-1))
for d in (0,1,2,3,5):
    assert_close(p*F(1,2**(m+d+1))/h,A*F(1,2**d),1e-10)
for j in (1,2,3,5):
    assert_close(p*F(1,2**(m-j+1))*(t**(m-j)-1)/(t**m-1)/h,A*(F(2,1)/t)**j,1e-10)
assert_eq(2*A+A*(F(2,1)/t)/(1-F(2,1)/t),1)
print('PASS',checks,'exact algebra checks and controlled asymptotic comparisons')
