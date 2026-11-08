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

# Reproducibility and verification

Run `python3 verify.py` with Python 3 and the standard library. The program constructs subsequence sets from the input words directly, checks maximality by every possible single-letter insertion (not merely a predicted length), checks the classification and palindromic subcount, and independently checks coefficients in the polynomial identity for the rational bivariate series. It prints:

`VERIFY_OK configurations=17 common_words=8323 maximal_words=3228 polynomial_cells=816`

The tested input pairs have alphabet sizes 2–6 and exponents 1–4 with input length at most 16. The rational-series coefficients are tested for alphabet sizes 2–7 through length 16. The checks are finite; the general theorem follows from the four proof steps in `RESULT.md`. No external software, private services, third-party papers or computational certificates are necessary to replay them. The known Smirnov descent identity is acknowledged as prior work. Independent audit: not performed.
