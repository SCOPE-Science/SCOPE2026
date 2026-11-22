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

The source `verify.py` generates Kautz vertices for selected small parameters, computes every directed shortest-path distance by BFS independently of the suffix/prefix proof, checks exact equality with overlap-derived distances, and verifies the prefix-twin necessary condition. It verifies every minimum prefix-transversal at \((q,n)=(3,2),(3,3),(3,4),(4,2),(5,2)\) and shortest distances and twin constraints at \((4,3)\). Execute `python verify.py`; a successful run prints `VERIFY_OK`.

The mathematical proof applies to every integer \(q\ge3\), \(n\ge2\); finite computations corroborate but do not certify its quantifiers. No external/independent audit or noise robustness has been performed. The established dimension formula is credited to Rajan et al.; uniqueness against all unindexed literature is not certified.
