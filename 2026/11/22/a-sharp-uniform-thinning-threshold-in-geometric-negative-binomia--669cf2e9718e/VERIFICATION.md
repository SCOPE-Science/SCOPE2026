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

# Verification record

The analytic proof in `RESULT.md` verifies the complex-root factorization and nonnegative logarithmic jump intensities for all positive mixture parameters and all rates, derives the discrete thinning criterion, and establishes the exact parameter boundary by an all-indices modulus bound together with a moving-index limit. The pure negative-binomial endpoints are handled separately.

Running `python3 checker.py` verifies, entirely with standard-library rational arithmetic, two independent finite representations of the canonical coefficients at the exact parameters \(p=1/5\) and \(q=99/100\). It checks agreement through coefficient index 31 and the negative thirteenth consecutive difference. This computation is a finite corroboration only, not an exhaustive numerical proof of statements with infinite quantifiers.

The parameter restriction \(\alpha\ge0\) ensures the original mixing components form a genuine convex mixture. The full fixed-rate admissible region is not claimed; historical priority is provisional. No independent audit or certification is asserted.
