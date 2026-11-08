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

Execute `python3 verify_star_pmms.py` with Python 3 and only its standard library. The saved execution produced:

```
CHECK_OK settings 83309 connected_partition_choices 1391766
ZERO_HUB_CLIFF_OK
```

The program independently enumerates legal center-leaf subsets, reconstructs each two-agent connected maximin share by enumerating which leaf is isolated, compares the predicted exact count, and computes the global leximin optimum over all connected choices. The systematic tests include all leaf-value tuples in `{0,1,2}` for 1 through 7 leaves and hub values in `{0,1,2}`; two additional larger sizes use a fixed pseudorandom seed. The reported count is of connected center-subset choices, not of labeled allocations. No finite enumeration proves the theorem for unbounded graph order or arbitrary real weights; that conclusion follows from the mathematical proof. Independent external audit has not been performed.
