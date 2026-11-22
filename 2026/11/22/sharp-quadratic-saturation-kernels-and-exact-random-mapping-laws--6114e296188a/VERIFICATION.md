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

# Verification and limits

Run `python verify.py` from the directory containing `verify.py` and the six documents; it requires only the Python standard library. The actual run printed:

```
VERIFY_OK 84 counts_d1 [0, 0, 2, 18, 174, 2100, 31030] counts_d2 [0, 0, 0, 0, 0, 180, 4500]
```

The program implements exact rational truncated EGF arithmetic and independently enumerates all functions on sizes 1 through 6 for each depth 1 through 3, checking every equality profile. It also tests 66 canonical extremal functions across depths 1 through 11. An additional independent coefficient inspection matched \((d^2+1)!(2d-1)/d\) at depths 1 through 5.

The proof, not the experiments, establishes all infinite-depth-family assertions and the fixed-depth asymptotic. The random limit uses the standard square-root singularity of the labelled rooted-tree EGF, not numerical extrapolation. No external proof certification or independent audit has been undertaken.
