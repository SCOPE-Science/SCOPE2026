---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For fixed σ in [0,1], each pair of nonnegative shares sums to its outer weight, including when that weight vanishes. Thus resource conservation for the four printed shares does not imply the formally declared sum cap. With efficiencies frozen and both functions finite and continuous on [0,1], each attains its minimum. Their maximum is bounded below by M=max(m₁,m₂) everywhere; independently attaining the two minima gives M. The simultaneous M-sublevel conditions are necessary and sufficient for equality, and compactness of the boundary gives the stated intersection criterion. The reported conditional first shares sum exactly to 14399/10000. This proves the frozen square-domain correction, not that the paper formally used a square, not a strict improvement for its particular fitted coefficients, and not a dynamic optimum.

## originality

FAIL

An earlier indexed result on this exact model already supplies the square-versus-triangle correction, the same reported-ratio witness, the same corrected minimax value, and the observation that Eq. (20) is a different coupled problem. The only unstated additions, the product of sublevel sets and its intersection with the boundary, are immediate equality criteria in that same minimax proof.

## value

FAIL

The square correction is meaningful for interpreting this public-health model, but that correction and its practical witness are already available. The remaining sublevel-set and boundary-equality wording adds no demonstrated model-specific consequence or new obstruction; it is the elementary equality condition in the same separable maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
