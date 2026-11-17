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

The finite certificate is self-contained in `CHECK.py` and requires only the Python standard library. It uses exact rational endpoint arithmetic, checks interval disjointness, verifies every five-step itinerary before applying a polynomial branch, establishes that each five-step image strictly covers the reference interval, and computes strict lower derivative products greater than \(2\).

The proof of the invariant Cantor subsystem uses strict expanding inverse branches and standard unique symbolic coding; no finite computation is treated as evidence for infinite exhaustive orbit coverage. The entropy bound is established on a compact continuous invariant subsystem, not on the discontinuous global map. The perturbative continuation is qualitative by continuity, with no explicit radius certified.

Independent mathematical audit has not been performed.
