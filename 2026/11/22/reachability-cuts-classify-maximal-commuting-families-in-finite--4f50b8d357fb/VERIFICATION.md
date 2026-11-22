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

Run `python3 verify_path_semigroups.py` in the same directory. The script uses only Python 3 standard-library modules, creates path sequences directly, tests semigroup concatenations, exhausts all commuting subsets in 79 DAG or multiquiver cases, and compares their maximal members to the cut construction. It also compares the centralizer of every nonzero element to the closed formula and tests the directed-line family count and maximum size through six vertices.

Observed output ended `PASS: 79 DAG instances; all maximal families and individual centralizers`. The explicit proof covers all finite directed acyclic multiquivers; the finite computations are independent corroboration only. Distinct parallel edges are retained as distinct paths. No independent audit was performed.
