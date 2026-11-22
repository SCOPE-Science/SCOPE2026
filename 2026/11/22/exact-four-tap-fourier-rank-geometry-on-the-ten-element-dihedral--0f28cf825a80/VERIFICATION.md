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

# Verification record

The self-contained theorem is proved in `RESULT.md`. The directly checkable parts are the nonzero coefficients, determinant-zero patterns and orbit transport. On the stated dependency versions, running

```sh
python check_dihedral.py
python check_regular.py
```

reproduces the outputs saved in `VERIFIER_OUTPUT.txt`. The first program uses exact symbolic/cyclotomic reasoning for all displayed coefficient witnesses; the second independently assembles left-regular convolution matrices and uses floating-point singular values to check all 210 supports and 1040 transported configurations. The numerical program is not used as an infinite or exact proof of absent ranks. The proof establishes the exhaustive implications between all scalar and two-dimensional Fourier-block singularity conditions. The algebraic witness calculations cover the entire finite rank table, and no external mathematical certification has been performed.
