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
# Verification of the equilateral farthest-projection basin theorem

The independent-audit channel has not been performed. The following checks are computational diagnostics supporting an analytical proof, not a replacement for it.

Run from the extracted package directory: `python3 verify.py`.

Expected exact output:

```
EXACT_RATIONAL_CAPTURE_AND_ORIENTATION_OK 50050
EXACT_DYADIC_BASIN_MEASURES_OK
EXACT_CAPTURE_TIME_DISTRIBUTION_OK
```

The checker performs exact rational iterations for 50,050 coordinate presentations on all three line types by symmetry, including external points, vertex preimages and midpoint ties. It verifies three-step returns of the two stated cycles; the first-entry and basin predictions for each sampled point; the cumulative measure identity for 15 dyadic scales; and probability normalization for 21 time horizons.

The proof checks necessary for the universal claim are the exact geometric projection factors, the sign-preserving half-edge contractions, the exterior sign-flip identity, the absence of nonperiodic recurrence, and the two distinct limiting basin frequencies. The source uses complete supporting lines. The finite checker has no power to exclude unsampled points, and there is no claim of external or independent certification.
