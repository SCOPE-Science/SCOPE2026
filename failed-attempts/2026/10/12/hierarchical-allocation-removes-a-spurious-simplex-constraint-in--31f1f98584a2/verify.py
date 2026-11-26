from fractions import Fraction

a1 = Fraction(6242, 10000)
a2 = Fraction(8157, 10000)
assert a1 + a2 == Fraction(14399, 10000)
assert a1 + a2 > 1

for sigma in (Fraction(5521, 10000), Fraction(2, 5)):
    shares = (
        sigma * a1,
        sigma * (1 - a1),
        (1 - sigma) * a2,
        (1 - sigma) * (1 - a2),
    )
    assert all(x >= 0 for x in shares)
    assert sum(shares, Fraction(0, 1)) == 1

# Exact top-level shares for sigma=0.5521, one orientation of the reported between-group split.
sigma = Fraction(5521, 10000)
shares = [sigma*a1, sigma*(1-a1), (1-sigma)*a2, (1-sigma)*(1-a2)]
assert shares == [Fraction(17231041, 50000000), Fraction(10373959, 50000000), Fraction(36535203, 100000000), Fraction(8254797, 100000000)]
print('VERIFY_OK')
