---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Direct multiplication gives the symmetric 2×2 block with diagonal (−ab,0) and off-diagonal (a+b)/2; all other entries vanish. The orthogonal tangent projector gives zero on the stated Z. Conditional on the first Gaussian columns (g,g′), the ratios have variances ∥g∥⁻², ∥g′∥⁻² and correlation ρ cos(angle). For fixed |ρ|<1, the standardized Gaussian absolute-product moment is bounded above and away from zero on the compact conditional correlation range. Radial integration in each first column, using a positive density on a ball times an annulus for necessity and Gaussian tails for sufficiency, gives p<ℓ including divergence at the boundary. For |ρ|=1 both signs give b=a and the norm squared is a⁴+2a². The density cℓ(1+x²)^−((ℓ+1)/2) gives the threshold p<ℓ/2 and the tail constant 2cℓ/ℓ after inverting the norm. Inverse chi-square integration and normal second/fourth moments reproduce both endpoint mean squares and their strict difference on ℓ≥5. Independently substituting x=(1+2u)^−1 in the Laplace integral gives Iℓ=[2(ℓ−2)]^−1 ∫₀¹ x^(ℓ/2−2)/(s+ρ²x) dx, s=1−ρ². For ℓ=3 set x=y² to get arctan(|ρ|/√s)/(|ρ|√s); for ℓ=4 direct integration gives −log(s)/(4ρ²). Wick's factor lies between 1 and 3 and the remaining norm-squared term stays uniformly bounded when ℓ>2, giving the two asserted sharp orders, not projected-risk leading constants. For ℓ≥5 Cauchy–Schwarz and the shared fourth marginal moment give a uniform bound. The frozen `verify.py` was inspected, not executed; lines 39–93 give replay paths for the matrix, endpoint and integral diagnostics. Neither the check nor the theorem addresses repeated integration, higher ranks, or other couplings.

## originality

PASS

The supported distinct result is the moment phase and quantitative contamination comparison for this prescribed symmetrized two-sided oblique tangent map. The oblique projection formula and the possibility that perpendicular forcing produces oblique motion are prior. Normal/chi laws, the bivariate chi-square product moment (including the inverse-norm integral as a special case), and independent-product heavy-tail mechanisms are also prior ingredients. The checked antecedents do not give the jointly coupled projected force or its endpoints and moment comparison.

## value

PASS

The rank-one positive normal-input test asks a concrete design question: can one reuse a sketch to keep the oblique tangent output symmetric without changing the probabilistic size of an otherwise zero tangent force? Finite mean-square risk needs three rows under any imperfect coupling but five at perfect sharing, and the sharp blow-up orders quantify the lack of uniformity in the former guarantee. This is an actionable distinction for the defined projection benchmark and goes beyond noting nonzero leakage. It does not establish stability or optimal sketch reuse for a time integrator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
