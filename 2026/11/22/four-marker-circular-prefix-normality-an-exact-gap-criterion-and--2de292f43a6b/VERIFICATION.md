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

# Reproducible verification

Use Python 3 with no third-party packages. From the directory containing the files, run:

```bash
python3 verify.py
```

The check reconstructs binary circular words from nonnegative four-gap tuples, computes circular maxima directly at all permitted lengths, independently identifies all maximizing starting positions, and compares these with the claimed gap criterion. For total zero-gap sum \(t=0,\ldots,22\), it checks \(14{,}950\) tuples. For each \(t\), it divides the number of failing labeled gap tuples by four and compares that exact value against the coefficient of \(z^t\) in \(z^3/[(1-z)^4(1+z^2)(1+z+z^2)]\), using the recurrence with denominator coefficients \((1,-3,4,-5,6,-5,4,-3,1)\). It also verifies that the weight-five gap tuple \((0,2,0,0,3)\) has no valid phase despite having one adjacent extremal pair.

Expected output:

```text
VERIFY_OK: 14950 four-gap configurations; all exact root sets;
          23 generating-function coefficients; five-marker boundary.
```

These finite tests are sanity checks. The all-length root criterion, exact generating function, sharp four-to-five structural boundary and limit \(2/3\) are proved in RESULT.md, independently of any finite exhaustion. Independent validation has not been performed.
