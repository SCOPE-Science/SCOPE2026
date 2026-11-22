#!/usr/bin/env python3
"""Independent finite checks for triple-restricted edge cuts of Kneser graphs.

The all-order statement is proved by a spectral inequality, not by these tests.
"""
from itertools import combinations
from math import comb


def graph(n, k):
    v = list(combinations(range(n), k))
    masks = [sum(1 << x for x in s) for s in v]
    adj = [set() for _ in v]
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            if masks[i] & masks[j] == 0:
                adj[i].add(j)
                adj[j].add(i)
    return adj


def connected_after_removal(adj, rem):
    remaining = set(range(len(adj)))-set(rem)
    seed = next(iter(remaining))
    seen = {seed}
    stack = [seed]
    while stack:
        for j in adj[stack.pop()]:
            if j in remaining and j not in seen:
                seen.add(j)
                stack.append(j)
    return seen == remaining


def test_small(n, k):
    adj = graph(n, k)
    N = len(adj)
    d = len(adj[0])
    assert all(len(e)==d for e in adj)
    target = 3*d-(6 if n>=3*k else 4)
    count = 0
    good_trip = None
    for S in combinations(range(N),3):
        a,b,c = S
        e = int(b in adj[a])+int(c in adj[a])+int(c in adj[b])
        boundary = 3*d-2*e
        if e>=2 and boundary == target:
            count += 1
            if good_trip is None:
                good_trip = S
        assert boundary >= target
    for S in combinations(range(N),4):
        internal = sum(j in adj[i] for i,j in combinations(S,2))
        assert 4*d-2*internal > target
    assert good_trip is not None
    assert connected_after_removal(adj,good_trip)
    expected = N*comb(d,2) if n==3*k-1 else N*d*comb(n-2*k,k)//6
    assert count==expected, (n,k,count,expected)
    print('EXHAUSTIVE_THREE_AND_FOUR_SETS_PASS', n,k,'N=',N,'lambda3=',target,'optimal_cut_count=',count)


def test_spectral_inequalities():
    tested=0
    for k in range(3,25):
        for n in range(3*k-1,3*k+11):
            N=comb(n,k)
            d=comb(n-k,k)
            t=comb(n-k-2,k-2)
            # exact integer tests for the universal hypotheses
            assert 10*t <= 3*d
            assert N>=56 and d>=10
            assert 5*(d-t)*(N-5) > 3*d*N
            assert 2*(d-t) > 6
            tested+=1
    print('EXACT_INTEGER_SPECTRAL_THRESHOLDS_PASS',tested)


def test_spectrum_incidence_identity(n,k):
    adj=graph(n,k)
    v=list(combinations(range(n),k))
    masks=[sum(1<<x for x in S) for S in v]
    for i in range(k+1):
        coefficient=comb(n-k-i,k-i)
        for T in combinations(range(n),i):
            tm=sum(1<<x for x in T)
            for X,neighbors in enumerate(adj):
                lhs=sum((masks[j]&tm)==tm for j in neighbors)
                rhs=coefficient if masks[X]&tm==0 else 0
                assert lhs==rhs
    print('DIRECT_INCIDENCE_EIGENSPACE_IDENTITY_PASS',n,k)


if __name__=='__main__':
    test_spectrum_incidence_identity(8,3)
    test_small(8,3)
    test_small(9,3)
    test_spectral_inequalities()
    print('VERIFY_OK')
