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

# Reproducibility

Run `python3 verify.py` using Python 3.8 or newer with no third-party dependencies. The checker independently constructs finite prefixes long enough to contain every length-\(n\) factor for each tested pair, canonicalizes by reversal, checks the exact formula for bases 2 through 10 and lengths 1 through 150, checks the binary simplification for lengths 4 through 100000, and checks 18 large-scale ratios. Expected console output:

`VERIFY_OK brute_cases=1350 base2_formula_cases=99997 asymptotic_cases=18 total_checks= 101365`

The full result is proved symbolically in `RESULT.md`. Although each tested finite factor census is exhaustive at that length, a finite number of lengths does not prove an infinite-length assertion. The source analysis is self-review; there is no independent mathematical audit.
