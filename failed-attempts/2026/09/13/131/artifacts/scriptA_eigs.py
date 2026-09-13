"""Script A: exact eigenvalue enclosures for A_star via Fraction bisection.
q(t) = t^3 - 5t^2 + 6t - 1 (integer coefficients -> exact rational arithmetic)."""
from fractions import Fraction as F

def q(t):
    return t*t*t - 5*t*t + 6*t - 1

# bracket roots: (0,1), (1,2), (3,4) since q(0)=-1,q(1)=1,q(2)=-1? check: 8-20+12-1=-1 yes; q(3)=27-45+18-1=-1, q(4)=64-80+24-1=7
brackets = [(F(0), F(1)), (F(1), F(2)), (F(3), F(4))]
print("endpoint signs:", [(float(q(a)), float(q(b))) for a, b in brackets])
for lo, hi in brackets:
    assert q(lo) * q(hi) < 0, (lo, hi)
    for _ in range(80):
        mid = (lo + hi) / 2
        if q(lo) * q(mid) <= 0:
            hi = mid
        else:
            lo = mid
    print(f"root in [{float(lo):.12f}, {float(hi):.12f}]  width={float(hi-lo):.3e}")
    print(f"   exact rationals: lo={lo} hi={hi}")
# det check: product of roots = 1 (constant term -1, monic cubic -> prod = 1)
print("det(A) exact:", 2*(2*1-1*1) - 1*(1*1-0*1) + 0)  # cofactor expansion row 1
print("char poly coeffs (t^3 -5t^2 +6t -1): trace =", 2+2+1)
