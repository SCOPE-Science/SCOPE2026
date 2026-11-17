#!/usr/bin/env python3
"""Exact symbolic identities and independently evaluated finite examples for triangular switching."""
import itertools
import sympy as s

a=s.symbols('a',real=True)
I=s.eye(3)
E=((0,1),(1,2),(0,2))

def kernel(edge):
    i,j=edge
    P=s.eye(3)
    P[i,i]=P[j,j]=0
    P[i,j]=P[j,i]=1
    return a*I+(1-a)*P

K=[kernel(e) for e in E]
M=s.simplify(K[2]*K[1]*K[0])
t=s.factor(s.trace(M)-1)
d=s.factor(M.det())
D=s.factor(t*t-4*d)
assert t==-a*(a*a-6*a+3)
assert d==(2*a-1)**3
assert D==(a-1)**4*(a*a-8*a+4)
assert all(s.simplify(v)==0 for v in M*s.ones(3,1)-s.ones(3,1))
assert all(s.simplify(v)==0 for v in (s.ones(1,3)*M-s.ones(1,3)))
assert s.simplify(M[0,1]-M[1,0])==a*(a-1)**2

threshold=4-2*s.sqrt(3)
lam=15*s.sqrt(3)-26
Mstar=s.simplify(M.subs(a,threshold))
J=s.ones(3,3)/3
N=s.simplify((Mstar-lam*s.eye(3))*(s.eye(3)-J))
assert N!=s.zeros(3)
assert N.applyfunc(s.simplify).equals(N)
assert (N*N).applyfunc(s.simplify)==s.zeros(3)
for k in range(1,5):
    assert (Mstar**k*(s.eye(3)-J) - lam**k*(s.eye(3)-J) - k*lam**(k-1)*N).applyfunc(s.simplify)==s.zeros(3)
for perm in itertools.permutations(E):
    X=s.eye(3)
    for edge in perm:
        X=kernel(edge)*X
    assert s.factor(s.trace(X)-1)==t
    assert s.factor(X.det())==d

# Direct original nonlinear four-species QSO versus the normalized stochastic product.
for q in (s.Rational(1,5),s.Rational(1,2),s.Rational(7,10)):
    y=s.Matrix([s.Rational(1,9),s.Rational(1,6),s.Rational(1,8)])
    w=1-sum(y)
    p=y/(1-w)
    z=2*w-1
    for r in range(7):
        if r:
            edge=E[(r-1)%3]
            Kq=kernel(edge).subs(a,q)
            y_new=2*w*Kq*y
            w_new=w*w+(1-w)**2
            p=Kq*p
            z=z*z
            assert y_new==s.simplify((1-w_new)*p)
            assert s.simplify(w_new-(1+z)/2)==0
            y,w=y_new,w_new
        assert s.simplify(sum(y)+w-1)==0

# Two-season contrast (distinct transpositions) is explicitly prior work, comparison only.
M2=K[1]*K[0]
t2=s.factor(s.trace(M2)-1)
assert s.factor(t2*t2-4*M2.det())==(a-1)**2*(a*a+6*a-3)
assert s.simplify((2*s.sqrt(3)-3)+(4-2*s.sqrt(3)))==1
print('TRIANGULAR_SWITCHING_SYMBOLIC_OK all_calendars=6 Jordan_powers=4 nonlinear_trajectories=21')
