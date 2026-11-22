"""Exact arithmetic certificate for the 5D R10 generalized symmetric-edge polytope.

Requires Python 3 and SymPy (tested with SymPy 1.13+).
All enumeration is finite and exhaustive; no numerical tolerance is used.
"""
from itertools import combinations, product
from math import comb
from sympy import Matrix, eye, zeros, Rational, sqrt

n = 5
D = Matrix([[int((i-j) % n in (1,n-1))-int(i == j)
             for j in range(n)] for i in range(n)])
M = eye(n).row_join(D)
assert M.shape == (5,10)
assert D.det() == 1
# Check all square minors: TU representation of the sporadic regular matroid.
minor_counts = {-1: 0, 0: 0, 1: 0}
for size in range(1,6):
    for row_set in combinations(range(5),size):
        for col_set in combinations(range(10),size):
            minor_counts[int(M.extract(row_set,col_set).det())] += 1
assert sum(minor_counts.values()) == sum(comb(5,k)*comb(10,k) for k in range(1,6))
assert minor_counts == {-1: 512, 0: 1920, 1: 570}, minor_counts

S = M*M.T
A = 2*S.inv()
assert A.det() == Rational(16,81)
assert A == Matrix([[1, Rational(1,3), -Rational(1,3), -Rational(1,3), Rational(1,3)],
                    [Rational(1,3),1,Rational(1,3),-Rational(1,3),-Rational(1,3)],
                    [-Rational(1,3),Rational(1,3),1,Rational(1,3),-Rational(1,3)],
                    [-Rational(1,3),-Rational(1,3),Rational(1,3),1,Rational(1,3)],
                    [Rational(1,3),-Rational(1,3),-Rational(1,3),Rational(1,3),1]])
assert A.eigenvals() == {1:1, 1+sqrt(5)/3:2, 1-sqrt(5)/3:2}
assert all((M[:,j].T*A*M[:,j])[0] == 1 for j in range(10))
assert A*(M*M.T) == 2*eye(5)

# Polar Q: coordinate inequalities |y_i| <= 1 and |(D*y)_i| <= 1.
# The TU property makes all Q vertices integral, hence among 3**5 ternary points.
rank_count = {}
feasible = []
vertices = []
for entries in product((-1,0,1), repeat=n):
    y = Matrix(entries)
    vals = M.T*y
    if any(abs(vals[k]) > 1 for k in range(10)):
        continue
    tight_indices = [j for j in range(10) if abs(vals[j]) == 1]
    rank = M[:, tight_indices].rank() if tight_indices else 0
    nz = sum(t != 0 for t in entries)
    rank_count[(nz,rank)] = rank_count.get((nz,rank),0) + 1
    feasible.append(y)
    if rank == 5:
        vertices.append(y)
assert rank_count == {(0,0):1,(1,4):10,(2,4):20,
                      (3,4):20,(4,4):10,(5,5):12}, rank_count
assert len(feasible) == 73 and len(vertices) == 12

ones = Matrix([1]*n)
base = (1,1,1,-1,-1)
expected = {tuple(ones),tuple(-ones)}
for k in range(n):
    shift = tuple(base[(j-k) % n] for j in range(n))
    expected.add(shift)
    expected.add(tuple(-z for z in shift))
assert len(expected) == 12
assert {tuple(y) for y in vertices} == expected

# Twelve polar vertices are in A-isotropic position and all share one polar ellipsoid.
cov = sum((y*y.T for y in vertices),zeros(5))/12
assert cov == A
assert all((y.T*A.inv()*y)[0] == 5 for y in vertices)
assert sum((M[:,j]*M[:,j].T for j in range(10)),zeros(5)) == 2*A.inv()

# Affine independent polytopal facets are guaranteed by the 5-active-normal rank.
# John's condition: a unit-sphere contact measure with identity second moment.
assert A*cov == A*A  # consistency control of the exact covariance identity
print('R10_ELLIPSOIDS_EXACT_PASS')
print('all_square_minors',sum(minor_counts.values()),minor_counts)
print('feasible_polar_lattice_points',len(feasible),'polar_vertices',len(vertices))
print('polar_support_rank_histogram',dict(sorted(rank_count.items())))
print('det_A',A.det(),'eig_A',A.eigenvals())
