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

# Reproducibility and limits

Run `python verify.py` using Python 3 and SymPy. The standalone program checks exact fixed-content word enumeration against the rational covariance formula, 2,061 exact finite assertions, the coefficientwise positivity identity with 65 strictly positive terms in the two nonnegative shift variables, a seven-term positive special case, and the symbolic square-root-scale limit. These outputs are same-model reproducibility checks; they are not independent auditing and no external certification has been performed.

The infinite-range sign conclusion follows from the polynomial identities proved in the mathematical text, not from finite enumeration alone. The identities are recomputed symbolically without floating-point arithmetic. The program does not assess novelty or completeness of the literature.
