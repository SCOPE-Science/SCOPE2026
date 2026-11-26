---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The conditional count at recognized size ℓ is binom(n−ℓ,k−ℓ)D_(n−k)/(n−ℓ)! = c_(n,k)(k)_(fall ℓ), vanishing when ℓ>k. Thus exactly k=n−1 must be excluded among the interior rows. The Pascal kernel is totally nonnegative and the odds-power kernel has strictly positive increasing-exponent ordered minors for strictly increasing positive odds. In Cauchy–Binet, intermediate columns 0,…,r−1 in the falling-factorial kernel give the ordinary Vandermonde in k, since the column polynomials are monic of degrees 0,…,r−1. That term is strictly positive and all terms are nonnegative. For curvature, reversing the standard Laguerre coefficient sum at degree k and parameter n−k gives the stated odds polynomial with constant term one. Orthogonality on (0,∞) gives k simple positive zeros, hence the stated positive linear factors in θ. Their second log derivatives give the identity; the (1−θ)^(n−k) term is strictly concave if k<n, and otherwise at least one of n≥2 distinct roots is not 1. The exponent also gives score −∞ at θ→1 when a count is <n; at 0 the score is n times the sum of (k−1). All-n data give a strictly increasing likelihood by coupling the binomial recognized size. These checks support the boundary/maximizer claims in RESULT.md lines 33–75. Independent exact subset/permutation enumeration at n=3 gave p_0=(1−θ)^3/3, p_1=1/2−3θ²/2+θ³ and p_3=1/6+θ+θ²/2−2θ³/3. They sum to 1; all ordered minors on the three-parameter grid (1/4,1/2,3/4) were positive, with determinant 11/1024, and the log-curvatures at 1/2 were (−12,−9,−984/289). Inspected verify.py without executing it. The n=3 calculation and supplied finite checks are not all-size proofs.

## originality

FAIL

The strongest same-model paper states the exact mixture, likelihood/Hessian, MLR, and MLE uniqueness; the inspected passages do not state the exact all-order and curvature formulas verbatim. Nonetheless both proposed sharpenings are direct consequences of that very mixture in the standard composition formula and Laguerre identities, with all hypotheses and strictness reduced explicitly below. This is demonstrated prior implication, not a claim that the exact combined wording was found or that a failed lookup weighs against novelty. No independent scientific remainder survives narrowing to either branch.

## value

FAIL

Strict likelihood shape for this natural model is useful, but the submitted contributions are the immediate positive-minor composition and classical root-factor consequences of the known exact mass function. No further inference result, distinct sharp boundary, or nonmechanical invariant beyond those consequences was established. MLE uniqueness is already stated by O'Neill; the extra finite checks do not create a surviving scientific finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
