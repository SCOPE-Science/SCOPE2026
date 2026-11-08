#!/usr/bin/env python3
"""Exact four-site contact-process star/path comparison.

Run: python verify.py
Requires Python 3 and SymPy. All expressions are obtained from the
complete, unreduced 15-state transient generator.
"""
from fractions import Fraction
from itertools import combinations
import sympy as sp

x = sp.symbols('x', positive=True)
star = ((0, 1), (0, 2), (0, 3))
path = ((0, 1), (1, 2), (2, 3))


def full_generator(edges, rate):
    Q = sp.zeros(16, 16)
    for state in range(1, 16):
        for v in range(4):
            if state & (1 << v):
                next_state = state ^ (1 << v)
                Q[state, next_state] += 1
                Q[state, state] -= 1
            else:
                boundary = sum(1 for a, b in edges if
                               (a == v and state & (1 << b)) or
                               (b == v and state & (1 << a)))
                if boundary:
                    next_state = state | (1 << v)
                    Q[state, next_state] += rate * boundary
                    Q[state, state] -= rate * boundary
    return Q


def occupancy_average(values, k):
    states = [state for state in range(1, 16)
              if state.bit_count() == k]
    return sum((values[s] for s in states), sp.S(0)) / len(states)


A = full_generator(star, x)
B = full_generator(path, x)
assert all(sp.simplify(sum(A.row(i))) == 0 for i in range(16))
assert all(sp.simplify(sum(B.row(i))) == 0 for i in range(16))
assert A[0, 0] == B[0, 0] == 0
u = sp.Matrix([int(j > 0) for j in range(16)])

# The coefficient of t^m/m! in P(T>t) is the initial mixture's Q^m u.
short_coefficients = {
    1: (3, -x*x/sp.Integer(12)),
    2: (4, x*x/sp.Integer(72)),
    3: (5, -x*x/sp.Integer(120)),
    4: (6, -x*x/sp.Integer(180)),
}
for k, (first, coefficient) in short_coefficients.items():
    for m in range(first):
        diff = occupancy_average((A**m-B**m)*u, k)
        assert sp.factor(diff) == 0, (k,m,diff)
    diff = occupancy_average((A**first-B**first)*u, k)
    assert sp.factor(diff/sp.factorial(first) - coefficient) == 0

# Mean hitting times solve (-Q_transient)t=1. Symbolic rational identities.
tA = (-A[1:16, 1:16]).inv()*sp.ones(15, 1)
tB = (-B[1:16, 1:16]).inv()*sp.ones(15, 1)
meansA = sp.Matrix([0]+list(tA))
meansB = sp.Matrix([0]+list(tB))
D = (3*x+2)*(4*x+3)*(4*x*x+9*x+6)*(12*x**3+31*x*x+32*x+12)
N1 = 96*x**7+656*x**6+1895*x**5+3083*x**4+3131*x**3+2030*x*x+792*x+144
N2 = (648*x**8+5262*x**7+18320*x**6+36564*x**5+46792*x**4
      +40131*x**3+22880*x*x+7980*x+1296)
N3 = (324*x**8+2595*x**7+8941*x**6+17676*x**5+22477*x**4
      +19319*x**3+11195*x*x+4032*x+684)
expected = [x*x*N1/(2*D),x*x*N2/(12*(x+1)*D),
            x*x*N3/(6*(x+1)*D),x*x*N3/(6*(x+1)*D)]
for k in range(1, 5):
    diff = occupancy_average(meansA - meansB, k)
    assert sp.cancel(diff - expected[k-1]) == 0, (k, diff)
    numer,denom=sp.fraction(sp.factor(expected[k-1]))
    assert all(z>=0 for z in sp.Poly(numer,x).all_coeffs()) and any(z>0 for z in sp.Poly(numer,x).all_coeffs())
    assert all(z>0 for z in sp.Poly(denom,x).all_coeffs())

# An independent exact numerical method: Gaussian elimination over Fraction.
def fraction_mean(edges, c):
    Q = full_generator(edges, sp.Rational(c.numerator,c.denominator))
    mat = [[Fraction(int(Q[i,j].p),int(Q[i,j].q)) for j in range(1,16)] for i in range(1,16)]
    rhs=[Fraction(1) for i in range(15)]
    for i in range(15):
        for j in range(15): mat[i][j] = -mat[i][j]
    for i in range(15):
        pivot=next(j for j in range(i,15) if mat[j][i])
        mat[i],mat[pivot]=mat[pivot],mat[i]
        rhs[i],rhs[pivot]=rhs[pivot],rhs[i]
        q=mat[i][i]
        for z in range(i,15):mat[i][z] /= q
        rhs[i] /= q
        for row in range(15):
            if row == i:continue
            mul=mat[row][i]
            if not mul:continue
            for z in range(i,15):mat[row][z] -= mul*mat[i][z]
            rhs[row] -= mul*rhs[i]
    return [Fraction(0)]+rhs

for c in (Fraction(1,4), Fraction(1), Fraction(5,2)):
    F = fraction_mean(star,c)
    G = fraction_mean(path,c)
    for k in range(1,5):
        sts=[s for s in range(1,16) if s.bit_count()==k]
        gap=sum((F[s]-G[s] for s in sts),Fraction(0))/len(sts)
        exact=expected[k-1].subs(x,sp.Rational(c.numerator,c.denominator))
        assert gap == Fraction(int(exact.p),int(exact.q))
        assert gap > 0

print('PASS: 4 all-rate rational mean gaps; 4 exact short-time signs; 12 independent fraction comparisons')
