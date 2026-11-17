#!/usr/bin/env python3
"""Exact finite checks for labelled subtree-size covariance in uniform recursive trees.
Every tree of order n has probability 1/(n-1)! under independent uniform parents.
These finite checks corroborate, but do not replace, the general induction proof.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import factorial

checks = 0
for n in range(2, 10):
    counts = Counter()
    for choices in product(*(range(1, k) for k in range(2, n + 1))):
        parent = [0, 0] + list(choices)
        sizes = [0] * (n + 1)
        for v in range(1, n + 1):
            x = v
            while x:
                sizes[x] += 1
                x = parent[x]
        counts[tuple(sizes[1:])] += 1
    total = factorial(n - 1)
    assert sum(counts.values()) == total
    checks += 1
    means = [Q(sum(c * z[i-1] for z,c in counts.items()),total) for i in range(1,n+1)]
    for i in range(1, n+1):
        assert means[i-1] == Q(n,i)
        checks += 1
        second=Q(sum(c * z[i-1]**2 for z,c in counts.items()),total)
        expected_var=Q(n*(n-i)*(i-1),i*i*(i+1))
        assert second-means[i-1]**2 == expected_var
        checks += 1
        for j in range(i+1,n+1):
            mixed = Q(sum(c*z[i-1]*z[j-1] for z,c in counts.items()),total)
            assert mixed==Q(n*n,i*j)
            checks += 1
            if 2<=i<j<n:
                joint=Q(sum(c for z,c in counts.items() if z[i-1]==1 and z[j-1]==1),total)
                assert joint==Q((i-1)*(j-2),(n-1)*(n-2))
                d=joint-Q(i-1,n-1)*Q(j-1,n-1)
                assert d==Q(-(i-1)*(n-j),(n-1)**2*(n-2))<0
                checks+=2
    path_mean=Q(sum(c*(sum(z)-n) for z,c in counts.items()),total)
    path_var=Q(sum(c*(sum(z)-n)**2 for z,c in counts.items()),total)-path_mean**2
    rhs=sum((Q(n*(n-i)*(i-1),i*i*(i+1)) for i in range(1,n+1)),Q(0))
    H=sum((Q(1,k) for k in range(1,n+1)),Q(0))
    H2=sum((Q(1,k*k) for k in range(1,n+1)),Q(0))
    assert path_var==rhs==n*n*(2-H2)-n*H
    checks+=1
print(f'PASS: {checks} exact assertions across all {(sum(factorial(n-1) for n in range(2,10)))} recursive trees of orders 2..9')
