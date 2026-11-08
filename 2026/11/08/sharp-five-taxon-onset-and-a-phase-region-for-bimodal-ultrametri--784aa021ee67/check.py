#!/usr/bin/env python3
"""Exact rational subset and symbolic variance checks for five-taxon rarefaction."""
from fractions import Fraction as F
from itertools import combinations

# Leaf order 0,1,2,3,4. Each clade mask indexes a tree edge.
MASKS = (1, 2, 8, 16, 4, 24, 3, 28)
# Each edge length: (constant, coefficient of alpha, beta, gamma).
LENGTHS = ((1,-1,0,0),(1,-1,0,0),(1,0,0,-1),(1,0,0,-1),
           (1,0,-1,0),(0,0,-1,1),(0,1,0,0),(0,0,1,0))

def edge_lengths(a,b,g):
    return (1-a, 1-a, 1-g, 1-g, 1-b, g-b, a, b)

def sample_vectors(k):
    for ids in combinations(range(5),k):
        mask=sum(1<<i for i in ids)
        yield tuple(sum((LENGTHS[j][u] for j,c in enumerate(MASKS) if mask&c),0)
                    for u in range(4))

def variance_direct(k,a,b,g):
    vals=[]
    weights=edge_lengths(a,b,g)
    for ids in combinations(range(5),k):
        mask=sum(1<<i for i in ids)
        vals.append(sum((weights[j] for j,c in enumerate(MASKS) if mask&c),F(0)))
    mean=sum(vals,F(0))/len(vals)
    return sum(((v-mean)**2 for v in vals),F(0))/len(vals)

def coefficient_vector(k):
    rows=list(sample_vectors(k)); n=len(rows)
    means=[sum((F(row[u]) for row in rows),F(0))/n for u in range(4)]
    assert all(row[0]==k for row in rows)
    centered=[tuple(F(row[u])-means[u] for u in range(1,4)) for row in rows]
    return tuple(sum((row[i]*row[j] for row in centered),F(0))*((2 if i<j else 1))/n
                 for i,j in ((0,0),(0,1),(0,2),(1,1),(1,2),(2,2)))

def polynomial_var(k,a,b,g):
    coeffs=coefficient_vector(k)
    mons=(a*a,a*b,a*g,b*b,b*g,g*g)
    return sum((c*m for c,m in zip(coeffs,mons)),F(0))

expected={
  0:(0,)*6,
  1:(0,)*6,
  2:(F(9,100),F(-4,100),F(-2,100),F(16,100),F(-4,100),F(9,100)),
  3:(F(21,100),F(-30,100),F(-18,100),F(25,100),F(-10,100),F(21,100)),
  4:(F(6,25),F(-4,25),F(-8,25),F(4,25),F(-4,25),F(6,25)),
  5:(0,)*6
}
for k in range(6):
    assert coefficient_vector(k)==expected[k],(k,coefficient_vector(k))

A,B,G=F(14,15),F(1,3),F(2,5)
assert 0<B<G<1 and 0<A<1
assert all(x>0 for x in edge_lengths(A,B,G))
expected_variances=(F(0),F(0),F(32,375),F(317,4500),F(28,375),F(0))
for k in range(6):
    a=variance_direct(k,A,B,G)
    b=polynomial_var(k,A,B,G)
    assert a==b==expected_variances[k],(k,a,b)
assert expected_variances[2]-expected_variances[3]==F(67,4500)
assert expected_variances[4]-expected_variances[3]==F(19,4500)

# Additional exact parameter tests across the whole admissible three-height domain.
cases=0
for a in (F(1,5),F(1,2),F(4,5),F(14,15)):
    for b in (F(1,8),F(1,3),F(1,2)):
        for g in (F(2,5),F(3,5),F(4,5),F(9,10)):
            if b>=g: continue
            for k in range(6):
                assert variance_direct(k,a,b,g)==polynomial_var(k,a,b,g)
            cases+=1
assert cases>=30
print('PASS: six symbolic variance polynomials; all witness subsets; two strict peaks; '+str(cases)+' additional admissible height triples')
