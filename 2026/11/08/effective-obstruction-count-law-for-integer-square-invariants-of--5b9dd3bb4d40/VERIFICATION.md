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

# Exact arithmetic checks

Run `python3 verify_density.py` with the standard Python library. The program uses `Fraction` to check local masses on complete residue rings, integer gcd and modular powers to validate the first nontrivial recurrence-iterate divisibility test, exhaustive factorization of parameters through 100000, and `Decimal` to evaluate the limiting product. It checks 181482 local residues and 114554 coprime-start input pairs, and constructs 98 bad-start witnesses for the first 1000 parameters. The observed obstruction-count histograms are `{0:902,1:98}` through 1000, `{0:9026,1:947,2:27}` through 10000, and `{0:90140,1:9516,2:343,3:1}` through 100000.

The truncated probability generating function through primes at most 1000000 has its first four coefficients approximately `0.901295042913`, `0.094871179374`, `0.003758422268`, and `0.000074522047`; **each** has error at most `1/(2(1000001)) < 5e-7` from omitted primes, so these decimals are not offered as twelve-digit certified values. The rigorous probability law and its effective rate are proved symbolically in `RESULT.md`; finite tests do not certify infinite claims or literature priority.
