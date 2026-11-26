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

For real distributional BV, subtracting the integral of the step kernels against Df leaves a function with zero distributional derivative, hence a constant. Both averages preserve constants. For a unit jump at s the defect equals −(1−α)(1−s)/(1−x) on x<s and αs/x on x>s. Integration yields E_α; Tonelli and the triangle inequality then bound the general signed-measure defect by ∫E_α d|Df|, and testing one jump gives the exact norm. E_α is strictly concave, with an interior critical point also at the pure endpoints (1−1/e and 1/e respectively). For nonzero variation, equality forces |Df| onto the unique maximum, so the displayed nonconstant steps suffice and exhaust that class. Constants also satisfy the unnormalized inequality as 0=0 and are excluded from the norm quotient and the nontrivial equality classification (as in Proof §4). All mixtures have the same value at s=1/2, but only α=1/2 has zero derivative there; this proves unique minimax balance even against the pure endpoints. At balance E''(s)=−1/[2s(1−s)]≤−2, yielding the integral deficit bound. The Taylor quotient along displaced single jumps tends to 1, so the quadratic factor is sharp. No restriction to monotone inputs or endpoint boundary traces is used.

## originality

PASS

The checked literature does not give the stated open-interval BV identity-defect norm for fixed convex mixtures of the forward and reflected averages, or its minimax theorem. This is a qualified finding about the specific operator and objective: the signed step reduction and binary-entropy deficit estimate are standard mechanisms, not separate originality claims.

## value

PASS

A forward/backward average is a natural way to approximate a BV input without choosing a direction. The result determines the best worst-case error among all fixed convex mixes, classifies nontrivial extremizers, and gives a sharp quantitative localization statement for arbitrary signed derivative measures. In particular, a small norm deficit bounds the part of the variation carried away from the midpoint, rather than merely lowering a numerical coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
