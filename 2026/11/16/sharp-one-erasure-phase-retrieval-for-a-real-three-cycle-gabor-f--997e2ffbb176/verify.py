"""Exact reproduction of the three-cycle Gabor phase-retrieval calculation.

Run: python verify.py (requires SymPy). No numerical tolerance is used.
"""
from itertools import combinations
from sympy import Matrix, symbols, factor, expand, Rational, I, sqrt, conjugate

s = symbols('s', real=True)

# Hermitian real basis: 3 diagonal, then three symmetric entries, then
# three imaginary skew entries (upper entry i*sqrt(3)).
B = []
for i in range(3):
    H = Matrix.zeros(3)
    H[i, i] = 1
    B.append(H)
for i, j in combinations(range(3), 2):
    H = Matrix.zeros(3)
    H[i, j] = H[j, i] = 1
    B.append(H)
for i, j in combinations(range(3), 2):
    H = Matrix.zeros(3)
    H[i, j], H[j, i] = I * sqrt(3), -I * sqrt(3)
    B.append(H)

# Generate the integer-valued real analysis matrix using 2Re(omega^j)
# and 2Re(i sqrt(3) omega^j), avoiding approximate complex arithmetic.
rows = []
for k in range(3):
    amplitudes = [1, 1, s]
    amplitudes = amplitudes[-k:] + amplitudes[:-k] if k else amplitudes
    for m in range(3):
        row = [a*a for a in amplitudes]
        for i, j in combinations(range(3), 2):
            t = (m*(j-i)) % 3
            row.append((2 if t == 0 else -1)*amplitudes[i]*amplitudes[j])
        for i, j in combinations(range(3), 2):
            t = (m*(j-i)) % 3
            row.append((0 if t == 0 else (-3 if t == 1 else 3))*amplitudes[i]*amplitudes[j])
        rows.append(row)
A = Matrix(rows)

expected_det = -5832*(s-1)**6*(s+1)**2*(2*s+1)**2*(s*s+2)
assert expand(A.det()-expected_det) == 0

# Explicit polynomial kernel of the 8 rows remaining after deleting (0,0).
a = (s+1)*(s*s+2)
v = Matrix([-(2*s+1), -(2*s+1), (2*s+1)*(s*s+1),
            -(s+1)*a, s*a, s*a, 0, 0, 0])
assert all(expand(e)==0 for e in A[1:, :]*v)
H = sum((v[j]*B[j] for j in range(9)), Matrix.zeros(3))
q = 2*s**4+2*s**3+5*s*s+6*s+3
assert expand(H.det()+(s*s+s+1)**4*q)==0
assert expand(q-(2*(s*s+s/2)**2+Rational(9,2)*(s+Rational(2,3))**2+1)) == 0

# The nine one-erasure choices are unitarily conjugate. Also reproduce
# special-parameter ranks and representative row-kernel data exactly.
for z, full_rank, eight_rank in ((1,3,3),(-1,7,7),
                                 (Rational(-1,2),7,7),(0,9,8),(2,9,8)):
    M = A.subs(s,z)
    assert M.rank() == full_rank
    assert M[1:,:].rank() == eight_rank
for removal in range(9):
    assert A.subs(s,2).extract([j for j in range(9) if j != removal],range(9)).rank()==8
print('PASS: full-rank factorization, exact kernel, cubic determinant, strict positivity identity, all nine erasures and special strata')
