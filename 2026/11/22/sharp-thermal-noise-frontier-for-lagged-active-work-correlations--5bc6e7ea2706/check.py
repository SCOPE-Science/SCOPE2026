#!/usr/bin/env python3
"""Exact-rational and deterministic checks for the active-work lag-covariance law.
Standard Python 3 only. Running: python3 check.py
"""
from fractions import Fraction as F
from math import exp, log, isclose

N = 0

def assert_eq(left, right):
    global N
    N += 1
    assert left == right, (left, right)


def assert_approx(left, right, tol=2e-11):
    global N
    N += 1
    assert isclose(left, right, rel_tol=tol, abs_tol=tol), (left, right)


def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def tr(A):
    return A[0][0]+A[1][1]


def transpose(A):
    return [list(row) for row in zip(*A)]


def independent_gaussian_cov(k, D, A, E):
    """Compute quadratic-current covariance by explicit pair contractions."""
    S = [[D/k+A/(k*(k+1)), A/(k+1)], [A/(k+1), A]]
    Q = [[F(0), -k/2],[-k/2, F(1)]]
    c = mm(S,transpose(E))
    out = F(0)
    for i in range(2):
        for j in range(2):
            for h in range(2):
                for l in range(2):
                    out += Q[i][j]*Q[h][l]*(c[i][h]*c[j][l]+c[i][l]*c[j][h])
    return out


def K_closed(k,D,A,t):
    if abs(k-1)<1e-13:
        return A*A*exp(-2*t)*(0.75-t-D/A)
    return (A*A*(k*(k+3)*exp(-(k+1)*t)
                  -2*(k+1)*exp(-2*t))/((k-1)*(k+1)**2)
            -D*k*A*exp(-(k+1)*t))


def critical(k):
    return (k+2)/(k*(k+1)**2)


def zero(k,d):
    if abs(k-1)<1e-13:
        return 0.75-d
    h = k*(k+3)/(2*(k+1))-d*k*(k-1)*(k+1)/2
    return log(h)/(k-1)

# The exponential semigroup has two independent monomials x=e^{-k t}, y=e^{-t}.
# Substitute arbitrary rational x,y to check the resulting polynomial identity exactly.
for k in [F(1,4),F(1,2),F(2,3),F(3,2),F(2),F(5),F(11,3)]:
    for D in [F(0),F(1,5),F(3,2),F(7)]:
        for A in [F(1,3),F(1),F(5,2)]:
            for x,y in [(F(1,2),F(2,3)),(F(3,5),F(4,7)),(F(1,9),F(7,8)),(F(3,11),F(2,7))]:
                E = [[x, (y-x)/(k-1)], [F(0),y]]
                direct=independent_gaussian_cov(k,D,A,E)-2*D*k*A*x*y
                rhs=(A*A*(k*(k+3)*x*y-2*(k+1)*y*y)/((k-1)*(k+1)**2)-D*k*A*x*y)
                assert_eq(direct, rhs)
# Resonant semigroup E_{12}=t exp(-t) must match the finite k=1 limit.
for D in [F(0),F(1,5),F(3,4),F(3,2),F(7)]:
    for A in [F(1,3),F(1),F(4)]:
        for t in [F(0),F(1,10),F(2,5),F(3,4),F(2),F(7)]:
            for y in [F(1,3),F(2,5)]:
                E = [[y,t*y],[F(0),y]]
                direct=independent_gaussian_cov(F(1),D,A,E)-2*D*A*y*y
                rhs=A*A*y*y*(F(3,4)-t-D/A)
                assert_eq(direct,rhs)

# Long-time exact covariance rate and stationary short-lag expression.
for k in [F(1,6),F(1,2),F(3,4),F(5,4),F(2),F(4)]:
    for D in [F(0),F(1,9),F(4)]:
        for A in [F(1,4),F(1),F(6)]:
            K0 = A*A*(k+2)/(k+1)**2-D*k*A
            K0_from_formula= A*A*(k*(k+3)-2*(k+1))/((k-1)*(k+1)**2)-D*k*A
            assert_eq(K0,K0_from_formula)
            integ=(A*A*k*(k+3)/((k-1)*(k+1)**3)
                   -A*A/((k-1)*(k+1))-D*k*A/(k+1))
            assert_eq(2*D*A+2*integ,2*D*A/(k+1)+2*A*A/(k+1)**3)

# All-parameter signs: exactly one positive zero below the threshold,
# no positive zero above, with the resonant k=1 case included.
for k in [0.1,0.3,0.75,1,1.1,2,3,7,15]:
    c=critical(k)
    for fraction in [0,0.15,0.5,0.9,0.99]:
        d=fraction*c
        tstar=zero(k,d)
        assert_eq(tstar>0, True)
        assert_approx(K_closed(k,d,1,tstar),0,tol=5e-12)
        assert_eq(K_closed(k,d,1,tstar*0.2)>0,True)
        assert_eq(K_closed(k,d,1,tstar*2)<0,True)
        assert_eq(K_closed(k,d,1,tstar+2)<0,True)
    for fraction in [1,1.05,2,8]:
        d=fraction*c
        for t in [0.0001,0.05,0.3,1,5]:
            assert_eq(K_closed(k,d,1,t)<0,True)

# Monotonic thermal crossover shift, plus exact k=1 sample.
for k in [0.13,0.5,1.0,1.8,4,12]:
    c=critical(k)
    a,b=zero(k,0.1*c),zero(k,0.5*c)
    assert_eq(a>b>0,True)
assert_approx(critical(1),0.75)
assert_approx(zero(1,0.25),0.5)
assert_approx(K_closed(1,1,1,0.25),exp(-0.5)*(-0.5))
assert_approx(K_closed(1,0.25,1,0.25),exp(-0.5)*0.25)
print(f'PASS: {N} exact-rational or deterministic positive-lag assertions')
