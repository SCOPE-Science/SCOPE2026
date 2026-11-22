---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-20.md",
      "INDEPENDENT_AUDIT_2026-11-20.json"
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

Read complete fixed-tree RESULT.md and inspected actual check_covariance.py entry. The stable filter representation X_j=j gamma integral exp(-j gamma s)S(t-s) ds gives the stated covariance; independently recomputed the full 3x3 determinant and its differentiated quartic with exact SymPy, matching the displayed rational expression. A one-sign-change Descartes argument plus Q(0)<0<Q(infinity) establishes the unique positive kappa critical point. For support, binary controls dense in [0,1]-valued moment controls, positive finite-switch path probabilities give both input-mode supports, rearrangement/bathtub inequalities give sharp lower and upper quadratic moment bounds and convex interpolation, and the exact section integral gives Beta(3,3)=1/30. These infinite claims rest on those arguments, not on sampled rates.

## originality

PASS

Best-of-knowledge PASS for combined three-moment explicit stationary support and sharp unique covariance-volume rate maximum, not for classical telegraph covariance formulas or existence of support. Benaim-Bichard gives general accessible-support identity and density regularity but not explicit trivariate bounds, volume or determinant optimizer; Bakhtin et al is planar. Actual Resultary comparison did not show a dominating 1:2:3 sharp optimization. Classical moment-space literature may contain the support body, but no located result covers the combined precise new optimizer.

## value

PASS

PASS: Rate-independent reachable volume versus a unique rate-dependent generalized-variance optimum is a motivated structural distinction in a nonelliptic stochastic-switching family; an explicit three-moment body and sharp universal optimum are more than repeated two-point correlations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
