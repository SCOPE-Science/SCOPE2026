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

Run `python3 verify.py` with a Python 3 standard-library interpreter. No downloads, third-party packages, random seeds, or network access are needed. Successful execution reports `PASS 425 exact arithmetic assertions`.

The checker independently enumerates weighted words that create a new covered window for small alphabet sizes and compares their exact rational probabilities against inclusion–exclusion. It checks the published uniform Stirling-number specialization, the product formula at the shortest possible window, exact two-symbol formulas, the \(M=4\) algebraic extremum, analytic derivative sign brackets, and strict unequal-sampling advantages for several nontrivial windows. A separate method computes the coefficient of a quadratic perturbation directly in the polynomial and compares it with the closed-form word-count Hessian over a family of finite parameters.

These finite checks do not establish the infinite integer quantifiers, global root uniqueness, or asymptotic statements. Those claims rest on the supplied mathematical proofs. The historical-priority search was selective, and no independent audit is asserted.
