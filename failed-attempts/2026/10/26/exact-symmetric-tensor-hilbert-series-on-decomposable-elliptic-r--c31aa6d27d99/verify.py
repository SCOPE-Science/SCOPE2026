"""Exact finite consistency checks for the symmetric-tensor Hilbert identity.

The geometric proof is in RESULT.md; finite cases do not prove it.
"""
from fractions import Fraction
from math import comb


def filtration_dimension(degree: int, power: int) -> int:
    return sum(sum(i * degree for i in range(1, j + 1))
               for j in range(1, power + 1))


def rr_euler(degree: int, power: int) -> Fraction:
    m, d = power, degree
    return (Fraction(d * m * (m + 1) * (2 * m + 1), 12)
            + Fraction(d * m * (m + 1), 4))


def hilbert_coeff(degree: int, power: int) -> int:
    return 1 + degree * comb(power + 2, 3) if power else 1


def main() -> None:
    cases = 0
    for d in range(1, 21):
        for m in range(0, 61):
            got = 1 + filtration_dimension(d, m)
            expected = hilbert_coeff(d, m)
            assert got == expected, (d, m, got, expected)
            assert rr_euler(d, m) == expected - 1, (d, m)
            cases += 1
    for d in (1, 2, 5, 7):
        assert [hilbert_coeff(d, m) for m in range(5)] == [
            1, d + 1, 4 * d + 1, 10 * d + 1, 20 * d + 1
        ]
    print(f"VERIFY_OK {cases} exact finite parameter checks")


if __name__ == '__main__':
    main()
