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

Rotational invariance gives the same conditional law of the squared radial multiplier given every past, hence independence and the fixed-dimension strong law. The square representation gives positivity and integrability of the log; the exact mean multiplier is 1-2η+(d+2)η². Independently, at c=2/(d+2), dividing E[(F-1)²] by 3c⁴ replaces U by a chi-square with five degrees of freedom (U² size bias), leaving W independent. Their sum then has d+4 degrees of freedom, so its squared deviation about d+2 has expectation 2(d+4)+4. Thus the leading second moment is 96/d³; the step displacement contributes 2a/d³ to the first moment. Centered W moments and fixed U moments give E|F-1|^p=O(d^(-3p/2)) for bounded a. On |F-1|≤1/2 the Taylor remainder is O(d^(-9/2)) in expectation, while the tail has arbitrarily small polynomial probability and its log is controlled by F and η²UW. This gives 2a−48 uniformly for bounded a. For a strict local crossing one can also differentiate under the expectation for large d: |F′/F|≤2η^(-1)(1+U/W)+2η^(-2)/W has L² norm O(d) uniformly for η near c, while F′ has bounded L² norm. On the good event the difference from E F′ is O(d^(-3/2)) and on the tail it is negligible; the derivative tends to 2. The signs for mean-square and pathwise growth follow with time tending to infinity first.

## originality

PASS

The mean-square boundary is explicitly prior. The supported distinct claim is the local ambient-dimension log-multiplier asymptotic and its leading pathwise–mean-square separation for one fresh unnormalized vector per step, not the mere existence of a difference between pathwise and moment growth.

## value

PASS

The exact mean-square edge is a natural reference point for users of covariance stability. The dimension-dependent width and sign of the regime in which typical trajectories decay while expected squared norm grows are not quantified by Jensen or an example at a single dimension. Identifying the scale d⁻³ and the coefficient 24 distinguishes the single-vector high-dimensional mechanism from the scalar probe-count mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
