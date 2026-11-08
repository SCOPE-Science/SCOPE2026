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

# Reproducible checks and scope

Execute the three included Python scripts in the same directory with Python 3, NumPy, and SciPy. The modular checker covers 8,358 dimension and 84,598 site cases; the full Hermitian spectral checker covers 297 cases; the gauge-and-loss-rate checker covers 216 phase/rate cases and finite-time consistency tests. All checks completed successfully on the delivered scripts. The proof uses cyclic Fourier decomposition, an elementary gcd equivalence, and finite-dimensional dissipative spectral theory, so finite enumeration is not being mistaken for an infinite proof.

The numeric SVD threshold is \(10^{-8}\); this tolerance is only a validation convention, not part of the exact theorem. Full Hamiltonian eigenspace grouping is performed independently of the modular construction. Absorption rates influence only transient decay under the stated assumptions. No interacting particles, finite-temperature statistics, additional dephasing, or independent external audit are covered.
