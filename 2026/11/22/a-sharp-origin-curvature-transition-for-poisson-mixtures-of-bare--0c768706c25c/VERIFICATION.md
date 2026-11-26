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

The frozen deficit asymptotics survive unchanged. Its final proof paragraph asserted the classical second-derivative limit without an estimate for the moving-edge singularity. The symmetric second difference alone cannot prove existence of the classical derivative, and direct twice-differentiation of the packet integrand is not justified by 3a<1 when ν<1. The complete corrected article is /workspace/repairs/5/RESULT.md; it replaces that step with an exact Tonelli primitive and corrects the version attribution of the prior special cases. Renormalizing x by ℓ t^a gives the claimed beta normalizer; mixing at x=0 gives r^aΓ(1−a)/(ℓIσ). At nonzero x the change of age t=su, s=(|x|/ℓ)^(1/a), gives the deficit tail νu^(−3a), so dominated convergence and integration by parts give the subcritical beta constant. At 3a=1 the tail is exactly u⁻¹ for u≥1 and E₁(rs) contributes −log(rs); at 3a<1 the original integrand divided by x² has a bounded packet factor tending to ν times the integrable age weight t^(−3a)e^(−rt). All deficits are o(|x|), so the ordinary derivative at zero vanishes. For classical curvature, the repaired derivative quotient is −2rν/(ℓ³Iσ) times K(q), q=x²/ℓ². After substituting t=q^(1/(2a))u, K is continuous at every positive q by integrability of (u−1)^(ν−1) at the edge. When 3a<1 the age interval from s to 2s has contribution O(s^(1−3a)), and above it the singular factor is uniformly bounded and converges to 1, giving the gamma integral by domination. For 3a≥1 Fatou gives divergence of K to +∞. This checks the two-sided classical derivative quotient, not only the symmetric second difference. Independent spot checks at r=ℓ=1 give deficit coefficients 10, 9/4 and Γ(1/4)/π for σ=1/2,1,2 respectively; the σ=1 similarity equation gives ℓ³I₁=6D and hence prefactor r/(2D). Replay: repaired RESULT.md (1)–(4) and the support-edge bounds; the uploaded checker was read as text, not executed. The verdict is for the one-dimensional exponential-age mixture, not for a stationary solution or evolution of a nonlinear reset PDE.

## originality

PASS

The repaired proof supports the same substantive claim: the all-positive-σ local classification with explicit fractional, logarithmic and quadratic coefficients and classical curvature threshold. The underlying renewal density is established prior work. The critical σ=1 and the σ=2 special cases are already encoded by Chełminiak's revised closed forms and are not counted as separate new results. The repair adds justification, not a broader novelty claim.

## value

PASS

The reset origin is a distinguished physical and mathematical point, and the result shows exactly when a local curvature description is legitimate there. The change of order and critical logarithm, with coefficients for the entire nonlinearity range, are useful qualitative information beyond existing renewal representations and individual examples. This value does not depend on novelty of the underlying model, or on claims of a nonlinear source-PDE solution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
