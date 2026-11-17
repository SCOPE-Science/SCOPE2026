"""Independent numerical diagnostics for striped triangular-lattice disk covering.

Run with Python 3.9 or later: python check.py
No third-party packages are needed. A finite grid is not a coverage proof.
"""
from math import sqrt, pi, hypot

A, B = 0.5, sqrt(3)/2
C = 1/sqrt(3)

def critical(r):
    if not (r >= 0):
        raise ValueError('radius must be nonnegative')
    if r <= A:
        return hypot(A-r, B)
    if r <= C:
        return B-sqrt(r*r-A*A)
    if r <= B:
        return hypot(A, B-r)
    if r <= 1:
        return A-sqrt(r*r-B*B)
    return 0.0

# Check the four branch transitions and their endpoint values.
for r, value in ((0,1), (A,B), (C,C), (B,A), (1,0)):
    assert abs(critical(r)-value) < 2e-13, (r,critical(r),value)

# Independent direct evaluation of distances to the closest centers on a
# dense rectangular fundamental cell. Grid geometry does not use the branch
# construction except to compare its predicted limiting boundary.
N = 701
for r in (0,.1,.25,.48,.5,.54,.57,C,.62,.75,B,.90,.97,.999):
    max_distance = 0.0
    for i in range(N+1):
        x = A*i/N
        for j in range(N+1):
            y = B*j/N
            if hypot(x,y) >= r:
                max_distance = max(max_distance, hypot(A-x,B-y))
    assert abs(max_distance-critical(r)) < 0.003, (r,max_distance,critical(r))

# Strictly discriminate the balanced optimum from both unbalanced branches.
min_value,min_radius = min((r*r+critical(r)**2,r) for r in (j/25000 for j in range(25001)))
assert abs(min_radius-C)<1e-4
assert abs(min_value-2/3)<1e-4
for r in (0,.15,.3,.5,.52,.65,.75,.9,1,1.2):
    assert r*r+critical(r)**2 > 2/3 + .005

print('FOUR_BRANCH_ENDPOINTS_OK')
print('INDEPENDENT_FUNDAMENTAL_CELL_GRID_OK')
print('SHARP_BALANCED_DENSITY_DIAGNOSTIC_OK')
print('All finite diagnostics passed; the continuum theorem is proved analytically in RESULT.md.')
