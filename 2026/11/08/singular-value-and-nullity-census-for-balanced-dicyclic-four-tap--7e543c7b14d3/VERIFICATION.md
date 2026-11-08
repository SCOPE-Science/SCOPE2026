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

# Computational verification

Run `python verify_dicyclic.py` in the same directory, with Python 3 and NumPy available. The checker constructs the full integer right-convolution matrices, computes ranks modulo the prime 1000003, compares numerical singular values to the explicit Fourier formula, and checks the predicted nullity census. It verifies all 225 supports for p=3 and all 2025 supports for p=5, plus 200 pseudorandom supports for p=7 with a fixed seed. It directly compares 525 singular spectra. The expected concluding token is `DICYCLIC_FOUR_TAP_CHECKS_PASS rank_cases 2450 singular_cases 525`.

The tests use exact modular elimination for the displayed finite matrices, but a modular rank can in principle differ from complex rank. The hand proof from complete irreducible Fourier blocks establishes complex ranks for every odd prime. Numerical singular-value comparisons are toleranced finite tests only, not independent verification of the all-prime theorem. The signed-cosine gap argument and counting argument are symbolic and not delegated to the numerical checks. The classification of the full singular-value spectrum, the sharp equality criteria, and each support-count formula remain subject to independent review.
