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

The accompanying standalone `check_monge_shortest.py` checks exact matrix entries, pair distances, minimizer counts and their index labels with rational arithmetic. The executed command was `python3 check_monge_shortest.py`, yielding:

`MONGE_MINIMUM_VERTEX_SEPARATION_CHECKS_PASSED n_range=3..33 all_pairs=973896 direct_matrices_pairs=1386`

The explicit matrix replay covered all pairs for \(3\le n\le9\); the formula-level exhaustive replay covered all pairs for \(3\le n\le33\). The analytically verified quantifiers extend to every integer \(n\ge3\); the program is corroboration only. The normalization counts both off-diagonal symmetric entries. No external or independent audit is asserted.
