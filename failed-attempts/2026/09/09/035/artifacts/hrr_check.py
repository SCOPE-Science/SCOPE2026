"""HRR / Todd sanity check for lane-366 (cubic threefold Y in P^4).
Verifies c(T_Y) = 1+2H+4H^2-2H^3, td = 1+H+(2/3)H^2+(1/3)H^3,
and chi(O)=1, chi(O(1))=5, chi(O(-1))=0 via int_Y H^3 = 3.
Stdlib only (Fractions).
"""
from fractions import Fraction

a = [Fraction(1), Fraction(5), Fraction(10), Fraction(10)]   # (1+H)^5
b = [Fraction(1), Fraction(-3), Fraction(9), Fraction(-27)]  # 1/(1+3H)
c = [Fraction(0)] * 4
for i in range(4):
    for j in range(4):
        if i + j < 4:
            c[i + j] += a[i] * b[j]
assert c == [Fraction(1), Fraction(2), Fraction(4), Fraction(-2)], c
c1, c2, c3 = c[1], c[2], c[3]
td1 = c1 / 2
td2 = (c1 * c1 + c2) / 12
td3 = c1 * c2 / 24
assert (td1, td2, td3) == (Fraction(1), Fraction(2, 3), Fraction(1, 3))
for m, want in [(0, 1), (1, 5), (-1, 0)]:
    coeff = Fraction(m**3, 6) + Fraction(m**2, 2) * td1 + Fraction(m) * td2 + td3
    assert coeff * 3 == want, (m, coeff * 3)
print("HRR_OK c=", c, "td=", (td1, td2, td3))
