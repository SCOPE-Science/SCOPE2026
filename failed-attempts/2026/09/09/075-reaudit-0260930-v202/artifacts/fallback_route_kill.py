"""Lane 434: fallback-route kill arithmetic (both legs), exact integers/Fractions.
1. theta': theta'(C7)>=82827/25000 (exact LDL in verify.py); theta'(C7^4)>=theta'(C7)^4
   by Kronecker squaring of the same witness (exact), and that exceeds 114.
2. Haemers: H_f(C7;F)=7/2 exact (see DRAFT), so H_f(C7^4;F)=(7/2)^4=2401/16>114;
   any rank cert is >= H_f hence cannot reach 114. Integer cross-checks included.
Stdlib only. Prints VERIFY_OK.
"""
from fractions import Fraction


def main():
    t = Fraction(82827, 25000)
    assert t ** 4 > 114
    assert 82827 ** 4 > 114 * 25000 ** 4
    print("theta'(C7)^4 >= (82827/25000)^4 = 47063879763179701041/390625000000000000")
    print("   = %.6f > 114 EXACT" % float(t ** 4))
    h = Fraction(7, 2)
    assert h ** 4 > 114
    assert 2401 > 114 * 16
    print("H_f(C7^4) = (7/2)^4 = 2401/16 = 150.0625 > 114 EXACT")
    print("fallback-route kill (both legs) verified")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
