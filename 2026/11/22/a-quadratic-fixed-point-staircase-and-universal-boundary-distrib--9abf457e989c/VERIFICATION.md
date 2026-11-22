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

The analytic proof in RESULT.md derives the complete fixed-point count, one-sided eigenvalues, integer-border jumps and Wasserstein estimate for the stated domain. The accompanying Python 3 checker is independent of floating-point evaluation and uses fractions.Fraction; run `python3 verify.py`.

Actual check: PASS for 18 rational gain values, including the three high-gain cases 64, 255 and 511/2; 71,115 explicitly constructed finite fixed points; 71,861 exact comparisons overall; the resonance curve checked at five rational points; integer-row mass differences checked for gains 2 through 39. The checker tests sampled parameters only and is not an exhaustive numerical search over arbitrary real K. The universal claims rest on the written proof. The checker was executed successfully from its packaged copy. No claim of independent validation, full-state census or security testing is made.
