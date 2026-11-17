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

# Reproducibility

`verify.py` is standalone and requires only Python 3 standard library modules. In the delivered package, run `python3 verify.py` from the directory containing the source file; the program prints `ALL_CHECKS_PASSED 490` when all assertions hold. The 490 checks cover the closed-form tail formula against independent midpoint quadrature, direct spherical dot-product enumeration on deterministic equal-area grids, probability positivity/normalization, the expected count, hemispherical parity and sharp first-contact coefficients.

These finite experiments are diagnostics and provide no infinite proof. The analytical proof for all integers \(n\ge3\), all real cap radii \(0\le r\le\pi\), and every integer multiplicity is in `RESULT.md`. External historical priority is not independently certified; the supporting literature and residual access limitations are described in the scientific review.
