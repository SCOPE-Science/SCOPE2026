---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS mathematically: normalized equiaffine arclength is uniform eccentric anomaly t because |det(x′,x″)|^(1/3)=(ab)^(1/3). Conditional chord phase and triangular angular-gap law give p=1/4−3Li2(η²)/(2π²), the same as earlier primary full proofs. Positive Li2 series yields monotonicity, sharp deficit bounds and endpoint expansion. Independent quadrature checked four η values; scientific rejection is for prior coverage, not incorrectness.

## originality

FAIL

FAIL. Equiaffine arclength on an ellipse is (ab)^(1/3)dt, so the exact law is mathematically the already-published uniform-eccentric-anomaly result. Both 2026-10-25 and 2026-11-02 complete primary proofs cover the formula, axis ordering, degeneration and circle enclosure coincidence; new deficit bounds are trivial positive-series inequalities.

## value

FAIL

FAIL: Once the already-known exact ellipse probability, strict monotonicity, degeneration and off-center circular equivalence are removed, only elementary Li2 series sandwich bounds and the rephrasing of the sampling measure remain. Neither supplies a motivated independently new scientific finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
