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

The complete analytical derivation is in `RESULT.md`. The included `verify.py` script requires only Python 3 standard-library modules and can be replayed by running `python3 verify.py` from this directory. Its observed output for this result was:

```text
DIRECT_SLIDING_WINDOW_OK 33649 N_4_TO_22
EXACT_FIBER_AND_SECOND_MOMENT_OK N_4_TO_200
ASYMPTOTIC_CONSTANT_FROM_POLE_OK 32
ALL_CHECKS_PASSED
```

The first check directly enumerates all \(33{,}649\) length-\(4\)-through-\(22\) binary words of Hamming weight four and independently computes factor maxima by prefix sums; it compares actual equivalence classes to the proposed parameterization. The second recomputes exact integer coefficients of the rational second-moment generating function and the sharp maximum through length \(200\). These are finite consistency tests; the all-length conclusions rely on the constructive proof and generating-function identities in `RESULT.md`.

No result on full factor-Parikh-set equivalence is asserted. Independent mathematical audit is not performed.
