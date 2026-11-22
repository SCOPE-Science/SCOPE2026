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

# Reproducibility and mathematical verification

The main inequality is analytic and valid in all integer spatial dimensions \(d\ge1\). The accompanying `verify.py` carries out exact symbolic identities for \(d=1,\ldots,8\) and checks a noninfinitesimal clipped tensor-pair near the equality construction for \(d=2\). Command: `python verify.py` (requires `sympy` and `numpy`).

Critical non-computational steps: the simplex mass identity; firm nonexpansivity and rank-one positive-contraction representation for an arbitrary input pair; the Kantorovich/Wielandt projection metric bound; exactly realizable rank-one nodal spectral clipping along commuting perturbations; and active-set optimization for the scalar case. Numerical agreement alone is not used to extrapolate beyond checked dimensions.

The proof is a self-review only. No independent mathematical or historical-priority certification has been performed.
