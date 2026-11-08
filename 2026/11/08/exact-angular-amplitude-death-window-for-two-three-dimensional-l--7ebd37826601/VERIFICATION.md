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

Run `python3 verify_window.py` using Python 3 with no nonstandard dependencies. The actual completed execution returned `PASS: 4096 exact rational checks (7 characteristic values and one Routh equivalence per case)`. This checks 512 rational parameter configurations and seven characteristic-determinant evaluations per case using exact Gaussian elimination over fractions, plus exact rational stability-condition comparisons.

## Meaning and limitations

The checker independently constructs each six-dimensional linearization from cross-product matrices and compares characteristic determinants to the two closed cubics. It then compares Routh-Hurwitz coefficient signs with the angular inequalities. These finite computations do not prove the claim for all real parameters. The RESULT.md proof supplies the all-parameter factorization via the exact exchange involution, all strict Hurwitz inequalities, and the elementary positivity argument. Near the strict equality boundaries, numerical signs may be delicate; no numerical floating-point eigenvalue test is used as a proof. Independent audit has not been performed.
