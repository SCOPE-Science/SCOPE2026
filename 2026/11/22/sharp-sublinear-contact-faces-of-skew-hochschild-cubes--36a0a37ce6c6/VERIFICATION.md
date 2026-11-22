---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification scope

Reproduce the finite computations with `python3 hoch_circumsphere_check.py`. The exact-rational checker enumerates all \(2^{n-1}\) composition vertices for every integer \(2\le n\le12\), evaluates the quadratic cosphere identity, tests the exact minimum-sphere formula and contacts, and validates the prefix inequalities that make the claimed center feasible. It ends with `HOCHSCHILD_SKEW_CIRCUMSPHERE_EXACT_PASS`. The proof in `RESULT.md` supplies independent all-dimensional reasoning through composition merges, convex projection, a transportation decomposition, and a contact-barycenter certificate. Exhaustive finite checks alone do not prove the infinite assertion. No independent audit has been performed.
