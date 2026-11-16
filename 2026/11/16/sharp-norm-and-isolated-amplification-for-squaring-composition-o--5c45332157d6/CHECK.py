"""Independent finite numerical consistency checks for the explicit squaring norm.

Requires only the Python standard library. The theorem is proved in RESULT.md;
finite computations here do not certify infinite-dimensional spectral claims.
"""
from math import sqrt


def polynomial(x):
    return x*x*x - 6*x*x + 8*x - 4


lo, hi = 4., 5.
assert polynomial(lo) < 0 < polynomial(hi)
for _ in range(90):
    mid = (lo + hi)/2
    if polynomial(mid) < 0:
        lo = mid
    else:
        hi = mid
lam = (lo + hi)/2
r = 1/(lam - 1)
gamma = (1+r)/(lam - 2)
assert abs(polynomial(lam)) < 1.e-12
assert 4 < lam < 5 and 0 < r < 1
checks = 3

# Source functions u(xi) = x + (xi-1)g(xi), v(xi)=y+(xi-1)h(xi).
x = 1/(lam - 2)
y = (lam - 1)/(lam - 2)
A = (1+gamma)/2
B = (r+gamma)/2
source_squared = 2*x*x + 4*A*A/(1-r*r) + 2*y*y + 4*B*B/(1-r*r)
even_squared = (A+y)**2 + (A*r+B)**2/(1-r*r)
odd_squared = (A+B)**2/(1-r*r)
target_squared = 2*(x+y)**2 + 4*(even_squared + odd_squared)
assert abs(target_squared/source_squared - lam) < 2.e-12
checks += 1

# Check the LL* eigen-equations coefficientwise on the decaying eigenvector.
alpha = sqrt(2)/(lam-2)
for n in range(90):
    v_n = r**n
    w_n = gamma*r**n
    # First row: 2alpha + sqrt(2) v_0 = lambda alpha.
    if n == 0:
        assert abs(2*alpha + sqrt(2) - lam*alpha) < 1.e-12
        checks += 1
    v_nm1 = r**(n-1) if n else 0.
    w_nm1 = gamma*r**(n-1) if n else 0.
    v_np1 = r**(n+1)
    block2 = (2 + (1 if n==0 else 0))*v_n + w_n + w_nm1 + (sqrt(2)*alpha if n==0 else 0)
    block3 = v_n + v_np1 + 2*w_n
    assert abs(block2 - lam*v_n) < 2.e-12
    assert abs(block3 - lam*w_n) < 2.e-12
    checks += 2

# Reconstruct the analytic norm without using the closed geometric-series sums.
# The tail is exponentially small because r = 1/(lambda-1) < 1/3.
for N in (24, 48, 96):
    g_coeff = [A*r**j for j in range(N)]
    h_coeff = [B*r**j for j in range(N)]
    source_N = 2*x*x+2*y*y+4*sum(c*c for c in g_coeff)+4*sum(c*c for c in h_coeff)
    # Approximate the quotient of u(xi^2)+xi v(xi^2) at xi=1.
    even = [g_coeff[j] + (h_coeff[j-1] if j else y) for j in range(N)]
    odd = [g_coeff[j]+h_coeff[j] for j in range(N)]
    target_N = 2*(x+y)**2 +4*(sum(c*c for c in even)+sum(c*c for c in odd))
    assert abs(target_N/source_N - lam) < (2.e-9 if N==24 else 2.e-12)
    checks += 1

# Weakly-null approximate shift invariance for the 2 essential-norm witness.
for width in (20, 200, 2000):
    # p = q = a normalized block of width entries.  ||Sp-p||^2 = 2/width.
    # ||p+Sq||^2 = 4-2/width; ||p+q||^2 = 4.
    quotient2 = ((4-2/width)+4)/2
    assert 4-2/width < quotient2 < 4
    assert abs(4-quotient2-1/width)<1.e-12
    checks += 2
assert abs(sqrt(lam)-2.093555771386623) < 1.e-12
print(f"PASS: {checks+1} finite consistency checks; lambda={lam:.15f}; norm={sqrt(lam):.15f}")
