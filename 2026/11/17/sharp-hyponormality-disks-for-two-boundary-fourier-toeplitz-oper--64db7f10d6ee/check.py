"""Exact-rational diagnostics for annular Hardy Toeplitz Fourier-mode shifts.

The analytic proof is independent of this finite checker. Run with Python >=3.9.
"""
from fractions import Fraction as F
from itertools import product

checks = 0

def confirm(statement):
    global checks
    assert statement
    checks += 1

def abs2(z):
    return z[0] * z[0] + z[1] * z[1]

def inner_real(a, b):
    return a[0] * b[0] + a[1] * b[1]

def norm_squared(R, k, n, A, B):
    t = R ** (2 * n + k)
    a, b, c = abs2(A), abs2(B), inner_real(A, B)
    return (a + 2*c*t + b*t*t) / ((1+R**(2*n))*(1+R**(2*n+2*k)))

def f(t, q, a, b, c):
    return (a + 2*c*t + b*t*t) / (1+(q+1/q)*t+t*t)

def condition(R, k, A, B):
    q = R**k
    return 2*inner_real(A, B) >= (q+1/q)*abs2(B)

for R, k in product((F(1,2),F(2,3),F(1,3)), (1, 2, 3)):
    q = R**k
    for u, v, x, y in product(range(-2,3), repeat=4):
        A, B = (F(u), F(v)), (F(x), F(y))
        a,b,c=abs2(A),abs2(B),inner_real(A,B)
        # Two coefficient inequalities are equivalent, including zero cases.
        base = (2*c >= (q+1/q)*b)
        both = (2*c >= (q+1/q)*b) and (2*c <= (q+1/q)*a)
        confirm(base == both)
        # The exact self-commutator diagonal factorization is independently
        # checked against the raw matrix coefficient calculation.
        for n in (-6,-3,0,1,4,8):
            t = R**(2*(n-k)+k)
            numerator = ((1-q*q)*t*(1+q*t)/q)*((1+q*q)*a-2*q*c+t*(2*q*q*c-q*(1+q*q)*b))
            den = (1+(q+1/q)*t+t*t)*(1+(q+1/q)*q*q*t+q**4*t*t)
            diff = norm_squared(R,k,n,A,B)-norm_squared(R,k,n-k,A,B)
            confirm(diff == numerator/den)
            if base:
                confirm(diff >= 0)

# Finite checks for a known sharp boundary: q=1/2, A=1,
# boundary real B=4/5, boundary nonreal B=2/5+2i/5.
R=F(1,2); k=1; A=(F(1),F(0))
for B,expected in [((F(0),F(0)),True),((F(4,5),F(0)),True),
                   ((F(2,5),F(2,5)),True),((F(9,10),F(0)),False),
                   ((F(-1,5),F(0)),False)]:
    confirm(condition(R,k,A,B)==expected)
    if expected:
        for n in range(-25,26):
            confirm(norm_squared(R,k,n,A,B)>=norm_squared(R,k,n-k,A,B))
    else:
        confirm(any(norm_squared(R,k,n,A,B)<norm_squared(R,k,n-k,A,B)
                    for n in range(-25,26)))

# Finite telescoping identity for the trace, valid for all cutoffs.
A=(F(1),F(2));B=(F(1,3),F(-1,5))
for R,k,N in product((F(1,2), F(2,3)), (1,2,3), (2,4,8)):
    finite_sum=sum((norm_squared(R,k,n,A,B)-norm_squared(R,k,n-k,A,B)
                    for n in range(-N,N+1)),F(0))
    boundary_sum=sum((norm_squared(R,k,n,A,B) for n in range(N-k+1,N+1)),F(0)) \
                 -sum((norm_squared(R,k,n,A,B) for n in range(-N-k,-N)),F(0))
    confirm(finite_sum==boundary_sum)
print('PASSED', checks, 'exact rational diagnostic identities and inequalities')
