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

# Reproducible finite checks

Running `python3 verify_digit_tiling.py` on the supplied code using Python 3 standard library produced:

```text
PERIODIC_DIGIT_CHECK_OK tested_signed_integers= 145808 direct_finite_pairs= 1066728 bases=2..5 periods=2..5
MECHANICAL_SUPPORT_CHECK_OK tested_signed_integers= 10005
GAP_WITNESS_CHECK_OK lengths=2,4,8,12
VERIFY_OK exact_integers=yes finite_tests_only=yes
```

The periodic tests use the least-residue signed-digit recurrence and a separate direct Cartesian-product enumeration of all six-digit pairs for uniqueness. The mechanical-support tests use exact rational slopes. The gap tests check the predicted witnesses at four block lengths. These finite computations are consistency checks, not a proof of completeness for arbitrary supports or unbounded integers. The proof in `RESULT.md` independently establishes the infinite assertions using quotient recurrence, finite termination and explicit gap witnesses.
