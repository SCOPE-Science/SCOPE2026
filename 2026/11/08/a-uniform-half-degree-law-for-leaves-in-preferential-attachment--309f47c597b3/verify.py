#!/usr/bin/env python3
"""Reproducible finite checks for a preferential-attachment leafdegree theorem.
The theorem's asymptotic conclusions are proved analytically, not by this script.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial
import random

checks = 0

def eq(x, y):
    global checks
    assert x == y, (x, y)
    checks += 1


def tree(parents):
    # Initial edge 0--1, then parent[v-2] lies in [0,v-1].
    n = len(parents) + 2
    adj = [set() for _ in range(n)]
    adj[0].add(1)
    adj[1].add(0)
    for v, p in enumerate(parents, start=2):
        adj[v].add(p)
        adj[p].add(v)
    return adj


def degrees_leafdegrees(adj):
    d = [len(nei) for nei in adj]
    l = [sum(d[u] == 1 for u in nei) for nei in adj]
    return d, l


def histories(n):
    for parents in product(*(range(v) for v in range(2, n))):
        yield parents


def rising(x, r):
    a = 1
    for j in range(r):
        a *= x + j
    return a


def check_local():
    # Every possible finite labelled tree (not just a simulation).
    for n in range(3, 8):
        for parents in histories(n):
            adj = tree(parents)
            d, l = degrees_leafdegrees(adj)
            eq(sum(d), 2 * (n - 1))
            eq(sum(l), sum(x == 1 for x in d))
            for v in range(n):
                old_a = Q(2*l[v]-d[v], 2)
                # All next attachments, exact rational transition probabilities.
                actual_drift = Q(0)
                actual_var_upper = Q(0)
                for u in range(n):
                    adj2 = [a.copy() for a in adj]
                    adj2.append({u}); adj2[u].add(n)
                    new_d, new_l = degrees_leafdegrees(adj2)
                    da = Q(2 * (new_l[v] - l[v]) - (new_d[v] - d[v]), 2)
                    indicator_da = Q(1, 2) * (u == v) - int(u in adj[v] and d[u] == 1)
                    eq(da, indicator_da)
                    weight = Q(d[u], 2*(n-1))
                    actual_drift += weight * da
                    actual_var_upper += weight * da * da
                eq(actual_drift, -old_a / (2*(n-1)))
                assert actual_var_upper <= Q(d[v], n-1)
                checks_add_one()


def checks_add_one():
    global checks
    checks += 1


def check_global():
    # Exact sum over all attachment histories for small sizes.
    for n in range(2, 8):
        s2 = Q(0); moments = [Q(0) for _ in range(5)]; prob_total = Q(0)
        for parents in histories(n):
            adj = tree(parents)
            d, _ = degrees_leafdegrees(adj)
            prob = Q(1)
            partial_adj = tree(())
            for v, p in enumerate(parents, start=2):
                prob *= Q(len(partial_adj[p]), 2*(v-1))
                partial_adj.append({p}); partial_adj[p].add(v)
            prob_total += prob
            s2 += prob * sum(x*x for x in d)
            for r in range(1, 6):
                moments[r-1] += prob * rising(d[0], r)
        eq(prob_total, Q(1))
        harmonic = sum((Q(1,j) for j in range(1,n)),Q(0))
        eq(s2, 2*(n-1)*harmonic)
        for r in range(1, 6):
            pred = Q(factorial(r))
            for t in range(1,n-1):
                pred *= Q(2*t+r,2*t)
            eq(moments[r-1],pred)


def check_simulation():
    # Fixed-seed optional diagnostics only, not used to establish infinity limit.
    rng = random.Random(20261102)
    n=8192
    for _ in range(24):
        d=[1,1]; l=[1,1]; neighbor=[1,0]
        endpoint=[0,1]
        for v in range(2,n):
            u=endpoint[rng.randrange(len(endpoint))]
            if d[u]==1:
                l[neighbor[u]]-=1
            d[u]+=1
            l[u]+=1
            d.append(1);l.append(0);neighbor.append(u)
            endpoint.append(u);endpoint.append(v)
        eq(sum(d),2*(n-1))
        eq(sum(l),sum(x==1 for x in d))
        assert max(l)>0 and max(d)>0
        checks_add_one()

if __name__=='__main__':
    check_local()
    check_global()
    check_simulation()
    print('PASS:',checks,'finite exact-rational and seeded diagnostic checks')
