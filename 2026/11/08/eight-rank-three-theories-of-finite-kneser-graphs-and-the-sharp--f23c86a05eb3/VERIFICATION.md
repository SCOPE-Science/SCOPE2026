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

The normal finite checker is included as `checker.py`. It ran with the standard Python interpreter and returned:

`KNESER_RANK3_ALL_FINITE_CHECKS_OK cases= 138 classes= 8 largest_bruteforce_vertices= 5005`

The script enumerates every permitted intersection orbit for parameter pairs up to \(n=17\) with at most 6000 vertices, compares actual third-vertex adjacency patterns against the theorem, and checks all pair types for the eight smallest representatives. It also checks exact boundaries in the three nontrivial regimes.

The infinite theorem is **not** established by these bounded enumerations. The proof rests on the quantifier-rank-three EF reduction, explicit existence of the three basic adjacency patterns, and the \(n\ge3k-t\) criterion for the fourth. The claim covers all positive integral parameters. No independent mathematical validation has been performed.
