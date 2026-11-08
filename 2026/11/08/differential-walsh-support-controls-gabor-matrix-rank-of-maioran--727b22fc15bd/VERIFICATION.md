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

The proof identifies the nonzero Weyl-orbit coefficients with all nonzero ambiguity coefficients, and counts each of the three disjoint shift classes exactly. The rank expression is an integer for every dimension and Boolean perturbation. The equality condition is checked through Walsh one-support equivalence and the unique Boolean algebraic normal form. For cubic perturbations, the derivative polar rank equals two in exactly seven eighths of directions, giving the stated exact gap.

To reproduce finite checks, run `python3 check.py` in a directory containing the embedded script. The script computes the raw Gabor ambiguity Fourier support using integer Walsh–Hadamard transforms, independently computes derivative supports, and compares them. It exhausts all Boolean perturbations at dimensions with \(m=1,2,3\), checks explicit cubic and quadratic examples at \(m=4\), and checks twelve reproducible samples at \(m=4\). Expected message: `DIFFERENTIAL_WALSH_GABOR_CHECKS_OK cases= 292`. Finite enumeration does not certify the infinite statement; the proof provides its quantifiers and boundary cases. Historical priority and independent mathematical validation have not been certified.
