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

Run `python3 verify_k3n_spanning_shattering.py` from the package directory. Python 3 and the standard library suffice.

The program generates spanning trees independently from all candidate edge subsets using disjoint-set union. For each of the 37,448 possible supports across the five graphs with 1 through 5 right vertices, it compares the count of distinct induced tree traces against the full Boolean cube; it then verifies the structural criterion and every coefficient of the closed formula. It also checks the three parallel classes of the smallest nontrivial matroidal case and exhibits nonmatroid exchange witnesses for right-side sizes 3 through 8.

Expected final line: `K3N_SPANNING_TREE_SHATTER_PASS 37448 supports 2551 trees`.

These are exhaustive finite checks through five right vertices, not a proof by induction over all parameters. No independent audit was performed.
