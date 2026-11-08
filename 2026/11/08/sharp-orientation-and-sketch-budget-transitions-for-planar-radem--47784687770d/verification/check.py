"""Independent finite checks for the planar best-of-m Rademacher Nystrom law.
Run with Python 3; uses only standard-library modules. These finite tests support,
but do not replace, the analytic proof for all real parameters.
"""
from fractions import Fraction
from math import cos, sin, pi, sqrt, isclose, log2, ceil

checks = 0
# Exact rational convexity endpoint inequality at 101 grid points for 29
# spectral ratios and 11 candidate counts; every rational operation exact.
for k in range(2, 31):
    for m in range(1, 12):
        p = Fraction(1, 2 ** m)
        low_axis = Fraction(2*k, k+1)
        high_sign = 1 + Fraction(k-1, 2 ** m)
        bound = max(low_axis, high_sign)
        assert (high_sign >= low_axis) == (k+1 >= 2**m)
        checks += 1
        for j in range(101):
            t = Fraction(j,100)
            f = 2*k*((1-p)/((k+1)+(k-1)*t) + p/((k+1)-(k-1)*t))
            assert f <= bound
            checks += 1
        # The best-of-m vs one-Gaussian threshold can be squared without error.
        threshold = 2**m >= 1 + sqrt(k)
        assert (float(bound) <= sqrt(k)+1e-12) == threshold
        checks += 1

# Matrix-level check independent of the Cayley--Hamilton simplification.
for k in (1,2,5,20,100):
    for theta in (0., pi/12, pi/8, pi/4):
        c,s=cos(theta),sin(theta)
        A11 = k*c*c+s*s
        A22 = k*s*s+c*c
        A12 = (k-1)*s*c
        residuals=[]
        for z in (1,-1):
            # w=(1,z), A w=(u,v)
            u = A11 + z*A12
            v = A12 + z*A22
            den = u + z*v
            B11=A11-u*u/den
            B22=A22-v*v/den
            B12=A12-u*v/den
            assert B11 >= -1e-12 and B22 >= -1e-12
            assert abs(B11*B22-B12*B12) <= 1e-8
            residuals.append(B11+B22)
            checks += 2
        t=abs(sin(2*theta))
        lo=2*k/(k+1+(k-1)*t)
        hi=2*k/(k+1-(k-1)*t)
        assert isclose(min(residuals),lo,abs_tol=1e-10)
        assert isclose(max(residuals),hi,abs_tol=1e-10)
        checks += 2
        for m in (1,2,4,8):
            p=2**(-m)
            assert isclose(lo+(hi-lo)*p, lo*(1-p)+hi*p, abs_tol=1e-12)
            checks += 1

# Independent numerical circle integration of the one-Gaussian benchmark.
for k in (1,2,7,20,100):
    N=20000
    total=0.0
    for j in range(N):
        angle=2*pi*(j+0.5)/N
        total+=k/(k*cos(angle)**2+sin(angle)**2)
    mean=total/N
    assert isclose(mean,sqrt(k),rel_tol=2e-9,abs_tol=2e-9)
    checks += 1

print('PASS:',checks,'assertions; exact rational, direct matrix and angular-integral checks')
