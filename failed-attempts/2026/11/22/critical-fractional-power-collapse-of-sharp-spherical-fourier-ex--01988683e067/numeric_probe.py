#!/usr/bin/env python3
"""Finite numerical consistency checks; not an infinite proof."""
import numpy as np
from scipy.special import jv
from scipy.integrate import quad
from scipy.optimize import brentq


def positive_cells(d, count=6):
    nu = d / 2 - 1
    qc = 2 * d / (d - 1)
    def moment_difference(r):
        if r == 0:
            return 0.0
        return r ** (d - 1 - nu * qc) * (
            abs(jv(nu, r)) ** qc - abs(jv(nu + 1, r)) ** qc)
    grid = np.arange(0.01, (count + 3) * np.pi + nu * np.pi / 2, 0.025)
    values = jv(nu + 1, grid)
    roots = [brentq(lambda x: jv(nu + 1, x), grid[i], grid[i + 1])
             for i in range(len(grid) - 1) if values[i] * values[i + 1] < 0][:count]
    assert len(roots) == count
    previous_root = 0.0
    cumulative = 0.0
    partials = []
    for root in roots:
        cell, err = quad(moment_difference, previous_root, root, limit=250,
                         epsabs=1e-10, epsrel=1e-10)
        assert cell > 0.0, (d, previous_root, root, cell, err)
        cumulative += cell
        partials.append(cumulative)
        previous_root = root
    assert all(y > x for x, y in zip(partials, partials[1:]))
    return partials


if __name__ == '__main__':
    for dimension in (3, 4, 5):
        partials = positive_cells(dimension)
        print(f'd={dimension}: six positive-cell cumulative integrals:',
              [round(x, 8) for x in partials])
    print('Finite consistency checks passed; the analytical proof controls the infinite tails.')
