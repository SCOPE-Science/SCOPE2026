"""Finite rational verification for the parent-linked duplication graph moment laws.

Run with Python 3.10+: python checker.py
This checks exact finite instances. It does not certify asymptotic limits.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

ASSERTIONS = 0

def verify(x, y, label):
    global ASSERTIONS
    ASSERTIONS += 1
    assert x == y, (label, x, y)

def grow(distribution, p, r):
    next_distribution = defaultdict(F)
    n = next(iter(distribution))[0]
    for (vertex_count, edges), mass in distribution.items():
        verify(vertex_count, n, 'vertex count')
        for parent in range(n):
            neighbors = [v for v in range(n) if tuple(sorted((parent, v))) in edges]
            trials = [(parent, r)] + [(v, p) for v in neighbors]
            for choices in product((0, 1), repeat=len(trials)):
                weight = mass / n
                new_edges = set(edges)
                for (vertex, probability), include in zip(trials, choices):
                    weight *= probability if include else (1 - probability)
                    if include:
                        new_edges.add(tuple(sorted((vertex, n))))
                next_distribution[(n + 1, frozenset(new_edges))] += weight
    verify(sum(next_distribution.values()), F(1), 'normalization')
    return dict(next_distribution)

def direct_moments(distribution):
    mean_edges = mean_degree_square = mean_edges_square = F(0)
    for (n, edges), weight in distribution.items():
        degrees = [0] * n
        for i, j in edges:
            degrees[i] += 1
            degrees[j] += 1
        count = len(edges)
        mean_edges += weight * count
        mean_degree_square += weight * sum(d*d for d in degrees)
        mean_edges_square += weight * count * count
    return mean_edges, mean_degree_square, mean_edges_square-mean_edges**2

def verify_model(p, r, maximum_n=5):
    distribution = {(1, frozenset()): F(1)}
    mean_edges = mean_square_degrees = variance_edges = F(0)
    coefficient = 4*r + 4*p - 2*p*p + 4*p*r
    exponent = 2*p+p*p
    for n in range(1, maximum_n+1):
        measured = direct_moments(distribution)
        verify(measured, (mean_edges, mean_square_degrees, variance_edges),
               ('moments', p, r, n))
        verify(sum(distribution.values()), F(1), ('probability', p, r, n))
        variance_increment = (r*(1-r)+2*p*(1-p)*mean_edges/n
                              +p*p*(mean_square_degrees/n-4*mean_edges**2/n**2))
        verify(variance_increment >= 0, True, ('nonnegative forcing',p,r,n))
        variance_edges = (1+4*p/n)*variance_edges+variance_increment
        mean_square_degrees = ((1+exponent/n)*mean_square_degrees
                               +coefficient*mean_edges/n+2*r)
        mean_edges = (1+2*p/n)*mean_edges+r
        distribution = grow(distribution, p, r)

def check_physics_coefficient(p):
    # Equation (16) of Bhat et al. (2016), for the certain parent edge.
    assert F(0) < p < F(1,4)
    c = 1/(1-2*p)
    b = 4+4*p-2*p*p+4*p
    d = (2+b*c)/(1-2*p-p*p)
    sigma = 2*p*(1-p)*c+p*p*(d-4*c*c)
    older = (2*p*(1-5*p+2*p*p)/(1-2*p)**2
             +2*p*p/(1-2*p)*(3+2*p-p*p)/(1-2*p-p*p))
    verify(sigma, older, ('comparison with previously predicted r=1 coefficient',p))

for p, r in ((F(1,5),F(1,2)), (F(1,4),F(1)),
             (F(1,3),F(2,3)), (F(3,5),F(1,3))):
    verify_model(p,r)
for p in (F(1,10),F(1,5),F(1,6),F(1,7)):
    check_physics_coefficient(p)
print('PASS: {} finite exact-rational assertions'.format(ASSERTIONS))
