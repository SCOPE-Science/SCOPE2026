"""Exact rational checks for finite screened-path landmark design claims.

Run: python verify_path_design.py
Python 3, standard library only. These finite checks complement, not replace,
the all-order analytic inequalities in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations


def continuant(size, shift, endpoint=False):
    """Return (determinant, derivative w.r.t. shift) exactly."""
    one = Fraction(1)
    if size == 0:
        return one, Fraction(0)
    older, derivative_older = one, Fraction(0)
    newer, derivative_newer = shift + (1 if endpoint else 2), one
    for _ in range(2, size + 1):
        now = (shift + 2) * newer - older
        derivative_now = newer + (shift + 2) * derivative_newer - derivative_older
        older, derivative_older = newer, derivative_newer
        newer, derivative_newer = now, derivative_now
    return newer, derivative_newer


def criterion(n, shift, selected):
    boundaries = (-1,) + tuple(selected) + (n,)
    gaps = [boundaries[j + 1] - boundaries[j] - 1 for j in range(len(boundaries) - 1)]
    determinant = Fraction(1)
    error = Fraction(0)
    for j, gap in enumerate(gaps):
        d, derivative = continuant(gap, shift, endpoint=(j == 0 or j == len(gaps) - 1))
        determinant *= d
        error += derivative / d
    return determinant, error


def eliminate_exact(A):
    """Gauss-Jordan inverse with exact rational operations."""
    n = len(A)
    b = [[Fraction(A[i][j]) for j in range(n)] + [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if b[j][i])
        b[i], b[pivot] = b[pivot], b[i]
        d = b[i][i]
        b[i] = [v / d for v in b[i]]
        for j in range(n):
            if j != i:
                d = b[j][i]
                if d:
                    b[j] = [v - d * w for v, w in zip(b[j], b[i])]
    return [row[n:] for row in b]


def determinant_exact(A):
    n = len(A)
    b = [[Fraction(v) for v in row] for row in A]
    determinant = Fraction(1)
    for i in range(n):
        pivot = next((j for j in range(i, n) if b[j][i]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != i:
            b[i], b[pivot] = b[pivot], b[i]
            determinant = -determinant
        value = b[i][i]
        determinant *= value
        for j in range(i + 1, n):
            factor = b[j][i] / value
            for k in range(i + 1, n):
                b[j][k] -= factor * b[i][k]
    return determinant


def dense_a(n, shift):
    return [[shift + (1 if i in (0, n - 1) else 2) if i == j
             else Fraction(-1) if abs(i-j) == 1 else Fraction(0)
             for j in range(n)] for i in range(n)]


def balanced(n, k, selected):
    if not (selected[0] == 0 and selected[-1] == n-1):
        return False
    gaps = [selected[i+1]-selected[i]-1 for i in range(k-1)]
    return max(gaps, default=0)-min(gaps, default=0) <= 1


def main():
    count = 0
    # Independent Schur complement and Jacobi determinant checks.
    for n in range(3, 8):
        for shift in (Fraction(1,4), Fraction(1,2), Fraction(2)):
            A = dense_a(n, shift)
            G = eliminate_exact(A)
            determinant_a = determinant_exact(A)
            for k in range(2, n+1):
                for S in combinations(range(n), k):
                    U = [i for i in range(n) if i not in S]
                    product, expected_error = criterion(n, shift, S)
                    GU = [[G[i][j] for j in S] for i in S]
                    assert determinant_exact(GU) * determinant_a == product
                    count += 1
                    if U:
                        Kss_inv = eliminate_exact(GU)
                        computed_error = sum(G[i][i] - sum(G[i][s] * Kss_inv[j][r] * G[S[r]][i]
                                          for j, s in enumerate(S) for r in range(k)) for i in U)
                        assert computed_error == expected_error
                        count += 1
                    else:
                        assert expected_error == 0
                        count += 1
    # Exhaustive exact optimization over all landmark sets.
    for n in range(3, 12):
        for shift in (Fraction(1,10), Fraction(1,4), Fraction(1,2), Fraction(1), Fraction(3)):
            for k in range(2, n + 1):
                choices = {S: criterion(n, shift, S) for S in combinations(range(n), k)}
                max_det = max(v[0] for v in choices.values())
                argmax_det = {S for S, v in choices.items() if v[0] == max_det}
                expected = {S for S in choices if balanced(n, k, S)}
                assert argmax_det == expected, (n, shift, k, 'determinant')
                count += len(choices)
                if shift >= Fraction(1,2):
                    min_error = min(v[1] for v in choices.values())
                    argmin_error = {S for S, v in choices.items() if v[1] == min_error}
                    assert argmin_error == expected, (n, shift, k, 'trace')
                    count += len(choices)
    # A concrete exact objective conflict with a reproducible rational gap.
    n, mu, k = 6, Fraction(1,4), 2
    end = criterion(n, mu, (0,5))[1]
    interior = criterion(n, mu, (1,4))[1]
    assert end - interior == Fraction(18016,190385) > 0
    count += 1
    print('PASS: %d exact rational matrix and partition assertions' % count)
    print('n=6, shift=1/4, k=2: endpoint error %s, inward error %s, gap %s' % (end,interior,end-interior))


if __name__ == '__main__':
    main()
