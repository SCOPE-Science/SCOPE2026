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

The checked objects are explicitly defined 16-vertex undirected loopless graphs and the synchronous open-neighborhood NOR map. The `verify_direct.py` script exhausts all \(65536\) initial states in each of the two graphs, constructs the complete update function using bitwise neighborhoods, checks the idempotent-two-step relation \(F^3=F\), and computes every recurrent orbit and basin size. The `verify_structural.py` script independently calculates row/column occupancies for the rook graph, verifies the two-sided bipartite incidence isomorphism, computes the same image supports, checks independent domination via subsets of sizes three and four, and checks the exact recurrent support-pair counts.

Executed commands:

```
python3 verify_direct.py
python3 verify_structural.py
```

Both exited successfully and printed `ALL_CHECKS_PASSED` or `SIDE_ISOMORPHISM_AND_FIXED_CLASSIFICATION_PASSED`. The outputs, including 29 bivariate coefficients and all basin classes, are stored in `direct_output.txt` and `structural_output.txt`. No unverified external arithmetic data or missing file dependency is used. The finite proof covers every configuration of the two named graphs; it establishes no corresponding general statement for other graph pairs. External historical priority and independent review have not been established.
