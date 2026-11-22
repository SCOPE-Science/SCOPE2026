"""Finite exact-arithmetic consistency checks for the two-clock escape theorem.

No finite test establishes the asymptotic theorem; the induction in RESULT.md does.
Execute with: python checker.py
"""
from fractions import Fraction
from math import log

cases = [
    (Fraction(1, 1), Fraction(1, 10)),
    (Fraction(-3, 2), Fraction(-1, 7)),
    (Fraction(11, 3), Fraction(5, 4)),
]
R = 10 ** 5
q_exponents = [4, 5, 8, 11]  # x2=10^4,10^5,10^8,10^11 => q=.8,1,1.6,2.2
checks = 0
for a, b in cases:
    for power in q_exponents:
        x0 = Fraction(R)
        x1 = Fraction(R)
        x2 = Fraction(10 ** power)
        y0 = (a - x0*x0 - x2)/b
        z0 = (a - y0*y0 - x1)/b
        state = (x0, y0, z0)
        seq = [x0, x1, x2]
        assert (a - y0*y0 - b*z0) == x1
        assert (a - x0*x0 - b*y0) == x2
        for n in range(3, 14):
            seq.append(a - seq[-2]**2 - b*seq[-3])
        for n in range(14):
            assert state[0] == seq[n]
            if n >= 2:
                assert state == (seq[n], seq[n-1], seq[n-2])
            if n >= 3:
                assert seq[n] < 0
            xx, yy, zz = state
            state = (a - yy*yy - b*zz, xx, yy)
            checks += 1
        # Partial normalized logarithmic heights should be close to their seeds.
        log_fraction = lambda f: log(abs(f.numerator))-log(f.denominator)
        odd = [log_fraction(seq[2*m+1])/(2**m) for m in range(6)]
        even = [log_fraction(seq[2*m+2])/(2**m) for m in range(6)]
        assert all(abs(h-log(R)) < 0.02*log(R) for h in odd)
        assert all(abs(h-log(10**power)) < 0.02*log(R) for h in even)
        checks += 12
print(f"PASS: {checks} exact-orbit/height consistency checks across {len(cases)*len(q_exponents)} cases")
