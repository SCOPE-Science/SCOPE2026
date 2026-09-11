"""Exact-arithmetic growth upper bounds for S3 totals and excursions. Stdlib only. Prints BOUNDS_OK."""
from fractions import Fraction
# Step polynomial S(x,y) = 1/(xy) + y + x + x/y.
def S(x, y):
    return Fraction(1, 1)/(x*y) + y + x + x/y
# (i) Excursions: e_n <= S(x,y)^n for ALL x,y > 0 (endpoint weight x^0 y^0 = 1 <= word sum).
xe, ye = Fraction(634, 1000), Fraction(1487, 1000)
Se = S(xe, ye)
print("S(0.634,1.487) =", Se, "=", float(Se))
assert Se < Fraction(361, 100), "excursion bound failed"
print("rho_exc <= S(0.634,1.487) < 3.61  (exact)")
# (ii) Totals: q_n <= S(x,y)^n for x,y >= 1 (confined endpoints have x^X y^Y >= 1).
xq, yq = Fraction(1, 1), Fraction(14142, 10000)
Sq = S(xq, yq)
print("S(1,1.4142) =", Sq, "=", float(Sq))
assert Sq < Fraction(7657, 2000), "total bound failed"
print("rho_tot <= S(1,1.4142) < 3.8285  (exact; cf. 1+2*sqrt(2) = 3.82842712...)")
print("BOUNDS_OK")
