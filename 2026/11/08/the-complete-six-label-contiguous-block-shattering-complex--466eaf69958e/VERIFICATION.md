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
# Reproduction
Execute `python3 interval6_verify.py interval6_orbits.json interval6_witnesses.json` using standard Python 3. The executable regenerates all 720 orders, deduplicates reversal-related patterns into 360 Boolean concepts, independently compares sliding-window and position-span predicates, enumerates every shattered support by exact bitmask splitting, checks all facet orbits and all-positive boundary ranks, and checks an explicit 32-row witness table. Output begins `INTERVAL6_SHATTER_PASS` on success.

The enumeration is complete for six distinct labels and 56 nontrivial subset queries. It supplies no evidence of an unrestricted formula for general numbers of labels. No independent audit was performed.
