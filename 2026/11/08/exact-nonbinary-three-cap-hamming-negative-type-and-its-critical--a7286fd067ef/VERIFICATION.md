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

The proof is a finite-character diagonalization followed by an exact quadratic optimization and a negative-type interval argument. The unnormalized Fourier transform, treatment of the trivial character, multiplicities, and both one-parameter limits are spelled out in RESULT.md. The accompanying standard-library `check.py` reproduces direct Fourier sums, critical degree comparisons, finite root tests, and asymptotic numerical controls. Execute `python3 check.py` in this directory.

Observed output: `QARY_CAP3_INDEPENDENT_FOURIER_CHECKS_PASS`; `direct_character_enumerations 12`; `analytic_parameter_cases 144`. All ordinary computations are finite checks; the infinite assertions depend on the written mathematical proof. No external mathematical audit or independent validation has occurred.
