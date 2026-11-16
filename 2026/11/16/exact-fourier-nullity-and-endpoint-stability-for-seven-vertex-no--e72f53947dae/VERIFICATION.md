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

# Exact arithmetic and reproducibility

The theorem concerns 21 binary edge characters and 1428 trees. The first checker enumerates all 16807 Prüfer codes and independently calculates the two Walsh transforms. The second checker enumerates all 54264 unordered six-edge subsets and independently validates tree connectivity and crossing exclusion. Both checkers use exact integer arithmetic, not floating-point zero thresholds.

Run `c++ -O2 -std=c++17 check_prufer.cpp -o check_prufer && ./check_prufer` and `python check_subsets.py` in this directory. The Python route requires NumPy. The two CSV tables are included with exact entries and verified by the Python checker. The recorded outputs were:

```
PRUFER_WALSH_PASS count=1428 zeros=160484 rank=1936668 min=4 gcd=4 twozeros=14 projection_l1_numer=312904152 projection_l1_denom=2097152
SUBSET_WALSH_PASS count=1428 zeros=160484 rank=1936668 gcd=4 min=4 pairzeros=14 projection_norm=39113019/262144
```

The first-stage Walsh Parseval identity is 2994733056. Every low-support zero is in the one 14-element two-chord orbit. The second-stage absolute sum is 312904152; dividing by the group size 2097152 yields the exact endpoint norm 39113019/262144. No unseen full group or other polygon sizes are claimed to have been checked. External independent mathematical validation has not occurred.
