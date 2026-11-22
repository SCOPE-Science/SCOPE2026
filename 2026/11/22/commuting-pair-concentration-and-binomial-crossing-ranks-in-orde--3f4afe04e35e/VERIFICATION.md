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

The standalone `checker.py` was run using Python 3. It enumerated all actual partial translations for chain sizes 1–8 and compared ordinary composition for every ordered pair, checking monoid sizes, idempotent commutators, the exact rank polynomial for exactly-one-idempotent pairs, and binary residue-chain partition functions. It returned `ORDER_DECREASING_PARTIAL_ISOMETRY_COMMUTING_OK`.

This is finite verification only. For the infinite-family theorem the independently stated mathematical proof establishes unique shifts, exact transfer-matrix enumeration, disjoint local commuting constraints, the geometric tail bound, and the asymptotic estimate. An independent external mathematical audit has not been performed.
