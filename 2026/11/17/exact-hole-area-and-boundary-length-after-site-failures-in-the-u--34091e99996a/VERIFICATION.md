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

# Verification

The proof is self-contained: its nonstandard geometric step is the six-neighbor locality claim for a unit elementary triangle. The proof includes its edge-projection enumeration. The two exact geometric quantities in the finite statement are checked against an independent midpoint integration of distances to retained sites by `check.py`. The Bernoulli formula is also tested by complete enumeration of the six relevant site-status bits, separately from the face-count symbolic derivation.

A numerical integration is not an infinite proof. The \(q\)-density almost-sure limit uses the standard pointwise ergodic theorem for bounded local functions of an i.i.d. lattice field, plus an \(O(R)\) boundary-cell error. No independent mathematical audit was performed.
