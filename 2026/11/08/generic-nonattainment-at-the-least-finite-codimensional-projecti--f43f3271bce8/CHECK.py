"""Exact rational diagnostics for the explicit near-minimal projections.

These finite checks do not replace the proofs for all real parameters,
all compact spaces, or Baire-category conclusions.
"""
from fractions import Fraction as F


def g(t, x):
    t, x = F(t), F(x)
    c = 2*t/(2*t-1)
    g1 = c*min(t*x, F(1))
    g2 = max(F(1)-t*x, F(0)) - g1/(2*t)
    return g1, g2


def triangle_integral(heights, ends):
    return sum((heights[i]+heights[i+1])*(ends[i+1]-ends[i])/2
               for i in range(len(ends)-1))


def run():
    assertions = 0
    for t in range(2, 1002):
        tt = F(t)
        c = 2*tt/(2*tt-1)
        x0, x1, x2 = F(0), F(1, t), F(1)
        v0, v1, v2 = [g(t, x) for x in (x0, x1, x2)]
        assert v0 == (F(0), F(1)); assertions += 1
        assert v1 == (c, -c/(2*tt)); assertions += 1
        assert v2 == v1; assertions += 1
        assert triangle_integral([v0[0],v1[0],v2[0]],[x0,x1,x2]) == 1; assertions += 1
        assert triangle_integral([v0[1],v1[1],v2[1]],[x0,x1,x2]) == 0; assertions += 1
        expected_norm = (2*tt+1)/(2*tt-1)
        assert sum(map(abs,v1)) == expected_norm; assertions += 1
        # The sum of absolute affine functions is convex on each piece,
        # so its maximum is at one of the three tested endpoints.
        assert max(sum(map(abs,v)) for v in (v0,v1,v2)) == expected_norm; assertions += 1
        lip1 = (v1[0]-v0[0])/(x1-x0)
        lip2 = abs((v1[1]-v0[1])/(x1-x0))
        assert lip1 == lip2 == tt + tt/(2*tt-1); assertions += 1
        eps = expected_norm - 1
        assert eps == F(2,2*t-1); assertions += 1
        assert eps*lip1 > F(1); assertions += 1
        assert eps*lip1 < F(2); assertions += 1
    print(f"Exact rational assertions passed: {assertions}")


if __name__ == '__main__':
    run()
