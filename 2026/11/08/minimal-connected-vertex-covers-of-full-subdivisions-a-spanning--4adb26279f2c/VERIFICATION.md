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

Run `python3 verify.py` in the directory containing the standalone file. It has no nonstandard dependencies.

Observed output:

```
VERIFY_OK all_labeled_graphs_by_order={3: 1, 4: 10, 5: 253} graphs=264 base_examined_subsets=1165880 bipartite_examined_subsets=149756 total_examined_subsets=1315636 minimal_sets=12695 exact_family=PASS bipartite_specialization=PASS
K2,n coefficients: {2: {7: 8}, 3: {9: 27, 10: 2}, 4: {11: 108, 13: 2}, 5: {13: 405, 16: 2}, 6: {15: 1458, 19: 2}}
```

For orders three through five, every labeled connected input graph with minimum degree at least two was checked. The program independently enumerates all vertex subsets of each full subdivision, tests edge coverage and induced connectivity, and computes inclusion-minimality via single-vertex deletions. The proof establishes that connected vertex covers are upward closed, making this minimality test sufficient. It separately constructs all admissible independent omitted sets and spanning trees and compares exact sets. At the bipartite specialization it exhaustively checks all subsets for \(q\le5\) and compares the generated full family for \(q=6\). These tests are finite only; the unrestricted proof is in RESULT.md. The independent-audit field is unperformed.
