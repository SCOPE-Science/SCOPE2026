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

# Reproduction

Run `python3 verify.py` with Python 3. The program uses only the standard library and requires no dataset download. It was executed from the delivered file set and produced:

```
DIRECT_PERIOD_CHECK_OK 8855
RATIONAL_GF_CHECK_OK lengths=3..36
SHARP_MAXIMUM_AND_HALF_LIMIT_OK
```

The direct checker enumerates all intervals and candidate least periods in each word, independently of the four-gap formula, for every word with three ones and length from three through twenty-two. The second checker expands the rational generating function using truncated polynomial arithmetic and compares all run-count coefficients with direct quadruple enumeration through length thirty-six; the six-run closed generating function and its first attainment are checked independently as well.

These finite computations are **not** proofs of the universal classification, rational identity or limit law. Those results follow from the periodic-block lemma, gap partition and coefficient asymptotics provided in `RESULT.md`. Independent audit and external validation have not been performed.
