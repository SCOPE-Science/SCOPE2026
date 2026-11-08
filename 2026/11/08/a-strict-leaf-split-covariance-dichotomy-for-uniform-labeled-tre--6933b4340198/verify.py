#!/usr/bin/env python3
"""Exact exhaustive checks for leaf–cut-size covariance in uniform Cayley trees."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb
import heapq


def edges_from_prufer(seq, n):
    degree = [1] * n
    for v in seq:
        degree[v] += 1
    leaves = [i for i in range(n) if degree[i] == 1]
    heapq.heapify(leaves)
    edges = []
    for v in seq:
        u = heapq.heappop(leaves)
        edges.append((u, v))
        degree[u] -= 1
        degree[v] -= 1
        if degree[v] == 1:
            heapq.heappush(leaves, v)
    a = heapq.heappop(leaves)
    b = heapq.heappop(leaves)
    edges.append((a, b))
    return edges


def statistics(edges, n):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    leaf_count = sum(len(a) == 1 for a in adj)
    splits = [0] * (n // 2 + 1)
    for a, b in edges:
        stack = [a]
        seen = {b, a}
        count = 0
        while stack:
            v = stack.pop()
            count += 1
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        splits[min(count, n-count)] += 1
    return leaf_count, splits


def p_m(m):
    return Fraction(m - 1, m)**(m - 1) if m > 1 else Fraction(1)


def theoretical(n, k):
    # k <= floor(n/2); exactly n^(n-2) trees
    h = n * Fraction(n - 1, n)**(n - 2)
    avg = k * p_m(k) + (n-k)*p_m(n-k)
    en = Fraction(comb(n,k)* k**(k-1) * (n-k)**(n-k-1), n**(n-2) * (1 + (2*k == n)))
    return en, en * (avg - h)


def exhaustive(n):
    total = n**(n-2)
    sums = defaultdict(int)
    for seq in product(range(n), repeat=n-2):
        edges = edges_from_prufer(seq, n)
        leaves, splits = statistics(edges, n)
        sums['L'] += leaves
        sums['LL'] += leaves*leaves
        for k in range(1,n//2+1):
            sums[k] += splits[k]
            sums['prod', k] += leaves*splits[k]
    mean_L = Fraction(sums['L'], total)
    assert mean_L == n * Fraction(n - 1,n)**(n - 2)
    var_L = Fraction(sums['LL'],total) - mean_L**2
    nchecks = 1
    for k in range(1,n//2+1):
        e, cov = theoretical(n,k)
        assert Fraction(sums[k], total) == e, (n,k,'mean')
        assert Fraction(sums['prod',k],total) - mean_L*e == cov,(n,k,'cov')
        if k==1:
            assert cov == var_L
        else:
            assert cov < 0
        nchecks +=3
    if n>=4:
        assert var_L > 0
    else:
        assert var_L == 0
    nchecks +=1
    return total,nchecks


def main():
    total_trees = 0
    total_checks = 0
    for n in range(2,9):
        trees,checks=exhaustive(n)
        total_trees += trees
        total_checks+=checks
        print(f'n={n}: {trees} trees; {checks} exact formula/sign checks')
    for n in range(4,151):
        for k in range(2,n//2+1):
            e,c=theoretical(n,k)
            assert e>0 and c<0
            total_checks +=2
    print(f'PASS {total_trees} exhaustively enumerated Cayley trees; {total_checks} exact equalities and inequalities')

if __name__ == '__main__':
    main()
