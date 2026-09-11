"""Stdlib-only exact verification that D_n(w) == 0 for all n >= 1
under the standard FH convention, vs the claimed nonzero n^{-1/2} law."""
from fractions import Fraction
import math

# Exact Taylor coeffs c_k of (1+z)^{1/2} = sum c_k z^k, via recurrence
# c_0=1, c_j = c_{j-1}*(3/2-j)/j
def binom_half(k):
    c = Fraction(1)
    for j in range(1, k+1):
        c = c * Fraction(3 - 2*j, 2*j)
    return c

cs = [binom_half(k) for k in range(10)]
print("c0..c5:", [str(c) for c in cs[:6]])
assert cs[0] == Fraction(1), cs[0]
assert cs[1] == Fraction(1,2), cs[1]
assert cs[2] == Fraction(-1,8), cs[2]
assert cs[3] == Fraction(1,16), cs[3]
assert cs[4] == Fraction(-5,128), cs[4]

# Summability bound |c_k| <= sqrt(2)/(k+1)^{3/2} for k>=1
for k in range(1, 50):
    ck = binom_half(k)
    assert float(abs(ck)) <= math.sqrt(2)/(k+1)**1.5 + 1e-18, (k, ck)
print("summability bound OK for k=1..49")

# Fourier support: (f0)_m = c_m for m>=0 else 0 ; w_k = (f0)_{k-1}
def f0_coeff(m):
    return binom_half(m) if m >= 0 else Fraction(0)
def w_coeff(k):
    return f0_coeff(k-1)

# w_k = 0 for all k <= 0
for k in range(-6, 1):
    assert w_coeff(k) == 0, k
print("w_k = 0 for k<=0 OK; w_1..w_4 =", [str(w_coeff(k)) for k in range(1,5)])

def det_frac(M):
    n = len(M)
    A = [row[:] for row in M]
    det = Fraction(1)
    for i in range(n):
        piv = None
        for r in range(i, n):
            if A[r][i] != 0:
                piv = r; break
        if piv is None:
            return Fraction(0)
        if piv != i:
            A[i], A[piv] = A[piv], A[i]
            det = -det
        det *= A[i][i]
        inv = A[i][i]
        for r in range(i+1, n):
            f = A[r][i]/inv
            for c_ in range(i, n):
                A[r][c_] = A[r][c_] - f*A[i][c_]
    return det

for n in range(1, 9):
    T = [[w_coeff(i-j) for j in range(n)] for i in range(n)]
    assert all(v == 0 for v in T[0]), (n, T[0])  # first row identically zero
    d = det_frac(T)
    assert d == 0, (n, d)
    # base determinant: lower-triangular with unit diagonal
    Tb = [[f0_coeff(i-j) for j in range(n)] for i in range(n)]
    db = det_frac(Tb)
    assert db == 1, (n, db)
print("D_n(w)=0 and D_n(f0)=1 for n=1..8 OK")

# Claimed law predicts nonzero values
E0 = 2.0**(-1.0/8.0)
Wmod = 2.0**(-3.0/4.0)*math.gamma(0.75)/math.gamma(1.25)
C = Wmod*E0
print("claimed |W*| = %.6f  E0 = %.6f  product = %.6f" % (Wmod, E0, C))
for n in [1,4,16,64]:
    print("n=%d claimed |D_n|~%.6f  actual 0" % (n, C*n**-0.5))
assert C > 0.5, C  # claimed constant bounded away from zero
print("VERIFY_OK")
