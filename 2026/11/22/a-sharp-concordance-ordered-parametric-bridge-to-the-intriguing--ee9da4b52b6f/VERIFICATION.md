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

Separately reconstructed the margins and mixed derivative. As x approaches 0 the powers stay bounded uniformly in y; as x approaches 1 the exponent tends to 1 and remains bounded away from zero, giving joint boundary continuity. For 0≤γ≤1, set s=1−x, t=1−xy and b=γs/x. The term −log t−s(1−t)/t is nonnegative on [s,1] by differentiation. The resulting lower bound on ∂x∂y C is s^b[1−γx−(γs/x)log s], strictly positive throughout the open square. Integrating on interior rectangles and passing to the continuous boundary proves two-increasingness. At x→1 with fixed y<1 the density tends to 1−γ−γ log(1−y). For γ>1 use y=0 and then continuity to obtain a negative interior rectangle; for γ<0 fix an interior y sufficiently near 1. For a≥1 the function u^a(−log u)/(1−u) is strictly increasing, as follows by factoring out u^(a−1) and differentiating the a=1 case. The parameter derivative is a positive prefactor times its difference at t and s; this proves the strict pointwise order and, by integration, strict Spearman ordering. Read VERIFICATION.md and check_int1.py without running the uploaded script; its sampled derivative and inequality tests are not used as a universal certificate.

## originality

PASS

The strongest source already contains exactly Int1 and exactly the proposed varying exponent, but in different constructions. The inspected results do not imply the sharp admissibility and strict ordering of the proposed interpolation. This is a bounded assessment, not a determination of historical priority.

## value

PASS

Int1 is a published asymmetric dependence model without a tuning parameter. A natural nonlinear interpolation now admits exact validity limits and a strict dependence order without relying on sampled densities or assuming closure under exponent interpolation. The result tells users exactly which parameter values are available and how their dependence compares; no claims about fitting or estimation are needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
