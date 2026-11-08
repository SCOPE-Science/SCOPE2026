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

# Verification record

The supplied `checker.py` was executed with Python 3 and completed with `TRIPLE_DEPENDENCE_RECTANGLE_CLASSIFICATION_OK`.

The finite certificate checks all 65536 distinct four-Boolean-variable teams, obtaining exactly 64591 satisfying teams and the minimal false-team histogram \(\{11:48,12:4,13:240\}\). An implementation of matching by augmenting paths, logically independent of the rectangle-enumeration implementation, checks all 292 minimal false teams and every one-cell deletion, 3211 deterministically sampled other four-by-four teams, and all teams of sizes one-by-four, two-by-two, two-by-four, and three-by-three. It also confirms a pair of teams with identical ordinary four-Boolean-variable functional-dependency theories but different three-way-splitting truth.

The general matching equivalence is established mathematically using Hall's theorem. The complete finite classification and numeric polynomial are proved by the capacity/rectangle support argument, not inferred from a handful of tests. No claim is made about independent replication, external formal certification, domains larger than the specified four-bit matrix, or historical priority beyond inspected literature.
