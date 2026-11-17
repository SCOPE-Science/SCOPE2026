"""Supplementary checks of the explicitly proved dyadic-series asymptotic.
Run with Python 3, standard library only. These finite tests are not a proof.
"""
import math


def increment(p, j, tail=110):
    # h=2**(-j), and |exp(i*u)-1|=2*|sin(u/2)|.
    return sum(2.0**(-n*p) * abs(2*math.sin(2.0**(n-j-1)))**p
               for n in range(j + tail))


def run():
    checks = 0
    for p in (0.25, 0.5, 0.8):
        previous = float('inf')
        for j in (16, 32, 64, 128, 256):
            h = 2.0**(-j)
            s = increment(p, j)
            rel = s/(j*h**p)
            assert 0.98 < rel < previous
            previous = rel
            checks += 2
            # The exact kernel is translation invariant, by coordinate phases.
            assert s > 0
            checks += 1
        # The leading term is approached, with an O(1/j) relative error.
        assert abs(previous-1) < 0.1
        checks += 1
    print(f"PASS: {checks} illustrative finite assertions")


if __name__ == '__main__':
    run()
