---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Patey–Shafer Theorem 1.7 already proves for every finite k that BRT^3_{2,4} is not ≤^k_ω RT^2_2. A bounded-pair instance (l,f) is an ordinary RT^2_2 instance f; every infinite RT-homogeneous set must have color 0 because a color-1 infinite homogeneous set would violate the absence of an l-element color-1 homogeneous subset. Therefore each BRT pair oracle use simulates with exactly one RT pair use; a hypothetical finite-use bounded-pair reduction contradicts published Theorem 1.7. No experiments or extrapolation.

## originality

FAIL

Published strictly stronger Patey–Shafer finite-use theorem already logically implies the submitted statement through a one-line identity-on-instances simulation. This is coverage despite the different target oracle terminology.

## value

FAIL

The source supplies no new hyperimmunity construction or strengthened reducibility boundary: all work is a routine oracle-weakening corollary of a strictly stronger published theorem. Repackaging an immediate consequence as a new finite-arity separation does not meet the substantive value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
