"""Supplementary finite diagnostics for q-numerical ranges of antiunitaries on C^2.

Run: python3 checker.py (standard library only).
Analytical proof, rather than finite testing, establishes the theorem.
"""
import cmath
import math
import random
from fractions import Fraction as F


def endpoint(c, s, q, d):
    """c^2+s^2=q^2+d^2=1, all nonnegative."""
    low = max(F(0), d*s-q*c)
    high = F(1) if q <= c else q*c+d*s
    return low, high


def exact_tests():
    pairs = [(F(0), F(1)), (F(1), F(0)), (F(3, 5), F(4, 5)),
             (F(4, 5), F(3, 5)), (F(5, 13), F(12, 13)),
             (F(12, 13), F(5, 13)), (F(15, 17), F(8, 17))]
    count = 0
    for c, s in pairs:
        assert c*c+s*s == 1
        for q, d in pairs:
            assert q*q+d*d == 1
            lo, hi = endpoint(c, s, q, d)
            assert 0 <= lo <= hi <= 1
            assert (lo > 0) == (q < s)
            assert (hi == 1) == (q <= c)
            # At each feasible rational m, extrema lie between the sharp endpoints.
            for k in range(101):
                m = float(c) * k / 100
                u = float(q)*m
                v = float(d)*math.sqrt(1-m*m)
                assert abs(u-v) + 1e-12 >= float(lo)
                assert u+v <= float(hi)+1e-12
                count += 2
    assert endpoint(F(3,5),F(4,5),F(5,13),F(12,13)) == (F(33,65),F(1))
    assert endpoint(F(3,5),F(4,5),F(4,5),F(3,5)) == (F(0),F(24,25))
    return count


def randomized_pair_checks():
    rng=random.Random(47012)
    count=0
    for c,s in ((3/5,4/5),(4/5,3/5),(5/13,12/13),(12/13,5/13),(0,1),(1,0)):
        # A(z1,z2)=(c conjugate(z1)+s conjugate(z2),
        #             -s conjugate(z1)+c conjugate(z2)).
        for q in (0,1/5,3/5,4/5,12/13,1):
            d=math.sqrt(1-q*q)
            lo=max(0,d*s-q*c)
            hi=1 if q<=c else q*c+d*s
            for _ in range(600):
                x1=complex(rng.gauss(0,1),rng.gauss(0,1))
                x2=complex(rng.gauss(0,1),rng.gauss(0,1))
                scale=math.sqrt(abs(x1)**2+abs(x2)**2)
                x1/=scale;x2/=scale
                a1=c*x1.conjugate()+s*x2.conjugate()
                a2=-s*x1.conjugate()+c*x2.conjugate()
                v1=-x2.conjugate();v2=x1.conjugate()
                phase=cmath.exp(1j*rng.uniform(0,2*math.pi))
                y1=q*x1+d*phase*v1
                y2=q*x2+d*phase*v2
                # Inner product linear in first argument.
                assert abs((x1*y1.conjugate()+x2*y2.conjugate())-q)<3e-14
                radius=abs(a1*y1.conjugate()+a2*y2.conjugate())
                assert lo-3e-13 <= radius <= hi+3e-13
                count+=2
    return count


def main():
    n=exact_tests()+randomized_pair_checks()
    print(f"PASS: {n} supplementary exact/rational-bound and finite pair assertions")
    print("No finite test is used as a proof of the universal range classification.")

if __name__=='__main__':main()
