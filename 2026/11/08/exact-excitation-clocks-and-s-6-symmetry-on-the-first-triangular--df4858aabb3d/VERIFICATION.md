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

# Reproducibility

Run `python3 src/verify.py` from the package root with Python 3, `g++` and C++17. The verifier uses only the embedded source and data, builds programs in a new temporary directory, and checks that re-execution regenerates the saved outputs exactly. The two full state-space analyses are independent algorithms (indegree peeling and forward-orbit traversal), not independent external audits.

Recorded checks: both methods classified all \(14{,}348{,}907\) base-three states; their four primitive-period cycle counts and all \(26\) nonzero joint entry-time/period cells matched. The longest transient was \(10\) steps, with \(1{,}440\) states at that time. The separate symmetry program checked every one of the \(270\) primitive 4-/7-cycles under all \(720\) label permutations and verified the three spatial orbits of sizes \(45,45,180\), their profiles, and uniform per-vertex excitations. See `data/checks.txt`, `data/raw_census.txt`, `data/forward_census.txt`, `data/representatives.txt` and `data/symmetry_results.txt`.

The exact result applies only to this finite graph and this update rule. These tests do not establish results for other graphs, nor do they constitute an independent audit.
