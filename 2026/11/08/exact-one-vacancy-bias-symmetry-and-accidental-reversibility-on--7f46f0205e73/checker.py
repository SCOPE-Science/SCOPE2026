#!/usr/bin/env python3
"""Independent exact finite-state checks of single-vacancy ring-current identities.
Requires Python 3 and SymPy. All comparisons are exact rational/symbolic.
The universal assertions are proved in RESULT.md, not by these finite tests.
"""
from fractions import Fraction
from itertools import product
from sympy import Matrix, Rational, symbols, factor, prod, simplify, cancel

checks = 0

def check(cond, detail):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(detail)

def formula(A, p):
    L = len(A)
    q = 1-p
    h = [sum(A[i]/(A[(i+k)%L]*A[(i+k+1)%L]) for i in range(L)) for k in range(L)]
    H = sum(h[k]*p**k*q**(L-1-k) for k in range(L))
    return (p**L-q**L)/H, h

def markov_current(A,p):
    """Independently solve N=L-1 exclusion generator and mean bond current."""
    L = len(A)
    q = 1-p
    states = [tuple(1 if i != hole else 0 for i in range(L)) for hole in range(L)]
    Q = Matrix.zeros(L,L)
    r = Matrix.zeros(L,1)
    for idx, state in enumerate(states):
        for site in range(L):
            for step in (-1,1):
                neighbor = (site + step)%L
                if state[site] and not state[neighbor]:
                    after = list(state)
                    after[site] = 0
                    after[neighbor] = 1
                    rate = A[site]*(p if step == 1 else q)
                    Q[idx,states.index(tuple(after))] += rate
                    r[idx] += rate*(1 if step==1 else -1)/L
        Q[idx,idx] = -sum(Q[idx,j] for j in range(L) if j!=idx)
    M = Q.T
    M[L-1,:] = Matrix([[1]*L])
    y = Matrix([0]*(L-1)+[1])
    return cancel((M.inv()*y).dot(r))

# Exact stationary reduction over multiple nonequal rates, sizes, and biases.
rate_lists = [
    (1,2,3), (2,5,7), (1,3,6),
    (1,2,3,4), (1,2,4,3), (1,2,4,8), (2,3,5,7),
    (1,2,3,4,5), (2,3,5,7,11),
    (1,2,3,4,5,6), (1,2,3,4,5,6,7)
]
for rates in rate_lists:
    A = tuple(Rational(a) for a in rates)
    for p in (Rational(1,7), Rational(1,4), Rational(2,5), Rational(1,2), Rational(3,5), Rational(5,6)):
        f, h = formula(A,p)
        direct = markov_current(A,p)
        check(f==direct,(rates,p,'stationary flux'))
        check(h[0]==h[-1],(rates,'endpoint coefficients'))
        check((f==0) == (p==Rational(1,2)),(rates,p,'sign'))

# The complete four-site factor identity.
a0,a1,a2,a3 = symbols('a0 a1 a2 a3', positive=True)
a = (a0,a1,a2,a3)
h1 = sum(a[i]/(a[(i+1)%4]*a[(i+2)%4]) for i in range(4))
h2 = sum(a[i]/(a[(i+2)%4]*a[(i+3)%4]) for i in range(4))
Delta = (a0-a2)*(a1-a3)*(a0+a2-a1-a3)/prod(a)
check(factor(h2-h1-Delta)==0,'four-ring factorization')

x = symbols('x')
p = (1+x)/2
for rates, expected in [
    ((1,2,3,4), 12*x*(1+x**2)/(x**3+20*x**2-x+30)),
    ((1,2,4,3), 48*x*(1+x**2)/(25*(3*x**2+5)))
]:
    A=tuple(Rational(t) for t in rates)
    f,h=formula(A,p)
    check(cancel(f-expected)==0,('closed witness',rates))
    check(cancel(f+f.subs(x,-x) - (0 if rates==(1,2,4,3) else
        24*x**2*(1+x**2)*(1-x**2)/((30+20*x**2)**2-x**2*(1-x**2)**2))) == 0,
        ('even witness',rates))

# Exact zero and sign tests for the generic four-site class and the
# nonsymmetric cancellation family across multiple rational bias values.
for rates in ((1,2,3,4),(1,2,4,3),(1,3,5,7),(1,2,4,8),(3,5,6,8)):
    A=tuple(Rational(t) for t in rates)
    delta=Delta.subs(dict(zip(a,A)))
    for e in (Rational(1,9),Rational(1,3),Rational(2,3),Rational(9,10)):
        f,_=formula(A,(1+e)/2)
        g,_=formula(A,(1-e)/2)
        check((f+g==0)==(delta==0),(rates,e,'exact oddness criterion'))
        if delta:
            check((f+g)*delta<0,(rates,e,'even-response sign'))

print('PASS:',checks,'exact symbolic/rational assertions')
