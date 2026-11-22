"""Independent cyclotomic coefficient checks, without modular arithmetic.

Verifies all binary-obstruction certificates by a seven-term coefficient
expansion of the 7x7 determinant. Also spot-checks ternary full-spark
minors using the 7x3 coefficient representation in Z[zeta_7,eta_3].
"""
import csv
import itertools
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
PERMS = tuple(itertools.permutations(range(7)))
SIGNS = []
for p in PERMS:
    inversions = sum(p[i] > p[j] for i in range(7) for j in range(i+1, 7))
    SIGNS.append(-1 if inversions % 2 else 1)


def determinant_coefficients(indices, exps, order):
    """Group-algebra polynomial indexed by powers of zeta_7 and eta_order."""
    columns = [(c // 7, c % 7) for c in indices]
    coef = [[0] * order for _ in range(7)]
    for perm, sgn in zip(PERMS, SIGNS):
        zpower = 0
        phasepower = 0
        for x, col in enumerate(perm):
            a, b = columns[col]
            zpower += b * x
            phasepower += exps[(x - a) % 7]
        coef[zpower % 7][phasepower % order] += sgn
    return coef


def cyclotomic_zero(coef, phase_order):
    # Modulo Phi_7(z)=1+z+...+z^6, then Phi_2(t)=1+t
    # or Phi_3(t)=1+t+t^2 as appropriate.
    for z in range(6):
        diff = [coef[z][v] - coef[6][v] for v in range(phase_order)]
        if any(diff[v] != diff[0] for v in range(1, phase_order)):
            return False
    return True


def main():
    rows = list(csv.DictReader((HERE/'binary_witnesses.csv').open()))
    assert len(rows) == 64
    for row in rows:
        mask = int(row['mask'])
        exps = [0] + [(mask >> (i-1)) & 1 for i in range(1,7)]
        inds = [int(row[f'c{i}']) for i in range(7)]
        assert len(set(inds)) == 7 and inds[0] == 0
        cf = determinant_coefficients(inds, exps, 2)
        assert cyclotomic_zero(cf, 2), (mask, inds, cf)
    print('PASS 64 binary exact cyclotomic determinant certificates')

    rng = random.Random(71998)
    exps = [0,1,1,0,1,0,0]
    for i in range(300):
        inds = [0] + sorted(rng.sample(range(1,49),6))
        cf = determinant_coefficients(inds, exps, 3)
        assert not cyclotomic_zero(cf, 3), (i, inds)
    print('PASS 300 independent exact integer-ring ternary spot checks')


if __name__ == '__main__':
    main()
