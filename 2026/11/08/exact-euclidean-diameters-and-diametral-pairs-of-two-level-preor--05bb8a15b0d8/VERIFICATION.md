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

The displayed universal diameter theorem is proved in `RESULT.md`. The accompanying self-contained checker `verify_preorder_diameter.py` uses only Python 3 standard-library integer arithmetic. Run it next to this document with `python3 verify_preorder_diameter.py`.

The checker independently generates points from the cube-plus-simplex representation, evaluates the original order-ideal inequalities, checks every pairwise Euclidean squared distance and the exact set and number of equality pairs for \(1\le m\le4\), \(2\le n\le5\), and independently enumerates actual lattice points directly from the inequalities for \(1\le m\le2\), \(2\le n\le3\). The observed result is `EXACT_CHECKS_OK 4983576`, with no assertion failures.

Exhaustive checking over these finite ranges does not constitute a proof for arbitrary \(m,n\); the all-dimensional result follows from the finite convex-hull representation and explicit distance inequalities in `RESULT.md`. No external proof assistant or independent audit has been used.
