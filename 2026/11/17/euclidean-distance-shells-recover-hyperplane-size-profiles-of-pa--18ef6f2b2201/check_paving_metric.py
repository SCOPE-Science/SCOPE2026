"""Finite numerical checks for Euclidean vertex distances of paving-base polytopes.

Uses explicit coordinate vertex hulls and numerical constrained least squares.
The unrestricted statement requires an analytical proof.
"""
from itertools import combinations
from fractions import Fraction
import numpy as np
from scipy.optimize import minimize


def run_case(n, k, hyperplanes):
    H = [frozenset(t) for t in hyperplanes]
    assert all(k <= len(h) < n for h in H)
    assert all(len(x & y) <= k-2 for i, x in enumerate(H) for y in H[i+1:])
    vectors = list(combinations(range(n), k))
    bases = [S for S in vectors if not any(set(S) <= h for h in H)]
    assert bases
    basesets = set(map(frozenset, bases))
    # Check the basis-exchange axiom and rank-minus-one independence.
    for I in combinations(range(n), k-1):
        assert any(frozenset(I) <= b for b in basesets)
    for X in basesets:
        for Y in basesets:
            for x in X-Y:
                assert any(frozenset((X-{x})|{y}) in basesets for y in Y-X)
    B = np.zeros((n, len(bases)), dtype=float)
    for col, b in enumerate(bases):
        B[list(b), col] = 1
    tested = 0
    for S in vectors:
        hs = [h for h in H if set(S) <= h]
        assert len(hs) <= 1
        v = np.zeros(n)
        v[list(S)] = 1
        if hs:
            h = hs[0]
            q = n-len(h)
            expected = Fraction(1,k)+Fraction(1,q)
            y = np.zeros(n)
            y[list(S)] = 1-1/k
            y[list(set(range(n))-h)] = 1/q
            # independently enumerate the basis witness, then compare exactly
            witness = []
            for i in S:
                for j in set(range(n))-h:
                    b = frozenset(set(S)-{i}|{j})
                    assert tuple(sorted(b)) in bases
                    w = np.zeros(n)
                    w[list(b)] = 1
                    witness.append(w)
            assert np.max(np.abs(y-np.mean(witness,axis=0))) < 1e-12
            assert abs(np.sum((v-y)**2)-float(expected)) < 1e-12
            # The exposed contact product has Gram determinant k*q.
            # Each block uses root differences of a regular simplex.
            s0 = next(iter(S))
            others = [t for t in S if t != s0]
            outside = sorted(set(range(n))-h)
            j0 = outside[0]
            dvecs = []
            for s in others:
                d = np.zeros(n); d[s] = 1; d[s0] = -1
                dvecs.append(d)
            for j in outside[1:]:
                d = np.zeros(n); d[j] = 1; d[j0] = -1
                dvecs.append(d)
            gram = np.array(dvecs)@np.array(dvecs).T
            assert abs(np.linalg.det(gram)-k*q)<1e-8
        else:
            expected = Fraction(0,1)
        if hs or (tested % 7 == 0):
            A = B.T@B
            g = B.T@v
            def fun(w):return float(np.sum((B@w-v)**2))
            def jac(w):return 2*(A@w-g)
            w0 = np.ones(len(bases))/len(bases)
            opt=minimize(fun, w0, jac=jac, method='SLSQP',bounds=[(0,None)]*len(bases),constraints=[{'type':'eq','fun':lambda w:np.sum(w)-1,'jac':lambda w:np.ones(len(w))}],options={'maxiter':700,'ftol':2e-12})
            if not opt.success and abs(fun(opt.x)-float(expected))>2e-7:
                raise ValueError(f'QP fail {n,k,S,opt.message,opt.fun,expected}')
            assert abs(fun(opt.x)-float(expected))<2e-7,(n,k,S,fun(opt.x),expected)
            tested+=1
    return len(vectors),len(bases),tested,len([s for s in vectors if any(set(s)<=h for h in H)])


if __name__=='__main__':
    cases=[
        (5,2,[(0,1,2)]),
        (6,2,[(0,1,2,3)]),
        (7,2,[(0,1,2,3,4)]),
        (6,3,[(0,1,2,3)]),
        (7,3,[(0,1,2,3,4)]),
        (8,3,[(0,1,2,3),(3,4,5,6,7)]),
        (8,4,[(0,1,2,3,4)]),
        (9,4,[(0,1,2,3,4,5)]),
        (7,3,[(0,1,2),(0,3,4),(1,5,6)]),
        (8,3,[(0,1,2,3,4,5)]),
    ]
    stats=[]
    for n,k,h in cases:
        v,b,t,missing=run_case(n,k,h)
        stats.append((v,b,t,missing))
        print(f'CASE n={n} k={k} hyperplane_sizes={[len(x) for x in h]} ksets={v} bases={b} qp={t} nonbases={missing}')
    print('PAVING_HYPERPLANE_METRIC_PASS cases=%d total_ksets=%d nonbases=%d independent_QP=%d' %(len(cases),sum(s[0] for s in stats),sum(s[3] for s in stats),sum(s[2] for s in stats)))
