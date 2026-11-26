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

Re-audited the corrected all-direction claim. For s≠1 the square root has no zeros; the circle in the squared plane has winding 0 or 1 about 0, giving two 2π branches or one 4π branch. Holomorphic local orientation and the sublevel region certify the outward normal e^{it}/(z/|z|). Its lifted derivative is (s²+2+3s cos t)/(2|1+s e^{it}|²), with total positive turn 2π per component when s<1, and net turn 2π when s>1. At s=2 the normal lift is strictly increasing despite isolated stationary parameters; thus all directions have one point. For 1<s<2 the numerator has two simple zeros per 2π and one negative interval. At t=π±φ the argument of 1+s e^{it} is π±ψ, giving outward angles π/2∓A/2 and antipodal ones on shifting t by 2π. The drop is positive and less than ψ<π/2, so these critical values are distinct. Signed degree gives m=1+2 times the number of negative preimages at every regular direction. Each simple fold contributes one distinct point exactly at its critical direction, while the one regular point persists from the side with a single preimage; distinct critical values exclude any other fold in that fiber. The two negative turns give K=2π+4A. Differentiation gives A′=−sqrt(4−s²)/(s sqrt(s²−1)); expanding this integrand gives −A′=sqrt(3/2)(s−1)^(−1/2)(1+O(s−1)) and −A′=sqrt(2−s)/sqrt(3)(1+O(2−s)) at the respective endpoints. Integrating gives both stated constants and remainder orders; endpoint arcs are measure zero. The implicit-gradient replay independently found and checked widths and absolute turns and matched 1,799 regular direction counts on connected shapes. The fold endpoint counts follow from the analytic simple-fold and compactness argument, not the sample mesh.

## originality

PASS

Best-of-knowledge pass for the exact angular fold images, all-fiber law and quantitative shape statistic, not for the classical topology, convexity threshold, curvature/inflection ingredients, or the generic degree-count formula. The critical-fiber extension uses a standard fold argument and is not credited as a separate novel fact beyond completing the Cassini-specific classification.

## value

PASS

Cassini ovals are a standard family in which disconnectedness and nonconvex connectedness behave differently. Counting boundary points with a prescribed outward normal is a natural inverse-geometric observable. The full angular fiber law locates where direction inference is ambiguous, including exactly where ambiguity changes. Its resolved measure recovers the shape parameter within the peanut phase, evaluates absolute curvature and distinguishes the two degenerations quantitatively. These are not supplied by just knowing the signed turn or convexity threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
