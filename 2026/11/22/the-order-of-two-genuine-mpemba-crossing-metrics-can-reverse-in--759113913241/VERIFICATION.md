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

Run `python3 checker.py` in the same directory. Python 3 standard library only; no random seeds or external datasets. The script checks exact fractional stationarity and eigenvectors, stationary-weighted mode orthogonality, the variation formula at four fractional mode times for multiple Gibbs preparations, two exact squared Hilbert crossover fractions, two total-variation crossover fractions, their positive-part activation inequalities, and exact opposite strict crossover ordering. Printed decimal times are expository; only Fraction equalities/inequalities determine acceptance.

The universal uniqueness theorem is separately proved in `RESULT.md` by the monotonicity of the positive-part hinge difference and the exact two-mode decomposition. Finite exact tests do not substitute for this proof. Literature comparisons establish only bounded best-knowledge originality; no independent external validation or priority certificate is asserted.
