"""Finite checks for the one-step modal degree-count probability theorem.

All exact graph probabilities use fractions. The Poisson calculations use
floating point only for numerical consistency checks, not for the proof.
"""
from fractions import Fraction
from collections import defaultdict
from math import comb, exp, factorial, log, log2


def all_pointed_graph_degree_probabilities(n, lam):
    p = Fraction(lam, n)
    assert 0 < p < 1
    q = 1-p
    arcs = [(i,j) for i in range(n) for j in range(n) if i != j]
    root_arc_indices = [z for z,(i,j) in enumerate(arcs) if i == 0]
    m = len(arcs)
    by_degree = defaultdict(Fraction)
    for mask in range(1 << m):
        edges = mask.bit_count()
        d = sum((mask >> i)&1 for i in root_arc_indices)
        by_degree[d] += p**edges * q**(m-edges)
    return [by_degree[k] for k in range(n)]


def binomial_outdegree_probabilities(n, lam):
    p = Fraction(lam, n)
    return [Fraction(comb(n-1,k))*p**k*(1-p)**(n-1-k)
            for k in range(n)]


def poisson_weights(lam, trunc=300):
    p0=exp(-lam)
    weights=[p0]
    for k in range(1,trunc):
        weights.append(weights[-1]*lam/k)
    return weights


def finite_tv(n, lam):
    b=[float(p) for p in binomial_outdegree_probabilities(n,lam)]
    q=poisson_weights(float(lam))
    return 0.5*(sum(abs(b[k]-(q[k] if k<len(q) else 0)) for k in range(n)) + sum(q[n:]))


def check():
    tests=0
    for n,lam in [(3,1),(3,2),(4,1),(4,2)]:
        explicit=all_pointed_graph_degree_probabilities(n,lam)
        formula=binomial_outdegree_probabilities(n,lam)
        assert explicit==formula,(n,lam,explicit,formula)
        assert sum(explicit)==1
        tests+=1
        # Every subset of degree values is definable by a Boolean combination.
        for mask in range(1<<n):
            a=sum((explicit[k] for k in range(n) if (mask>>k)&1),Fraction())
            b=sum((formula[k] for k in range(n) if (mask>>k)&1),Fraction())
            assert a==b
    for lam in [Fraction(1,2),Fraction(1),Fraction(2),Fraction(3)]:
        for n in [10,30,100,200]:
            if n>lam:
                tv=finite_tv(n,lam)
                bound=float((lam+lam*lam)/n)
                assert tv<=bound+1e-13,(n,lam,tv,bound)
                tests+=1
        w=poisson_weights(float(lam),350)
        for k in range(30,100):
            tail=sum(w[k+1:])
            assert w[k]>tail,(lam,k,w[k],tail)
            tests+=1
        if lam < Fraction(693,1000):
            assert exp(-float(lam))>0.5
    print('ALL_CHECKS_OK', 'tested_conditions=', tests)
    for lam in [0.5,1.0,2.0]:
        w=poisson_weights(lam,350)
        print('lambda=',lam,'p0=',w[0], 'tail40=',sum(w[40:]))

if __name__=='__main__':
    check()
