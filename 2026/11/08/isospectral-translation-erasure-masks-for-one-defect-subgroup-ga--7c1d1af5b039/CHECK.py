#!/usr/bin/env python3
"""Independent dense-matrix checks of finite Gabor frame erasure formulas.

Requires Python 3 and NumPy. These tests are finite evidence, not the proof.
"""
import itertools
import math
import numpy as np


def direct_spectrum(m, q, removed, z):
    n = m*q
    g = np.ones(n, dtype=complex)
    g[0] += z
    kept = set(range(n)) - set(removed)
    x = np.arange(n)
    S = np.zeros((n, n), dtype=complex)
    for t in kept:
        translated = np.roll(g, t)
        for ell in range(0, n, q):
            atom = translated*np.exp(2j*np.pi*ell*x/n)
            S += np.outer(atom, atom.conjugate())
    assert np.max(np.abs(S-S.conj().T)) < 1e-9
    return np.linalg.eigvalsh(S)


def prediction(m, q, removed, z):
    n = m*q
    k = n-len(removed)
    u, v = abs(z)**2, z.real
    vals = []
    count = []
    for a in range(m):
        s = sum(x not in removed for x in range(a, n, m))
        count.append(s)
        if s < q-1:
            return None
        if s == q:
            vals.extend([u]*(q-1))
            vals.append(u+q*(k+2*v))
        else:
            T = q*k+2*(q-1)*v+u
            D = u*(k-q+1)
            delta = max(0., T*T-4*D)
            vals.extend([(T-math.sqrt(delta))/2,
                         (T+math.sqrt(delta))/2])
            vals.extend([u]*(q-2))
    return sorted(x*m for x in vals)


def run():
    checks = 0
    for m, q in ((2, 2), (2, 3), (3, 2), (3, 3), (2, 4), (4, 2)):
        n = m*q
        all_indices = range(n)
        for e in range(min(n, m+2)+1):
            masks = list(itertools.combinations(all_indices, e))
            if len(masks) > 500:
                masks = masks[:250]+masks[-250:]
            for mask in masks:
                mask = frozenset(mask)
                good = len({a % m for a in mask}) == len(mask)
                for z in (-1.0, 1.25, -3.0+0.6j):
                    actual = direct_spectrum(m, q, mask, z)
                    expected = prediction(m, q, mask, z)
                    assert (expected is not None) == good, (m,q,mask,z)
                    if good:
                        assert np.allclose(actual, expected, atol=2e-8, rtol=2e-9), (m,q,mask,z,actual,expected)
                        assert actual[0] > 1e-8
                    else:
                        assert abs(actual[0]) < 2e-8, (m,q,mask,z,actual[0])
                    checks += 1
        for e in range(m+1):
            expected_count = math.comb(m,e)*q**e
            counted = sum(len({a % m for a in mask}) == e
                          for mask in itertools.combinations(range(n),e))
            assert counted == expected_count
            checks += 1
        for z, erasures, should_tight in (
                (-n/2, (), True),
                (-n/2+0.7j, (), True),
                (0.2, (), False),
                (-2.0, tuple(a for a in range(m)), m==2 and q==2),
                ):
            ev = direct_spectrum(m, q, erasures, z)
            tight = np.max(abs(ev-ev[0])) < 2e-8
            assert tight == should_tight, (m, q, z, erasures, ev)
            checks += 1
    print('ONE_DEFECT_SUBGROUP_ERASURE_CHECKS_PASSED', checks)

if __name__ == '__main__':
    run()
