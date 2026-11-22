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

# Finite verification and proof boundaries

The source-free executable `verify.py` was run with Python 3 in the presence of the seven packaged files. Successful output:

```text
SQUARE_FRUSTRATION_AND_ORTHOGONALITY_PASS
ALL_65536_EVEN_SPIN_PATTERNS_PASS [((8, 8, 0), 10240), ((10, 5, 1), 45056), ((12, 2, 2), 10240)]
PARTITION_COEFFICIENTS_PASS total= 4294967296 energy_levels= 33 ground= 10240 next= 126976
NEGATIVE_EDGE_MINIMUM_24_AND_5120_DISTINCT_SIGNINGS_PASS
VERIFY_OK
```

The checker tests every negative square, confirms \(B^TB=5I\), exhaustively enumerates all \(2^{16}\) even-side assignments, constructs the total Laurent polynomial through integer convolutions, and checks total mass, top two coefficients, symmetry and randomly selected direct signed-edge sums (deterministic specified samples). The unrestricted identity is **proved** by the orthogonality and pair-event inclusion-exclusion argument in `RESULT.md`; the enumerator is a check on arithmetic rather than a replacement for proof. No claim is made about arbitrary dimensions, nonzero magnetic field, exhaustive historical novelty, or independent mathematical review.
