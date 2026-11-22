"""Exact checks for complementary length-three moving cylinders in binary shift.

Run: python verify.py (standard Python 3, no dependencies).
"""
from itertools import product, permutations
from fractions import Fraction

M0 = ((0, 0, 1, 0), (1, 0, 1, 0), (0, 1, 0, 1), (0, 1, 0, 1))
M1 = ((1, 0, 1, 0), (1, 0, 1, 0), (0, 1, 0, 1), (0, 1, 0, 0))
ZERO = (1, 1, 1, 1)

def mv(mat, vec):
    return tuple(sum(a*b for a, b in zip(row, vec)) for row in mat)

def mm(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))

def eye(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))

def matrix_for(schedule):
    mat = eye(4)
    for c in schedule:
        mat = mm(M0 if c == '0' else M1, mat)
    return mat

def transfer_count(schedule):
    v = ZERO
    for c in schedule:
        v = mv(M0 if c == '0' else M1, v)
    return sum(v)

def direct_count(schedule):
    n = len(schedule)
    total = 0
    for bits in product('01', repeat=n+2):
        if all(''.join(bits[i:i+3]) != c*3 for i, c in enumerate(schedule)):
            total += 1
    return total

def charpoly_coeffs(mat):
    # Exact determinant expansion at five integer arguments, no spectral library.
    # Polynomial interpolation via finite differences, normalized monic.
    def determinant(a):
        value = 0
        for perm in permutations(range(4)):
            inversions = sum(perm[i] > perm[j] for i in range(4) for j in range(i+1,4))
            term = (-1)**inversions
            for i, j in enumerate(perm):
                term *= a[i][j]
            value += term
        return value
    vals = [determinant(tuple(tuple((int(i == j)*q)-mat[i][j]
                    for j in range(4)) for i in range(4))) for q in range(5)]
    diffs = [vals]
    for _ in range(4):
        diffs.append([diffs[-1][i+1]-diffs[-1][i] for i in range(len(diffs[-1])-1)])
    # Newton forward basis P(x) = sum Delta^k P(0) * x(x-1)...(x-k+1)/k!
    coeffs = [Fraction(0)]*5
    falling = [Fraction(1)]
    fact = 1
    for k in range(5):
        if k:
            falling2 = [Fraction(0)]*(k+1)
            for j, x in enumerate(falling):
                falling2[j] -= (k-1)*x
                falling2[j+1] += x
            falling = falling2
            fact *= k
        for j, x in enumerate(falling):
            coeffs[j] += Fraction(diffs[k][0], fact)*x
    return tuple(int(x) if x.denominator == 1 else x for x in coeffs)

def poly(coeffs, x):
    y = 0
    for c in reversed(coeffs):
        y = y*x+c
    return y

assert charpoly_coeffs(matrix_for('01')) == (0, -1, -3, -2, 1)
assert charpoly_coeffs(matrix_for('010')) == (0, -1, 4, -6, 1)

L2 = Fraction(3079595, 1000000)
U2 = Fraction(3079596, 1000000)
L3 = Fraction(5278039, 1000000)
U3 = Fraction(5278040, 1000000)
p2 = (-1, -3, -2, 1)
p3 = (-1, 4, -6, 1)
assert poly(p2, L2) < 0 < poly(p2, U2)
assert poly(p3, L3) < 0 < poly(p3, U3)
assert U3**2 < L2**3

minima = [7,12,21,37,64]
for n in range(1, 9):
    counts = {''.join(s): transfer_count(''.join(s)) for s in product('01', repeat=n)}
    for schedule, count in counts.items():
        assert count == direct_count(schedule), (schedule, count)
    if n <= 5:
        assert min(counts.values()) == minima[n-1], n
    if n == 5:
        assert sorted(k for k, v in counts.items() if v == min(counts.values())) == [
            '01001','01101','10010','10110']
    print('n=%d schedules=%d minimum=%d' % (n, len(counts), min(counts.values())))
for s in ('0','01','010','01001','01010','010010','010101'):
    print('count', s, transfer_count(s))
print('PASS: complete finite tests and exact spectral certificates')
