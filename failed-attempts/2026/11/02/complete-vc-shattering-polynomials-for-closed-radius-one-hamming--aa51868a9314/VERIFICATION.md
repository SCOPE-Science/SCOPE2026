---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Fix a center for the full trace. A different center on one arm covers only that arm among the neighbors; a center at distance two can cover at most two neighbors on distinct arms; farther centers cover none. These facts rule out shattering four: if the original center is a support point, it cannot be dropped while retaining a mixed-arm triple of neighbors; otherwise a mixed-arm triple forces the original center and thereby the fourth point. Collinear triples fail the two-positive trace. The remaining triples have distance patterns (1,1,2), (2,2,2), (1,2,2), and unique full-trace centers. Offsets on a spare coordinate give the requisite exclusion witnesses in d≥3. In d=2 the pivot has no singleton witness, the three-arm case is impossible, and the repeated-arm triple is shattered exactly when q≥4, as its empty trace needs an unused value outside three on one coordinate and two on the other. The pair condition is exactly distance ≤2 outside d=1 and (d,q)=(2,2); in the latter every ball misses only one vertex. Counting the three types and applying Pascal's identity gives the stated formula. Independent raw traces in branches/224c8b6a-87ed-4117-9045-0533e8f21052/verify_record4_raw.py reproduced all counts through support size four at (2,2),(2,3),(2,4),(3,2),(3,3),(4,2); this is finite corroboration.

## originality

FAIL

A distinct Resultary record, 6c82fc864f93, states the entire same polynomial on identical objects and parameters and proves the same three-type support classification. The product-form simplification does not change the theorem. This is demonstrable catalogue coverage, not a finding about time of discovery, authorship, or the order of the two records. No distinct mathematical remainder was identified in the frozen claim.

## value

PASS

As a mathematical result, the all-parameter structural census quantifies which finite samples realize all labelings, rather than just the largest size; it explains the alphabet threshold via the empty trace and separates three distinct geometric mechanisms. This is substantive scientific content, but the duplicate coverage gives this frozen finding no separate originality credit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
