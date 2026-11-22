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
Run `python3 verify_humbert.py` (only the Python standard library is required). The program exactly checks the four-variable alternant polynomial identity over the integers, Hasse binomial coefficients modulo five, separability of the three presented degree-four branch polynomials, and their derivative multiplicity patterns by polynomial gcd over an explicit quadratic extension of the prime field.

The accompanying `verification_output.txt` captures a successful replay. These computations verify critical algebraic lemmas and examples, not the general infinite-field geometric assertion by enumeration. The complete proof uses the Hasse–Wronskian transformation law, local parameter valuations at each ramification point, and global degree accounting, as written in `RESULT.md`. Characteristic-five nonclassical canonical weights are defined using the generic sequence, not characteristic-zero ordinary jets. Independent scientific review has not been performed.
