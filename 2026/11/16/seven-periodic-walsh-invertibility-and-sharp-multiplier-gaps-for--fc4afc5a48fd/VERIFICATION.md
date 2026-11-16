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

The script `check_walsh_path_square.py` was executed from this package using Python 3 with no third-party dependencies. Exact integer computations checked the following independently of the all-length proof:

- Full recurrence versus direct signed independent-set enumeration for every sign assignment and every length from zero through ten (2,047 signed inputs).
- Complete integer fast Walsh transforms of the path-square independent-set indicators for every length from one through sixteen (131,070 Fourier coefficients), including Fourier-zero existence and exact least nonzero magnitudes.
- The complete list of 32 allowed seven-sign blocks and their first-row transfer identities, with a census over all 128 seven-sign words.
- All two-block concatenation witnesses for each of the three base zero words, and five deterministic long-witness chains per length through 201.
- Parity recurrence through length 1000.

Exact program output:

```
PATH_SQUARE_WALSH_EXACT_PASS direct_signs_n_le_10=2047 full_FFT_n_le_16=131070 seven_blocks=32 zero_seeds=1,3,4 min_seeds=0..6 long_witnesses_n_le_201 parity_n_le_1000
n=1..16 zeros: 1,0,3,6,0,0,0,59,0,188,369,0,0,0,3837,0
```

These tests independently corroborate the recurrence, parity criterion, construction and finite examples. The infinite classification is proved symbolically in `RESULT.md`; finite enumeration alone would not prove it. No independent external audit was performed.
