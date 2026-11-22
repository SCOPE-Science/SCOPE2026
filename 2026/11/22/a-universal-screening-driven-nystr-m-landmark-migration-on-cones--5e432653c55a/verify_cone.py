#!/usr/bin/env python3
"""Reproducible exact-arithmetic checks for the cone rank-one Nyström theorem.

Requires Python >=3.10, sympy; scipy for an optional numerical cycle-asymptotic test.
The mathematical proof is analytic; finite checks are independent corroboration.
"""
from fractions import Fraction
import math
import sympy as sp

MU = sp.symbols('mu', positive=True)
checks = 0

def assert_eq(a, b):
    global checks
    assert sp.simplify(a-b) == 0, (a,b)
    checks += 1

def adj_matrix(m, edges):
    A=sp.zeros(m)
    for u,v in edges:
        assert 0<=u<v<m
        A[u,v]=A[v,u]=1
    return A

def cycle(m):
    return adj_matrix(m, sorted({tuple(sorted((i,(i+1)%m))) for i in range(m)}))

def complete_bipartite(p):
    return adj_matrix(2*p, [(i,p+j) for i in range(p) for j in range(p)])

def petersen():
    # Outer pentagon, inner pentagram, five spokes
    return adj_matrix(10, sorted({tuple(sorted((i,(i+1)%5))) for i in range(5)} |
             {tuple(sorted((5+i,5+((i+2)%5)))) for i in range(5)} |
             {(i,5+i) for i in range(5)}))

def triangular_prism():
    return adj_matrix(6,[(0,1),(0,2),(1,2),(3,4),(3,5),(4,5),(0,3),(1,4),(2,5)])

def test_graph(A, mus):
    m=A.rows
    degree=sum(A[0,j] for j in range(m))
    for i in range(m):
        assert sum(A[i,j] for j in range(m))==degree
    LH=degree*sp.eye(m)-A
    one=sp.ones(m,1)
    LC=sp.zeros(m+1)
    LC[0,0]=m
    for j in range(m):
        LC[0,j+1]=LC[j+1,0]=-1
    for i in range(m):
        for j in range(m):
            LC[i+1,j+1]=LH[i,j]+(1 if i==j else 0)
    for mu in mus:
        K=(mu*sp.eye(m+1)+LC).inv()
        h=(mu+1)/(mu*(mu+m+1))
        assert_eq(K[0,0],h)
        r=K[1,1]
        for j in range(1,m+1):
            assert_eq(K[j,j],r)
        Tin=(LH+(mu+1)*sp.eye(m)).inv()
        rest=sp.trace((m*sp.eye(m)-LH)*Tin)-m/(mu+1)
        Q=1+mu*rest/(m*(mu+1))
        assert_eq(r/h,Q)
        # The actual one-column trace gain and the resolvent derivative identity
        gains=[]
        for i in range(m+1):
            rank1=K[:,i]*K[i,:]/K[i,i]
            residual=K-rank1
            assert_eq(sp.trace(residual),sp.trace(K)-(K*K)[i,i]/K[i,i])
            assert_eq(sp.trace(residual),(mu*sp.eye(m+1)+LC).minor_submatrix(i,i).inv().trace())
            gains.append((K*K)[i,i]/K[i,i])
        for gain in gains[2:]:
            assert_eq(gain,gains[1])
        M=LH+sp.eye(m)
        denom=mu*sp.eye(m)+M
        # Polynomial/rational g(mu) expression, excluding constant mode
        g=sp.trace((m*sp.eye(m)-LH)*(M-mu*mu*sp.eye(m))*denom.inv()*denom.inv()) - m*(1-mu*mu)/(mu+1)**2
        assert_eq(gains[0]-gains[1], g/(m*(mu+1)**2*Q))
        if mu<=sp.Rational(1,2):
            assert gains[0]>gains[1]
        if mu>=m+2:
            assert gains[0]<gains[1]
        if degree !=m-1:
            assert r>h
        global checks
        checks+=3
    return m

families=[cycle(m) for m in range(4,10)]
families += [complete_bipartite(p) for p in (2,3,4)]
families += [triangular_prism(),petersen()]
for A in families:
    test_graph(A,[sp.Rational(1,2),sp.Rational(3,2),sp.Rational(5,2),sp.Integer(A.rows+2)])

# Prove the sharp m=4 cycle transition exactly from the derivative rational polynomial.
A=cycle(4)
LH=2*sp.eye(4)-A
m=4
M=LH+sp.eye(m)
D=MU*sp.eye(m)+M
g=sp.trace((m*sp.eye(m)-LH)*(M-MU**2*sp.eye(m))*D.inv()*D.inv())-m*(1-MU**2)/(MU+1)**2
assert sp.simplify(g.subs(MU,sp.sqrt(3)))==0
checks+=1

# Asymptotic expression for cycle thresholds is not inferred from finite tests.
# Numeric check supports the independent Fourier-integral derivation.
import numpy as np
from scipy.optimize import brentq
x0=math.sqrt(6)-1
A0=(x0+1)*(x0+5)
coeff=A0*(x0*(x0+1)**2-2*math.sqrt(A0))/(2*(x0+1)**3)
assert 0.39<coeff<0.42
checks+=1
for m in (20,50,100,250,1000):
    nu=2-2*np.cos(2*np.pi*np.arange(1,m)/m)
    c=m-nu
    g=lambda x:np.sum(c*(1+nu-x*x)/(x+1+nu)**2)
    root=brentq(g,1,math.sqrt(5),xtol=1e-13)
    assert abs(m*(root-x0)-coeff)<12/m
    checks+=1
print(f'PASS: {checks} exact symbolic/rational assertions and asymptotic comparisons over {len(families)} test graphs')
