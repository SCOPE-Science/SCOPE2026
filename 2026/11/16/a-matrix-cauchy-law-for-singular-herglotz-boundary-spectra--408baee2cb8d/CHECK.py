"""Finite checks for the matrix boundary Cauchy identity; Python 3 standard library only."""
import cmath
import math

PI = math.pi


def madd(A, B):
    return ((A[0][0] + B[0][0], A[0][1] + B[0][1]),
            (A[1][0] + B[1][0], A[1][1] + B[1][1]))


def smul(c, A):
    return tuple(tuple(c * v for v in row) for row in A)


def minv(A):
    d = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return ((A[1][1] / d, -A[0][1] / d),
            (-A[1][0] / d, A[0][0] / d))


def diff(A, B):
    return max(abs(A[i][j] - B[i][j]) for i in range(2) for j in range(2))


A1 = ((2.0, 0.0), (0.0, 1.0))
A2 = ((1.0, 0.4), (0.4, 1.5))
B = ((0.3, 0.2), (0.2, -0.4))
T = madd(A1, A2)
I = ((1.0, 0.0), (0.0, 1.0))
assert abs(A1[0][0]*A2[0][1]-A2[0][1]*A1[1][1]) > 0.1


def sample(theta):
    return madd(B, madd(smul(-1.0/math.tan(theta/2), A1),
                       smul(-1.0/math.tan((theta-1.6)/2), A2)))


def resolvent(Y, w):
    return minv(madd(Y, smul(-w, I)))


n = 16384
for w in (-1j, 1.0-0.75j, -2.0-1.4j, 2.0-0.2j):
    total = ((0j, 0j), (0j, 0j))
    for k in range(n):
        theta = 2*PI*(k+0.5)/n
        total = madd(total, resolvent(sample(theta), w))
    total = smul(1/n, total)
    target = resolvent(madd(B, smul(1j, T)), w)
    error = diff(total, target)
    assert error < 4e-4, (w, error)

for t in (0.2, 0.7, 1.0, 3.0):
    for y in (-2.0, -0.5, 0.0, 0.5, 2.0):
        cdf_tail = 0.5-math.atan(y/t)/PI
        assert 0 < cdf_tail < 1
        if y == 0:
            assert cdf_tail == 0.5
    for p in (0.2, 0.4, 0.8):
        target = t**p/math.cos(PI*p/2)
        # Put |x|=t*exp(v); the exact logarithmic Cauchy density is 1/(pi*cosh(v)).
        m = 32000
        h = 320.0/m
        observed = t**p*h*sum(math.exp(p*(-160+(j+0.5)*h)) / (PI*math.cosh(-160+(j+0.5)*h)) for j in range(m))
        assert abs(observed-target)/target < 0.004, (t, p, observed, target)
print('PASS: 4 noncommuting matrix resolvent comparisons; Cauchy tails and 12 fractional-moment checks')
