#!/usr/bin/env python3
"""Finite numerical checks for the chiral triangular router transfer identity.

Requires NumPy; analytic Fourier and Kronecker arguments establish the theorem.
"""
import math
import numpy as np


def hamiltonian():
    core = np.array([[0, -1j, 1j], [1j, 0, -1j], [-1j, 1j, 0]], dtype=complex)
    z = np.zeros((3, 3), dtype=complex)
    eye = np.eye(3, dtype=complex)
    return np.block([[core, eye], [eye, z]])


def exact_amplitude(t, core, leaf):
    offset = leaf - core
    return -1j * (np.sin(t) + 4 / math.sqrt(7)
                  * np.sin(math.sqrt(7) * t / 2)
                  * np.cos(math.sqrt(3) * t / 2 - 2 * math.pi * offset / 3)) / 3


def main():
    h = hamiltonian()
    assert np.max(np.abs(h-h.conj().T)) < 1e-14
    energies, vectors = np.linalg.eigh(h)
    expected = np.sort([-1, 1, -(math.sqrt(7)+math.sqrt(3))/2,
                        (math.sqrt(7)+math.sqrt(3))/2,
                        -(math.sqrt(7)-math.sqrt(3))/2,
                        (math.sqrt(7)-math.sqrt(3))/2])
    assert np.max(np.abs(energies - expected)) < 1e-13
    bound = (23 + 8*math.sqrt(7))/63
    assert abs(bound - ((1 + 4/math.sqrt(7))/3)**2) < 1e-14
    tested = 0
    for t in (0, 0.125, 0.7, 2.629, 4.23, 11.17, 47.0):
        propagator = (vectors * np.exp(-1j * energies * t)) @ vectors.conj().T
        assert np.max(np.abs(propagator.conj().T @ propagator - np.eye(6))) < 1e-12
        for j in range(3):
            for k in range(3):
                computed = propagator[3+k, j]
                predicted = exact_amplitude(t, j, k)
                assert abs(computed-predicted) < 2e-12
                assert abs(computed)**2 <= bound + 1e-12
                tested += 1
    rng = np.random.default_rng(17341)
    for t in rng.uniform(0, 100000, 500):
        for j in range(3):
            for k in range(3):
                assert abs(exact_amplitude(t, j, k))**2 <= bound + 1e-12
                tested += 1
    # A three-frequency, finite-time scan supplies approximations only,
    # not a proof of the infinite-time supremum or of nonattainment.
    times = np.pi * (0.5 + 2*np.arange(300000, dtype=float))
    sine7 = np.sin(math.sqrt(7)*times/2)
    best = []
    for d in range(3):
        amplitudes = (1 + 4/math.sqrt(7)*sine7
                      * np.cos(math.sqrt(3)*times/2 - 2*math.pi*d/3))/3
        achieved = float(np.max(amplitudes**2))
        assert 0.7010 < achieved < bound
        best.append(achieved)
    print('PASS: spectrum, all 3x3 analytic amplitudes, bounds, unitarity')
    print('checked time-site amplitude instances:', tested)
    print('exact probability supremum:', f'{bound:.15f}')
    print('finite sampled lower approximations:', [round(x, 12) for x in best])


if __name__ == '__main__':
    main()
