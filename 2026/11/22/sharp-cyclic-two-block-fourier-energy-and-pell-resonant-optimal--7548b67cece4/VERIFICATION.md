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

# Verification

The exact theorem and proof, including all quantifiers and boundary restrictions, are in `RESULT.md`. Execute the accompanying `CHECK.py` with Python 3 and no third-party packages. The code forms raw ordered pair-sums directly and compares all admissible shifts for 504 pairs of parameters. It also tests 500 integer Pell/tie equivalences, and uses direct convolution at larger Pell witnesses with adjacent competitors.

Observed checker output:

```
PASS: two larger Pell ties verified by direct convolution and adjacent competitors
PASS: 504 exhaustive (n,a) cases with direct ordered two-sum counts
PASS: 500 independent exact tie/Pell checks and three named ties
Note: finite tests do not prove the universal theorem.
```

The infinite generality is justified by the convolution identity, nonnegative-packet packing argument, discrete correlation monotonicity, triangle-tail identity, integer first differences, and negative Pell equation in the proof, not by finite test coverage. The result does not establish optimal spacings outside its stated near-threshold window, nor has independent mathematical audit been performed.
