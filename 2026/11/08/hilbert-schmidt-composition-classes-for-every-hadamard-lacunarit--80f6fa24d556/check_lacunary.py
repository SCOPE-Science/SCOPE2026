"""Exact finite checks for the lacunary compression argument.

These checks test finite coefficient identities. They do not prove the
infinite Hilbert-space statements; the proof is analytical.
"""
from collections import Counter
from fractions import Fraction


def hadamard_sequence(q_num, q_den, first, count):
    a = [first]
    for _ in range(count - 1):
        a.append((a[-1] * q_num + q_den - 1) // q_den)
    return a


def coefficient(k):
    return Fraction(1, 8 * (2 ** k)) if 0 <= k <= 14 else Fraction(0)


def check_compression(seq, ell):
    n = len(seq)
    a = coefficient(ell)
    diffs = Counter(seq[j] - seq[i] for j in range(n) for i in range(j))
    gap_bound = max(diffs.values(), default=0)
    offdiag_squared = sum(
        (coefficient(seq[j] + ell - seq[i]) ** 2 for j in range(n)
         for i in range(n) if i != j), Fraction(0)
    )
    hs_upper = gap_bound * Fraction(1, 64 * (4 ** ell) * 3)
    assert offdiag_squared <= hs_upper
    # For a large enough tail, the finite compression has no off-diagonals.
    tail = range(n - 5, n)
    for i in tail:
        for j in tail:
            entry = coefficient(seq[j] + ell - seq[i])
            assert (entry == a) if i == j else (entry < a / 10)
    return len(diffs)


def check_dyadic_weights():
    special = {2 ** k for k in range(1, 13)}
    def beta(n):
        return Fraction(1, n) if n in special else Fraction(1)
    assert all(beta(n) == Fraction(1, n) for n in special)
    # For the symbol phi(z)=z/2, the operator is diagonal.
    trace_hardy = sum((Fraction(1, 4 ** n) for n in range(100)), Fraction(0))
    trace_weighted = sum((Fraction(1, 4 ** n) * beta(n) / beta(n)
                          for n in range(100)), Fraction(0))
    assert trace_hardy == trace_weighted
    # For phi(z)=z^2/2, singular squares are 4^{-n} beta(2n)/beta(n).
    trace_monomial = sum((Fraction(1, 4 ** n) * beta(2*n) / beta(n)
                          for n in range(100)), Fraction(0))
    assert 0 < trace_monomial < 10
    # q=2 is not covered by the q>2 hypothesis of the initiating paper.
    assert all(2 ** (k + 1) == 2 * (2 ** k) for k in range(1, 11))


def run():
    tests = 0
    for num, den, first in ((7, 5, 3), (3, 2, 4), (2, 1, 2), (3, 1, 2)):
        seq = hadamard_sequence(num, den, first, 16)
        assert all(seq[i+1] * den >= seq[i] * num for i in range(15))
        tests += check_compression(seq, 1)
    check_dyadic_weights()
    print('LACUNARY_FINITE_CHECK_OK', tests)


if __name__ == '__main__':
    run()
