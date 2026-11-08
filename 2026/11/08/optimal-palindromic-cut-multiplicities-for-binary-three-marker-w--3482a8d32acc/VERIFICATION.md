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

# Reproducible checks

Run `python3 verify.py` with the Python standard library. Expected output:

```text
VERIFY_OK words=12650 direct_four_cut_checks=330 bivariate_lengths=3..100
MOMENT_AND_SHARP_SPECTRUM_OK
```

The dynamic program checks both the minimum number of palindrome blocks and their optimal multiplicities. For short words an independent direct enumeration checks all three cut positions. A separate gap-parameter summation checks the two-variable generating-function coefficients and the attainable multiplicities up to length one hundred; exact rational polynomial integration checks limiting mass, mean, second moment and variance. The unrestricted claims are proved analytically in `RESULT.md`; these finite checks do not establish them by exhaustion. No independent audit has been performed.
