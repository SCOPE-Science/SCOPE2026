#!/usr/bin/env python3
"""Finite consistency checks for the excitation-support proof.

The proof in RESULT.md is analytic and applies to every number of segments.
This script checks the abstract support dynamics for a bounded range and the
closed-form depth count used by the statement.
"""
from math import ceil

ANCILLA = (0, 1, 2)


def classical_closure(states):
    """Classical-field control preserves the cavity photon number."""
    return {(n, a) for (n, _) in states for a in ANCILLA}


def quantum_closure(states):
    """Quantum-field control preserves total excitation n+a."""
    totals = {n + a for (n, a) in states}
    return {(t - a, a) for t in totals for a in ANCILLA if t - a >= 0}


def max_photon_after(k):
    states = {(0, 0)}
    for _ in range(k):
        states = classical_closure(states)
        states = quantum_closure(states)
    return max(n for n, _ in states)


def main():
    for k in range(0, 21):
        got = max_photon_after(k)
        assert got == 2 * k, (k, got)
    for n in range(0, 41):
        k = ceil(n / 2)
        assert 2 * k >= n
        if k:
            assert 2 * (k - 1) < n
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
