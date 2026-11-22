"""Standalone checks for weighted theta-graph tree-preconditioning formulas.
Run: python verify_theta.py
Requires numpy, scipy, sympy.
"""
import itertools
import math
import numpy as np
import sympy as sp
from scipy.linalg import eigh


def theta_edges(lengths, weights):
    # Paths share terminal 0 and terminal 1; internal labels unique.
    edges = []
    n = 2
    for arm, (length, weight) in enumerate(zip(lengths, weights)):
        vertices = [0] + list(range(n, n + length - 1)) + [1]
        n += length - 1
        for position in range(length):
            edges.append((vertices[position], vertices[position + 1], float(weight), arm, position))
    return n, edges


def laplacian(n, edges):
    out = np.zeros((n, n))
    for u, v, w, _, _ in edges:
        out[u,u] += w
        out[v,v] += w
        out[u,v] -= w
        out[v,u] -= w
    return out


def prediction(lengths, weights, retained):
    i,j = [a for a in range(3) if a != retained]
    R = lengths[retained]/weights[retained]
    Di = lengths[i] - 1 + weights[i]*R
    Dj = lengths[j] - 1 + weights[j]*R
    H = math.sqrt(weights[i]*weights[j])*R
    disc = math.sqrt((Di-Dj)**2 + 4*H*H)
    return [1.0]*(sum(lengths)-4)+[1+(Di+Dj-disc)/2,1+(Di+Dj+disc)/2], Di+Dj


def check_numerical():
    tests = 0
    for lengths,weights in [
        ((2,2,2),(1,2,3)), ((2,2,3),(6,6,7)),
        ((2,3,4),(2,7,5)), ((3,3,3),(4,1,3)),
        ((2,2,5),(3,3,4)), ((3,4,5),(3,5,8)),
    ]:
        n,edges = theta_edges(lengths,weights)
        Lg = laplacian(n,edges)
        for retained in range(3):
            i,j = [a for a in range(3) if a!=retained]
            for pi in range(lengths[i]):
                for pj in range(lengths[j]):
                    Lt = laplacian(n,[e for e in edges if not (e[3]==i and e[4]==pi) and not (e[3]==j and e[4]==pj)])
                    assert np.linalg.matrix_rank(Lt,tol=1e-8)==n-1
                    actual = np.sort(eigh(Lg[1:,1:],Lt[1:,1:],eigvals_only=True))
                    predicted, trace = prediction(lengths,weights,retained)
                    assert np.allclose(actual,np.sort(predicted),rtol=1e-10,atol=1e-10), (lengths,weights,retained,pi,pj,actual,predicted)
                    assert np.isclose(actual.sum(),n-1+trace,atol=1e-10)
                    tests += 1
    return tests


def check_symbolic():
    t=sp.symbols('t',positive=True)
    short=(15+t+sp.sqrt(t*t+18*t+9))/6
    long=1+36/t
    short_trace=5+t/3
    long_trace=2+36/t
    assert sp.simplify(short.subs(t,sp.Rational(36,5))-long.subs(t,sp.Rational(36,5)))==0
    assert sp.simplify(((216/t-9-t)**2-(t*t+18*t+9)) + 72*(t+18)*(5*t-36)/t**2)==0
    tau=3*(sp.sqrt(57)-3)/2
    assert sp.simplify((short_trace-long_trace).subs(t,tau))==0
    assert sp.simplify(short_trace.subs(t,7)-sp.Rational(22,3))==0
    assert sp.simplify(long_trace.subs(t,7)-sp.Rational(50,7))==0
    assert sp.simplify((1+short).subs(t,7)-(14+sp.sqrt(46))/3)==0
    assert sp.simplify((1+long).subs(t,7)-sp.Rational(50,7))==0
    assert float(tau)<7<sp.Rational(36,5)
    return 7


if __name__=='__main__':
    a=check_numerical()
    b=check_symbolic()
    print(f'PASS: {a} grounded generalized-eigenvalue/trace cases; {b} symbolic comparisons.')
    print('Finite tests supplement the theorem; they do not prove the all-parameter statement.')
