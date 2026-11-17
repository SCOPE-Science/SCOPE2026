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

# Reproducibility and verification

The complete claim is in `RESULT.md`. The two included self-contained Python 3 scripts require only the standard library and can be run independently:

```
python3 code/transfer_certificate.py
python3 code/direct_check.py
```

`code/transfer_certificate.py` constructs the 256-state graph of temporal state pairs and the 16-state fixed-state graph from their five-site update inequalities. It evaluates their exact integer trace differences for \(n=7,\ldots,290\), for deletion of either a distance-one or distance-two edge. It checks each asserted formula and 272 consecutive equalities between the trace differences at arguments \(n\) and \(n+12\), for \(n=7,\ldots,278\). Because the two trace sequences satisfy the characteristic-polynomial recurrences of matrices of dimensions 256 and 16, the difference satisfies an order-at-most-272 recurrence. Thus 272 consecutive zeros of the twelve-step difference imply all subsequent zeros, proving the periodic exact formula for all \(n\ge7\). These computations use unbounded Python integers, never floating-point or a timeout-as-proof inference. The actual output appears in `evidence/transfer_run.txt`.

`code/direct_check.py` constructs the graph by inspecting pairwise cyclic distances and deleting the specified bond. It separately applies the local majority rule to every binary configuration of sizes seven through sixteen for both deleted-bond distances. It counts fixed states and distinct unordered primitive two-cycles, thereby checking 261888 binary initial configurations in total. Its actual output appears in `evidence/direct_run.txt`.

The direct enumeration is only a finite cross-check. The infinite-family assertion relies on the exact transfer-to-dynamics correspondence and the finite characteristic-polynomial argument. Neither script is an external independent review, and no external validation has been performed.
