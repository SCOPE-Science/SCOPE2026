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

The infinite theorem is proved by a gap-generating-polynomial identity, exhaustive removable-limit cases at roots of unity, discrete Fourier inversion, a Chinese-remainder extremum argument and a quantitative bound for nonresonant Fourier modes. No exhaustive finite computation is used to infer the universal result.

To reproduce the separate-method finite checks, run `python3 check.py` from this directory. The checker uses Boolean dynamic programming for representability up to the known two-generator conductor, with no calls to the Fourier derivation or an Apéry counting routine. Its observed output was:

```
PASS discrepancy_cases 6266 a_shift_cases 4383 b_shift_cases 4383 arithmetic_histogram_cases 340
```

The tested ranges are moduli 2 through 14 and coprime generator pairs from 2 through 29. Only transfers retaining coprimality are tested. Finite tests cannot establish the unlimited ranges, and no separate independent mathematical validation has been performed.
