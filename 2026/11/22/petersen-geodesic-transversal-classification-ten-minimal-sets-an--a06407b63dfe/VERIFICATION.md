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

The proof reduces all maximal Petersen geodesics to thirty triples and characterizes feasible vertex subsets through an elementary forbidden-subgraph lemma on five ground vertices.

Run `python3 verify_petersen.py` with Python 3 (standard library only). Successful execution reports `PETERSEN_GEODESIC_VERIFY_OK` and lists the complete counts, component sizes and symmetry classes.

The program reconstructs graph distances by breadth-first search, tests all 1024 vertex subsets against thirty graph-derived two-edge paths, compares with the independent star characterization, derives coefficients using inclusion-exclusion, checks permutations of the five base labels, and builds single-addition/removal reconfiguration graphs at budgets four through seven.

These checks are finite exhaustive tests for this fixed graph. They do not certify historical publication priority or constitute an independent mathematical audit.
