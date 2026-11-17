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

# Verification record

Run `python verify.py` from a directory containing `verify.py`. No network access is required. The standard-library tests verify the exact cube of the cat matrix and determinant, enumerate *all states* for dyadic grids through \(2^6\), check rational trace identities for five moduli, and compare three finite-resolution traces with the analytic profile. Optional `mpmath` calculations at increased precision check dyadic periodicity, a nonzero Fourier coefficient, and a nonzero phase difference for \(H(1)\) and \(H(3/2)\).

Observed check marker: `VERIFY_OK exact_A3=1 dyadic_censuses=6 rational_traces=5 scaling_samples=3`.

The mathematical proof is in `RESULT.md`. Finite enumeration and numerical profile comparisons are corroborative, not exhaustive for all moduli, and do not constitute independent review or verification of the infinite assertions.
