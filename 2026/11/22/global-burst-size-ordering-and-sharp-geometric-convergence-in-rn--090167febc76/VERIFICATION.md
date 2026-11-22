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

The analytic proof starts from Jia's Eq. (5) and shows exact normalization, cone preservation, strict comparison of every tail and optimal-order total-variation convergence. No finite sampling is treated as an infinite proof.

`python CHECK.py` (Python 3.10+ with SymPy) reconstructs the defining matrix and checks 6,000 deterministic, exact-rational comparisons, including varying threshold and initial count, as well as symbolically checking the defining cone/derivative identities, limiting matrix and the exact first-tail formula. The boundary case of complete translation repression is explicitly included. All checks passed when run from the package file.

Limits: finite tests do not independently validate the fast-mRNA approximation, historical originality, or biological accuracy. The total-variation rate is sharp as an order, not as a globally optimal upper constant. Independent audit has not been performed.
