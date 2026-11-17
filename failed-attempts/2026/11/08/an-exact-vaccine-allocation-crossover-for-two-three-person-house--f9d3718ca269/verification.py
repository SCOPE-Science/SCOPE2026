#!/usr/bin/env python3
"""Exact independent enumeration for a two-household bond-percolation vaccination theorem.
Run with Python >=3.8; standard library only.
"""
from fractions import Fraction as F
from itertools import combinations, product

assertions = 0

def check(condition, label):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(label)

def expected(m, s, p):
    """Enumerate each undirected contact graph and external infection seed set."""
    edges = tuple(combinations(range(m), 2))
    answer = F(0)
    for open_bits in product((0, 1), repeat=len(edges)):
        graph_weight = p ** sum(open_bits) * (1-p) ** (len(edges)-sum(open_bits))
        adjacency = [[] for _ in range(m)]
        for (u, v), active in zip(edges, open_bits):
            if active:
                adjacency[u].append(v)
                adjacency[v].append(u)
        for imported in product((0, 1), repeat=m):
            weight = graph_weight * s ** sum(imported) * (1-s) ** (m-sum(imported))
            reached = {i for i, a in enumerate(imported) if a}
            frontier = list(reached)
            while frontier:
                for v in adjacency[frontier.pop()]:
                    if v not in reached:
                        reached.add(v)
                        frontier.append(v)
            answer += weight * len(reached)
    return answer

def closed_form(m,s,p):
    if m == 0: return F(0)
    if m == 1: return s
    if m == 2: return 2*s*(1+(1-s)*p)
    if m == 3:
        return 3*(1-(1-s)*((1-p)**2+2*p*(1-p)**2*(1-s)+(3*p*p-2*p**3)*(1-s)**2))
    raise ValueError(m)

def gap(s,p):
    return p*s*(1-s)*(2+6*p-6*p*p-s*p*(9-6*p))

# Independent pair of exact computations: brute graph/seed enumeration and component formulas.
for i,j in product(range(1,20),repeat=2):
    p,s = F(i,20),F(j,20)
    e = [expected(m,s,p) for m in range(4)]
    for m in range(4):
        check(e[m]==closed_form(m,s,p),f'formula m={m} p={p} s={s}')
    check(e[1]+e[3]-2*e[2]==gap(s,p),'factored allocation difference')
    check(e[2]-2*e[1]==2*s*(1-s)*p,'size-two strict split optimality')
    split=2*e[2]; concentrate=e[1]+e[3]
    threshold=(2+6*p-6*p*p)/(9*p-6*p*p)
    expected_sign = 1 if p<=F(2,3) or s<threshold else (-1 if s>threshold else 0)
    observed_sign = (concentrate>split)-(concentrate<split)
    check(observed_sign==expected_sign,'global classification')

# An interior exact tie and two strict parameter regimes.
p=F(9,10)
s=F(127,162)
check(gap(s,p)==0,'exact tie')
check(expected(1,s,p)+expected(3,s,p)==2*expected(2,s,p),'enumerated tie')
p=s=F(9,10)
check(gap(s,p)==-F(3807,125000),'exact concentration witness')
check(expected(1,s,p)+expected(3,s,p)==F(486693,125000),'concentrated cost')
check(2*expected(2,s,p)==F(981,250),'split cost')
p=s=F(1,2)
check(gap(s,p)>0,'strict splitting witness')

print('PASS',assertions,'exact-rational assertions')
