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

# Verification details

The supplied `checker.py` was executed under Python 3 with `fractions.Fraction` and produced `Exact-rational assertions: 34659`. It checks both parameter values, 5 positive rational heights and 385 rational time samples per height, crossing all break lines. For each sample, the height formula, inverse-coordinate formula, one-step conjugacy, and four exact iterates were tested, as well as forward first-entry thresholds. Exact determinant checks at interior time points additionally establish the sampled Jacobian identity.

The all-real conjugacy, homeomorphism property, branch boundary behavior and two-sided asymptotic laws are deduced by the symbolic piecewise algebra in RESULT.md. Finite sampling cannot certify those quantified assertions on its own. The coordinate maps are nonsmooth at their branch seams. Independent audit: not performed.
