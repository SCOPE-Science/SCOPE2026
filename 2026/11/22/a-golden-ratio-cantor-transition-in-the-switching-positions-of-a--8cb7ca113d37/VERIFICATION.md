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

# Verification

The stationary two-run map is derived by composing two exact solutions of \(\dot z=\kappa(\sigma-z)\). Four contractions define the attractor and measure. The hull endpoints, all three exact factored signed gaps, and the canonical \(q=1/2\) intervals are given in `RESULT.md`. For \(q<\varphi^{-1}\), strict image gaps justify classical strong-separation Hausdorff dimension and exact-dimensional measure formulas. For \(q\ge\varphi^{-1}\), adjacent overlap along a chain beginning and ending at the hull endpoints yields an interval attractor. A renewal-reward identity and a positive lower bound on within-run speed imply bounded physical-time stationary density without any numerical approximation.

Execute `python3 verify.py` in the extracted directory. Its Python-standard-library checker passes 187 rational/numeric assertions on endpoint maps, gap identities, ordered image behavior, invariant hulls, dimension examples, and finite symbolic mass. These checks do not replace the exact algebra or classical infinite-level contraction and measure-dimension theorems.

The external scientific literature comparison is qualified. The motivating 2024 paper's relevant complete sections were inspected, as were the complete accessible result/proof texts of the two closest renewal-swimmer variance studies. No external independent audit or experimental validation has been performed.
