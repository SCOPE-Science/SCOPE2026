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

# Verification and limits

The entire proof in `RESULT.md` is a finite graph-theoretic argument; it depends only on three-edge walks, odd shortest paths in bipartite graphs and the exact integer partitions proved there. The one-step rule is evaluated synchronously. Disconnected components and the empty relation are covered by convention.

Run `python3 verify.py`. It uses direct Boolean incidence-matrix saturation independent of a breadth-first-search distance classifier and tests every stage, every fixed-point index and the sharp alternating-path cutoff. It also implements the anchored historical update separately to confirm a different distance-radius law. The executed run produced `VERIFY_OK 71642 exhaustive and random matrices; 25 sharp paths; anchored-rule comparison`. Its complete finite matrix sweep covers shore sizes up to \((4,4)\), with seeded random tests at additional sizes and all-size symbolic proof stated separately.

Finite tests do not prove the universal theorem or establish novelty. Literature inspection supports a best-knowledge distinction between the known final difunctional closure and the new exact synchronous trajectory; an independent exhaustive priority review remains unperformed.
