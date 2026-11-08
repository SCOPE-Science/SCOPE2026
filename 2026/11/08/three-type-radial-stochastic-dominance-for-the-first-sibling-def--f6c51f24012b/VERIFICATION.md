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

The symbolic verifier `verify.py` recalculates the derivative of the exact tail probability, reduces it to an explicit rational polynomial, and asserts 79 positive coefficients with total degree 12. It independently computes probabilities using an exact rational absorbing-state recurrence on the capped counts 0,1,2, for every positive integer rate triple in `{1,...,6}^3` (216 triples); it also verifies 12 strict sampled ray comparisons. The proof of the continuum assertion is the rational positivity identity reproduced in `CERTIFICATE.md`, not the finite sample checks.

Run using Python 3 with SymPy 1.13 or later: `python verify.py`. No simulations or external files are needed.
