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

# Reproducibility and limits

Run `python check_ultrametric_haar.py` using Python 3 and only the standard library. The script uses exact rational arithmetic and computes signed Haar kernels and tree-flow transportation norms without calling the Bellman recurrence for the kernel comparison. It exhausts all 128 node-sign choices and all 28 unordered leaf pairs for three independent depth-three radius configurations; it also checks the depth-two configuration and enumerates all 256 path-sign strings through depth eight.

The observed diagnostics were:

```
EXACT_SIGNED_HAAR_ROW_BELLMAN_PASSED depths=1..8
EXACT_ALL_TRANSFORMS_AND_PAIRS 2 48 optimal 1 per-depth ['1', '1']
EXACT_ALL_TRANSFORMS_AND_PAIRS 3 3584 optimal 5/4 per-depth ['5/4', '1', '1']
EXACT_ALL_TRANSFORMS_AND_PAIRS 3 3584 optimal 11/10 per-depth ['11/10', '1', '1']
EXACT_ALL_TRANSFORMS_AND_PAIRS 3 3584 optimal 5/4 per-depth ['5/4', '1', '1']
ALL_EXACT_ULTRAMETRIC_HAAR_CHECKS_PASSED
```

The depth-two count is \(8\times6=48\), and each depth-three count is \(128\times28=3584\). These tests corroborate the finite norm identities but are not an exhaustive verification of all dimensions or all positive real radius profiles. The general finite and infinite assertions rely on the analytical argument in `RESULT.md`. Independent validation of the mathematics has not been performed.
