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

# Verification notes

The exact proof in `RESULT.md` establishes all quantifiers and boundary cases. Execute `python3 verify.py` using Python 3's standard library. The program enumerates full permutation groups \(S_4\) through \(S_8\) independently of the analytic cycle-count formula; checks the signs of the proposed irreducible character and its mean and square mean; compares the direct convolution row norm with the forbidden-short-cycle formula; and separately checks exact rational cycle-exclusion coefficients for \(0\le m\le14\).

The observed final line is `ALL_SECOND_SPECHT_PROJECTION_CHECKS_PASSED`. This is an ordinary reproducible computational check, not a proof for unbounded \(n\). In particular, minimality among **all** projections relies on the analytical left-right averaging argument, and the limit uses the full generating-function argument. Independent audit has not been performed.
