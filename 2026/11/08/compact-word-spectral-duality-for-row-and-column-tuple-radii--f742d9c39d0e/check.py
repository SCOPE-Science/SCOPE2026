"""Finite-dimensional diagnostics for compact-Kraus spectral duality.

These tests do not establish any infinite-dimensional assertion.
Requires numpy.  Run: python check.py
"""
import numpy as np


def cp_matrix(ks, opposite=False):
    n = ks[0].shape[0]
    if opposite:
        ks = [a.conj().T for a in ks]
    return sum(np.kron(a.conj(), a) for a in ks)


def radius(a):
    return max((abs(z) for z in np.linalg.eigvals(a)), default=0.)


def main():
    rng = np.random.default_rng(9173)
    passed = 0
    for n in range(2, 6):
        for d in (2, 3):
            for repeat in range(12):
                ks = [(rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))) / (3*n) for _ in range(d)]
                a = cp_matrix(ks)
                b = cp_matrix(ks, opposite=True)
                assert np.max(np.abs(a.conj().T-b)) < 1.e-12
                passed += 1
                assert abs(radius(a)-radius(b)) < 1.e-10
                passed += 1
                # The matrix superoperator has the conjugate spectrum, with multiplicities.
                ea = np.linalg.eigvals(a)
                eb = np.linalg.eigvals(b)
                remaining = list(eb)
                for val in np.conj(ea):
                    j = int(np.argmin([abs(x-val) for x in remaining]))
                    assert abs(remaining.pop(j)-val) < 1.e-7
                    passed += 1
                # Every fixed-length word tuple again has conjugate CP spectra.
                words = [np.eye(n, dtype=complex)]
                for _ in range(2):
                    words = [a @ w for a in ks for w in words]
                aa = cp_matrix(words)
                assert np.max(np.abs(aa - a@a)) < 1.e-11
                passed += 1
    print(f"PASS: {passed} exact-formula and floating point diagnostic assertions")


if __name__ == '__main__':
    main()
