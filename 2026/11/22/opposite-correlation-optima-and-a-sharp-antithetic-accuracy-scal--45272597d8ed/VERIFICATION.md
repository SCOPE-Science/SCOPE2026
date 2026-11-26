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

The frozen recurrence and formulas are correct for the exogenous colored oracle, but the frozen assumptions' phrase 'additive error independent of state' is false as a statement of statistical independence. In the unique stationary law, Cov(Z_k,ξ_k)=−hρσ²/(1−rρ), which is nonzero for every ρ≠0 (e.g. −3/5 at the finding's positive-correlation example). Taken literally, the independence assumption would rule out the colored regime. The complete replacement specifies no feedback from position to the error dynamics and independent thermal and oracle innovation streams, without imposing joint independence of the current error and position. In the repaired setting, stability of the joint linear recursion gives the unique Gaussian stationary law. Its causal thermal filter has coefficients t and t(1+r)r^(j−1) for j≥1, yielding 1/κ. In the oracle double sum, grouping by lag gives (h²σ²/(1−r²))(1+rρ)/(1−rρ); this is positive throughout the domain. The two independent streams' zero-frequency gains yield 2/(κ²h) and (σ²/κ²)(1+ρ)/(1−ρ), with absolutely summable covariance for each fixed admissible pair. Differentiation yields opposite signs for 1<κh<2, constancy of position accuracy at κh=1, and the claimed upper-end boundary limit. The Gaussian Wasserstein distance strictly increases with excess variance. At small h the variance prefactor is of order h; the remaining ratio is (κh+rδ)/(2−κh−rδ), δ=1+ρ_h. If the ratio is O(h), the denominator is at most 2 and r stays bounded below, so δ=O(h); the converse and leading coefficient follow on substitution. The boundary correlations remain limits only.

## originality

PASS

Credit the prior SGLM update and independent-gradient bias results as well as ordinary stationary linear-filter and integrated covariance identities. The surviving specific result is the fixed-marginal AR(1) classification simultaneously comparing invariant accuracy and mean-estimation variance, plus the necessary and sufficient antithetic scale for the variance error. The corrected assumption matches the exogenous AR(1) model originally used by the proof; it does not convert an iid-gradient result into this one.

## value

PASS

Even at fixed marginal oracle variance, changing temporal dependence changes two natural meanings of sampling quality. The exact regime of strict disagreement shows why better invariant fidelity need not improve linear time-average precision, and the sharp antithetic scaling tells how close to alternating errors one must be for second-order stationary variance accuracy. These consequences survive the correction from statistical independence to exogenous generation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
