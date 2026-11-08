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

The analytic certificate is the four-part proof in RESULT.md: (i) exact two-point quadrature moments; (ii) the positive-semidefinite diagonal inequality; (iii) strict univariate minimization; and (iv) an attaining symplectic tableau with exact third-order conditions. Together these cover every admissible real tableau, not only a finite sample.

Run `python verify.py` in the extracted package. The script checks six exact-rational tableaux and their four order conditions, exact vanishing of the algebraic-stability matrix, rational bounds for the unique quartic root, and 1,500 supplementary numerical comparisons. Numerical tests alone are not an infinite proof. The verification assumes exact real arithmetic and does not establish stability for any application or stage count beyond two.
