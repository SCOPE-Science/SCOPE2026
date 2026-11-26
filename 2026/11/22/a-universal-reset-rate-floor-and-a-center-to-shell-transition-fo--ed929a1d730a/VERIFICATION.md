---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

With complete independent Poisson resets, the stationary weak equation forces the probability measure q to have density p_a-r⁻¹L*p_a; smoothness excludes singular alternatives. Radial differentiation gives L*p_a/(κp_a)=d-2ν+2ν(1+bλ)s-4λν(ν+1)s². The drift flux at radius R is O(R^{d-2ν}), the diffusion flux decays faster, and both vanish at zero, so the forced source has mass one. For sufficiency p_a is in the L¹ forward OU generator domain: smoothly truncate at radius R and pass in graph norm using p_a, ∇p_a and L*p_a in L¹ and uniformly bounded x·∇χ_R. The forward resolvent then gives p_a=r∫₀∞e^{-rt}P_t* q_r dt, the unique invariant law by the first-reset coupling. No finite moment is needed. The strictly concave f is maximized at s₀=min(1,s_*), s_*=(1+bλ)/(4λ(ν+1)). Positivity of the maximum follows from its zero mean and nonconstant values on an interval of full support. At the rate boundary the density factor is κ[f(s₀)-f(s)]/r; RESULT.md §3's introductory reference to f(s_*) is only valid for the interior and critical regimes, and its subsequent subcritical computation correctly uses f(1). Since 1-s is quadratic in radius at zero and s has nonzero radial derivative at a positive radius, the three vanishing orders follow from the one-sided derivative or the exact quadratic vertex difference. The two rate branches meet at λ_c; the first decreases and the second has derivative ν(b²-λ⁻²)/(4(ν+1)) in κ units. The unique minimizer 1/b lies above λ_c, and direct substitution gives the minimum d/(ν+1) and squared zero radius dD/κ. In d=1 the nonzero sphere is two points. Replay: RESULT.md §§1–5; CHECK.py was inspected but not executed. It provides finite arithmetic support, not general positivity or semigroup sufficiency.

## originality

PASS

Both forward reset renewal theory and the inverse-source identity are antecedents. The checked sources do not give the sharp Pearson–VII feasibility branches, optimized floor and zero geometry for complete Poisson OU resetting. The distinct claim is the classification in this family, not the inverse recipe.

## value

PASS

The rate threshold is a necessary and attainable design constraint for a standard multivariate heavy-tailed family, including targets with infinite variance. It describes the actual limiting reset law and supplies a unique optimal target width and exponent-independent physical zero radius. These answer a motivated feasibility/optimization question beyond simply writing the forward or inverse equation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
