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

# Reproducible mathematical checks

Run `python VERIFY.py` using Python 3 and only its standard library. The script uses exact `fractions.Fraction` arithmetic; no tolerance-based numerical comparison is used. It passed 136 choices of dimension and endpoint scale and 17,308 assertions, including all 61 sampled parameter distances per case. The checks test strict contact classification and the positive-barycenter certificate in the three-contact regime.

The proof in RESULT.md, rather than finite evaluation, establishes the theorem over all real parameters and all compact parameter sets in the stated domain. In particular, the exact inequalities prove that no unexamined intermediate curve point can touch the sphere. The abstract and a secondary explanation of arXiv:2609.28417 were accessible, but the full primary manuscript was not; this limits only the literature-priority assessment. No independent mathematical audit has been performed.
