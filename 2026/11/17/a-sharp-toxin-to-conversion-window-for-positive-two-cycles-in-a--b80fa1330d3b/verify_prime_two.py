"""Exact rational checks for the Holling-II toxic-plankton two-cycle theorem.

Run: python3 verify_prime_two.py
These checks corroborate, but do not replace, the proof for all real parameters.
"""
from fractions import Fraction as F


def step(u, v, c, beta, theta, r):
    return (u * (2 - u) - u * v / (1 + c * u),
            v * (1 - r + beta * u / (1 + c * u) - theta * u))


def construct(c, q, a, b):
    assert c > 0 and 0 < a < b < a * (2 - a)
    y1 = (1 + c * a) * (2 - a - b / a)
    y2 = (1 + c * b) * (2 - b - a / b)
    k = y2 / y1
    Q = (1 + c * a) * (1 + c * b)
    assert y1 > 0 and y2 > 0 and k > 1 and q > 1/Q
    beta = (k - 1/k) / ((b - a) * (q - 1/Q))
    theta = q * beta
    r = 1 - k + a * beta * (1/(1 + c * a) - q)
    assert r > 0 and beta > 0 and theta > 0
    assert step(a, y1, c, beta, theta, r) == (b, y2)
    assert step(b, y2, c, beta, theta, r) == (a, y1)
    difference = (b-a)*(a+b-a*b+a*b*c*(3-a-b))/(a*b)
    assert y2 - y1 == difference
    assert F(1, (1+c)**2) < q < 1
    return beta, theta, r, y1, y2


def main():
    samples = 0
    for c in [F(1, 2), F(1), F(2), F(4)]:
        for a in [F(1, 4), F(1, 2), F(3, 4)]:
            lo = 1/(1+c*a)**2
            hi = 1/(1+c*a)
            for t in [F(1, 10), F(1, 2), F(9, 10)]:
                q = lo + t*(hi-lo)
                b = a + a*(1-a)/1000
                construct(c, q, a, b)
                samples += 1
    c = F(1)
    a = F(1, 2)
    b = F(3, 5)
    q = F(1, 2)
    beta, theta, r, v1, v2 = construct(c, q, a, b)
    assert (beta,theta,r,v1,v2) == (
        F(55759,306),F(55759,612),F(28907,2040),F(9,20),F(68,75))
    print('TOXIC_PLANKTON_TWO_CYCLE_EXACT_OK generic_samples=%d rational_witness=1' % samples)


if __name__ == '__main__':
    main()
