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

# Verification and reproducibility
The proof in `RESULT.md` uses the exact Hardy–Stein representation and monomial orthogonality from the published source to derive the quadratic expansion. All smallness assumptions and quantifiers are stated there. In particular, the remainder estimate is uniform across bounded analytic functions small in both indicated norms. The strict eigenvalue ordering follows algebraically from the ratio of adjacent generalized binomial coefficients; sharpness is witnessed by \(1+t z^2\), not extrapolated from numerical tests.

Run `python CHECK.py` with Python 3 and `mpmath`. The script checks finitely many exact rational coefficient identities and high-precision sample perturbations, without asserting that finite checks certify the infinite theorem. No external or independent mathematical audit was conducted; the review is same-model only.
