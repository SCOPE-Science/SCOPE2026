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

The standalone standard-library verifier `verify.py` reads the entire `chords.csv` witness table. For each of the 592 instances it independently computes every cyclic-arc sum and a valid family of chord-connected sums from two complementary paths. Complete bit coverage up to the exact triangular total establishes the upper bound. A separate unaugmented-cycle bitset check proves the lower bound. For sizes 8 through 14, exhaustive enumeration of all vertex subsets and actual graph traversal confirms that the constructive bitset equals the set of all connected-subgraph sums.

The following exact checks were executed on the finished verifier and CSV before package assembly:

```
VERIFY_OK range 8 300 instances 293 exact_integer=yes
VERIFY_OK range 301 450 instances 150 exact_integer=yes
VERIFY_OK range 451 525 instances 75 exact_integer=yes
VERIFY_OK range 526 564 instances 39 exact_integer=yes
VERIFY_OK range 565 599 instances 35 exact_integer=yes
```

These batches partition the full inclusive interval 8 through 599. All computations are finite and deterministic. The claimed equality has no meaning outside this range; no infinite extrapolation is made. Neither independence of audit nor external formal certification is claimed.
