"""Independent labelled-state voter-chain check of no-hub-flip probabilities.

The generator is assembled directly from vertex-neighbor copying, not from a
birth-death aggregation. Run: python verification/check_full_state.py
Dependencies: numpy and scipy.
"""
from itertools import combinations_with_replacement
from math import isclose
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve


def direct_hub_survival(blades):
    L = sum(blades)
    full = (1 << L) - 1
    positions = []
    cursor = 0
    for r in blades:
        positions.append(tuple(range(cursor, cursor + r)))
        cursor += r
    row = []
    col = []
    vals = []
    right = np.zeros(full)
    for state in range(full):
        exit_rate = (L - state.bit_count()) / L  # hub copying zero
        for r, members in zip(blades, positions):
            for v in members:
                old = (state >> v) & 1
                neighbors = [w for w in members if w != v]
                # Each non-hub vertex has r neighbors, including the hub (bit 1).
                opposing = (sum(1 - ((state >> w) & 1) for w in neighbors)
                            if old else 1 + sum((state >> w) & 1 for w in neighbors))
                rate = opposing / r
                if rate == 0:
                    continue
                exit_rate += rate
                dest = state ^ (1 << v)
                if dest == full:
                    right[state] += rate
                else:
                    row.append(state)
                    col.append(dest)
                    vals.append(-rate)
        row.append(state)
        col.append(state)
        vals.append(exit_rate)
    matrix = csr_matrix((vals, (row, col)), shape=(full, full))
    x = spsolve(matrix, right)
    assert np.max(x) < 1 + 1e-10 and np.min(x) > -1e-10
    return float(x[0])


def analytic_hub_survival(blades):
    # Independent rational closed forms are available for blade sizes 1, 2, 3.
    from fractions import Fraction
    L = sum(blades)
    t = Fraction(1, L)
    f = {
        1: 1 / (1 + t),
        2: 1 / (1 + 4 * t + 2 * t * t),
        3: 2 / (2 + 18 * t + 27 * t*t + 9 * t*t*t),
    }
    result = Fraction(1)
    for r in blades:
        result *= f[r]
    return result


def main():
    cases = 0
    for L in range(1, 9):
        for k in range(1, L + 1):
            for blades in combinations_with_replacement((1, 2, 3), k):
                if sum(blades) != L:
                    continue
                actual = direct_hub_survival(blades)
                expected = analytic_hub_survival(blades)
                assert isclose(actual, float(expected), rel_tol=0, abs_tol=4e-12), (blades, actual, expected)
                print('sizes', list(blades), 'full-state', format(actual, '.12f'),
                      'exact', expected)
                cases += 1
    assert cases >= 20
    print('LABELLED MICROSTATE CHECKS PASS; case_count', cases)


if __name__ == '__main__':
    main()
