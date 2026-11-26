"""Exact-rational tests for circle Poisson covariance knot interpolation.

Run with python3 checker.py. These finite tests supplement, rather than replace,
the all-degree recurrence proof in RESULT.md.
"""
from fractions import Fraction as F
from random import Random


def fourier(c, r, k, n):
    """Fourier coefficient of P_r(theta) sum_{j=-d}^d c_j exp(i*j*k*theta)."""
    d = len(c) - 1
    return c[0] * r ** abs(n) + sum(
        c[j] * (r ** abs(n - j*k) + r ** abs(n + j*k))
        for j in range(1, d+1))


def from_knots(knots, r, k):
    d = len(knots) - 1
    R = r**k
    den = 1-R*R
    c = [((1+R*R)*knots[0] - 2*R*knots[1])/den]
    for j in range(1,d):
        c.append(((1+R*R)*knots[j] - R*(knots[j-1]+knots[j+1]))/den)
    c.append((knots[d]-R*knots[d-1])/den)
    return c


def interpolant(knots, r, k, n):
    n=abs(n)
    d=len(knots)-1
    if n>=d*k:
        return knots[d]*r**(n-d*k)
    j,s=divmod(n,k)
    A=(r**s-r**(2*k-s))/(1-r**(2*k))
    B=(r**(k-s)-r**(k+s))/(1-r**(2*k))
    return A*knots[j]+B*knots[j+1]


def ray_support(j,d,k,n):
    n=abs(n)
    if j==d:
        return n>(d-1)*k
    if j==0:
        return n<k
    return (j-1)*k<n<(j+1)*k


def main():
    rng=Random(20261117)
    count=0
    for r in (F(1,3),F(2,5),F(3,4)):
        for k in range(1,6):
            for d in range(1,7):
                for j in range(d+1):
                    knots=[F(int(j==v)) for v in range(d+1)]
                    c=from_knots(knots,r,k)
                    for m in range(d+1):
                        assert fourier(c,r,k,m*k)==knots[m]
                        count+=1
                    for n in range(-2*d*k-3,2*d*k+4):
                        val=fourier(c,r,k,n)
                        assert val==interpolant(knots,r,k,n)
                        assert (val>0)==ray_support(j,d,k,n)
                        count+=2
                for _ in range(5):
                    coeffs=[F(rng.randint(-8,8),rng.randint(1,9)) for i in range(d+1)]
                    knots=[fourier(coeffs,r,k,m*k) for m in range(d+1)]
                    assert coeffs==from_knots(knots,r,k)
                    count+=1
                    for n in range(-d*k-4,d*k+5):
                        assert fourier(coeffs,r,k,n)==interpolant(knots,r,k,n)
                        count+=1
    # Explicit signed modifier with a single pair of positive Fourier atoms:
    r=F(2,5)
    c=from_knots([F(0),F(0),F(1),F(0)],r,1)
    assert [fourier(c,r,1,n) for n in range(8)]==[F(0),F(0),F(1)]+[F(0)]*5
    assert any(x<0 for x in c)
    count+=2
    print(f'PASS: {count} exact-rational assertions')

if __name__=='__main__':
    main()
