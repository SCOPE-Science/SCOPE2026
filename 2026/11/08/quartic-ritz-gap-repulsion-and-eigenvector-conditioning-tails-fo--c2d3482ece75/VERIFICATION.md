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

# Verification of formulas and computations

The complete proof is in `RESULT.md`. The provided `verify.py` uses exact rational arithmetic for the barycentric polynomial identities and NumPy for direct, independent matrix checks of the Ritz gap, Schur off-diagonal modulus, and unit-column eigenvector conditioning. The script runs 5,436 positive assertions on its fixed seed, including finite-sample consistency checks for both real and complex ensembles. Reproduce with `python verify.py` from the directory containing `verify.py`; NumPy is required.

The asymptotic gap and conditioning-tail constants depend on the exact Dirichlet densities and elementary local disk-area limits, not on a numerical fit. Simulations only inspect moderate positive thresholds and cannot verify infinite-limit or moment claims. The probability of a defective compression is zero, but the defective point is in the support. The results do not imply bounds for non-Haar or finite-precision eigenvalue algorithms.
