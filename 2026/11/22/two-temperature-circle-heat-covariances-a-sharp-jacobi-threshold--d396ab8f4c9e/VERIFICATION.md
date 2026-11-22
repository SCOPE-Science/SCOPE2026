---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification procedures and limits

Run `python3 check_two_time_heat.py` in the directory containing this file; it requires only the Python standard library. The script independently constructs high-precision *candidate* positive vectors, converts every component to an exact integer, and verifies strict rational Collatz–Wielandt inequalities with exact Fraction operations and norm bounds on the omitted infinite tails. On replay it passed all three cases (24/23, 12/11, 5/4), proving the odd–even–odd parity ordering and, by continuous spectral branches, at least two crossings.

The analytic phase law follows from an exact Fourier coefficient and Jacobi congruence, together with the finite Fourier tests criterion, the free adjacency spectrum, compact-operator spectral symmetry, and decay of critical Jacobi eigenvectors. Finite tests alone do not prove the infinite cutoff. Annihilating smooth measures are obtained from the critical eigenvectors, while no finite atomic Fourier transform can converge to zero at infinity. The audit is confined to these claims. No independent review, numerical condition-number assertion, uniqueness of parity crossings, or definitive historical priority is claimed.
