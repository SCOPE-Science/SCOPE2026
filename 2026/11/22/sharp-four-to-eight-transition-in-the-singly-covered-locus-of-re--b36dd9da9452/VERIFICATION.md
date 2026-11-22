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

# Verification and limits

The analytic proof is self-contained in `RESULT.md`, including the exact disk-membership condition, angular quadratic, component classification, polar integral and local singular expansion. `verify.py` is a separate standard-library Python 3 checker. Running `python3 verify.py` in the containing directory passed exact-fraction identities, direct membership counts on 600-by-600 midpoint grids at ten aspect ratios, independent polar quadrature, transition-root checks and cusp-coefficient comparisons. Direct grid estimates differed from the exact fraction by less than 0.0003 in the tested cases; the polar integrals agreed to better than 5e-8. Numerical checks are finite and cannot certify the continuum theorem, whose proof is analytic. Source comparison is not exhaustive historical priority, and no independent audit has been performed.
