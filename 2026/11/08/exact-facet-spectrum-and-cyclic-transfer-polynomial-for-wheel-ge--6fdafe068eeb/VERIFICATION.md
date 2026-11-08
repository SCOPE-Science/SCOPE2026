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

The executable `verify.py` uses standard-library Python 3 and directly enumerates every subset of independently constructed wheel graphs for rim orders 4 through 11. It measures pairwise shortest-path distances and tests every selected triple using the original geodesic equality, not an assumed run characterization. It independently checks the binary-word predicate, inclusion-maximality, transfer-polynomial recurrence and exact size spectra up through rim order 17.

Run: `python3 verify.py`.

Recorded actual execution output:

```
VERIFY_OK rim_orders=4..17 rim_masks=262128 valid_rim=69134 rim_facets=1071 brute_wheels=4..11 wheel_masks=8160 independent_geodesics=PASS cyclic_runs=PASS rational_recurrence=PASS spectra=PASS
```

The complete ranges of masks, arithmetic comparisons and geodesic computations are implemented directly in that file. The output does not constitute an infinite proof; the unrestricted argument is contained in `RESULT.md`. The first two polynomial recurrence coefficients correspond to formal cycles of length below the wheel scope. The analysis does not establish priority beyond the literature and database comparisons described in the review.
