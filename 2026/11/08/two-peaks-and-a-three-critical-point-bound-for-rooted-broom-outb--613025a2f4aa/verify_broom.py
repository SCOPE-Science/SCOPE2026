"""Exact rational checks for rooted-broom bond-percolation cluster variance.

Run: python3 verify_broom.py
Only the Python standard library is required.
The proof of the infinite assertions is in RESULT.md; this script supplies
independent finite-instance checks, not an exhaustive infinite proof.
"""
from fractions import Fraction
from itertools import product


def coefficients(m, L):
    """Ascending coefficients of the variance polynomial."""
    c = [0] * (2 * L + 1)
    c[1] += m
    c[2] -= m
    for k in range(1, L + 1):
        c[k] += k
    for k in range(L + 1, 2 * L + 1):
        c[k] -= 2 * L + 1 - k
    return c


def evaluate(coeff, p):
    return sum(v * p**k for k, v in enumerate(coeff))


def derivative_coeff(coeff):
    return [k * coeff[k] for k in range(1, len(coeff))]


def independent_moments(m, L, p):
    mean_path = sum(p**j for j in range(1, L + 1))
    second_path = sum((2*j - 1) * p**j for j in range(1, L + 1))
    return m*p*(1-p) + second_path - mean_path**2


def enumerate_edges(m, L, p):
    edges = m + L
    expected = Fraction(0)
    expected_sq = Fraction(0)
    for outcomes in product([0, 1], repeat=edges):
        q = sum(outcomes)
        weight = p**q * (1-p)**(edges-q)
        leaves = sum(outcomes[:m])
        path = 0
        for is_open in outcomes[m:]:
            if not is_open:
                break
            path += 1
        size = 1 + leaves + path
        expected += weight * size
        expected_sq += weight * size**2
    return expected_sq - expected**2


def tail_derivative(L, p):
    """Derivative of variance for a single length-L run."""
    return sum(k*k*p**(k-1) for k in range(1, L + 1)) - sum(
        k*(2*L + 1-k)*p**(k-1) for k in range(L+1, 2*L+1)
    )


def main():
    cases = 0
    for m in range(0, 5):
        for L in range(1, 6):
            c = coefficients(m, L)
            d = derivative_coeff(c)
            for p in (Fraction(0), Fraction(1, 4), Fraction(1, 3),
                      Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(1)):
                assert evaluate(c, p) == independent_moments(m, L, p)
                if p != 1:
                    closed = p/(1-p)**2-(2*L+1)*p**(L+1)/(1-p)-p**(2*L+2)/(1-p)**2
                    assert evaluate(c, p) == closed + m*p*(1-p)
                assert evaluate(d, p) == m*(1-2*p)+tail_derivative(L, p)
                cases += 1
            assert evaluate(d, Fraction(0)) == m+1
            assert evaluate(d, Fraction(1)) == -m-L*(L+1)*(2*L+1)//6
    enumerated = 0
    for m in (0, 1, 2, 3):
        for L in (1, 2, 3, 4):
            for p in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
                assert enumerate_edges(m, L, p) == evaluate(coefficients(m, L), p)
                enumerated += 1
    assert Fraction(3, 4)**14 < Fraction(1, 56)
    assert Fraction(9, 16)**14 < Fraction(1, 3000)
    assert 4*29*18/Fraction(56) + 24*18/Fraction(3000) < Fraction(75, 2)
    # The correction functions at p=3/4 decrease from L=14 onward.
    for L in range(14, 151):
        a = 4*(2*L+1)*(L+4)*Fraction(3, 4)**L
        a_next = 4*(2*L+3)*(L+5)*Fraction(3, 4)**(L+1)
        b = 24*(L+4)*Fraction(9, 16)**L
        b_next = 24*(L+5)*Fraction(9, 16)**(L+1)
        assert a_next < a and b_next < b
    boundary_checks = 0
    for L in (14, 15, 16, 20, 30, 60):
        for m in range(136, 150):
            d = derivative_coeff(coefficients(m, L))
            assert evaluate(d, Fraction(0)) > 0
            assert evaluate(d, Fraction(2, 3)) < 0
            assert evaluate(d, Fraction(3, 4)) > 0
            assert evaluate(d, Fraction(1)) < 0
            signs = [1 if c > 0 else -1 for c in reversed(d) if c]
            assert sum(signs[i] != signs[i-1] for i in range(1, len(signs))) == 3
            boundary_checks += 1
    print('PASS: exact moment/polynomial/derivative identities:', cases)
    print('PASS: independent edge-mask checks:', enumerated)
    print('PASS: rational endpoint/monotonic-correction inequalities')
    print('PASS: derivative sign brackets and Descartes coefficient patterns:', boundary_checks)


if __name__ == '__main__':
    main()
