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

**Analytic checks.** Decompose each observation as a fair sign times an independent magnitude and derive the conditional cumulants of their signed sum. Expand the fourth central moment, including the mixed covariance of the sum of squares and the square of the signed sum. Use the fourth moment of a sum of fair signs to identify the intercept, the variance fraction, and the covariance with the squared sign imbalance. The strict positivity of the conditional-variance slope for nonconstant magnitudes follows from a positive independent-copy expectation.

**Executable check.** Execute `python3 checker.py` using standard Python. It enumerates all finite samples for several explicit symmetric distributions with rational atom probabilities and verifies 516 exact first- and second-moment assertions. This corroborates, but cannot replace, the all-\(n\) proof.

**Limits.** No certification by an independent auditor has been performed. The result requires iid symmetry about the prespecified origin, no zero atom, and finite fourth moment. Conditional moments are not a claim of stochastic ordering of the full conditional laws. Statistical-test optimality and complete historical priority are not certified.
