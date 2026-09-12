"""Exact rational Pisot certificate for the Schaad 7-fold inflation factor.

Claim: lambda = 2+2cos(pi/7)+2cos(2pi/7) = 5.0489173395223... is the largest
root of p(x) = x^3 - 6x^2 + 5x - 1, and is a Pisot (PV) number.

Method: exact Fraction sign evaluations only (no floating-point root finding
used for the certificate). Irreducibility: degree 3 with p(1)=-1, p(-1)=-13,
so no rational root, hence irreducible over Q. Three disjoint rational
brackets each contain exactly one root (degree 3):
  (5, 5.05), (0.3, 0.31), (0.64, 0.65).
The two small roots lie strictly inside the unit disc, so lambda is Pisot.

Replay: python3 pisot_check.py  ->  PISOT_CERTIFIED (stdlib only).
"""
from fractions import Fraction


def p(x: Fraction) -> Fraction:
    return x**3 - 6*x**2 + 5*x - 1


def main() -> None:
    checks = [
        ("p(1)", p(Fraction(1)), -1),
        ("p(-1)", p(Fraction(-1)), -13),
        ("p(5)", p(Fraction(5)), -1),
        ("p(5.05)", p(Fraction(101, 20)), 181),
        ("p(0.3)", p(Fraction(3, 10)), -13),
        ("p(0.31)", p(Fraction(31, 100)), 3191),
        ("p(0.64)", p(Fraction(16, 25)), 71),
        ("p(0.65)", p(Fraction(13, 20)), -83),
    ]
    ok = True
    for name, val, num in checks:
        # check sign matches expectation via sign of numerator
        exp_neg = (num < 0)
        is_neg = (val < 0)
        status = "OK" if (exp_neg == is_neg and val != 0) else "FAIL"
        if status == "FAIL":
            ok = False
        print(f"{name} = {val}  sign_ok={status}")
    brackets = [
        (Fraction(5), Fraction(101, 20)),
        (Fraction(3, 10), Fraction(31, 100)),
        (Fraction(16, 25), Fraction(13, 20)),
    ]
    for a, b in brackets:
        pa, pb = p(a), p(b)
        if pa == 0 or pb == 0 or (pa < 0) == (pb < 0):
            print(f"bracket ({a},{b}): FAIL (no sign change)")
            ok = False
        else:
            print(f"bracket ({a},{b}): sign change OK")
    # disjointness + unit-disc containment of the two small brackets
    assert Fraction(13, 20) < 1, "small roots inside unit disc"
    assert Fraction(101, 20) > 1, "large root > 1"
    print("PISOT_CERTIFIED" if ok else "CERTIFICATE_FAILED")


if __name__ == "__main__":
    main()
