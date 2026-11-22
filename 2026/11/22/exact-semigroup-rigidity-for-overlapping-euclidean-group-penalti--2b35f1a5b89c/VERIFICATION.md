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

# Reproducibility and verification

The complete analytic proof and all hypotheses are in `RESULT.md`. The included `checker.py` (Python, NumPy, SciPy) checks exact derivational consequences and numerical finite cases; invoke `python checker.py`. Its preparation-time execution returned `PASS: 1044 supplementary assertions; exact symbolic coefficients proved in RESULT.md`.

The checker verifies the exact small-instance Hessian-gradient identities to numerical precision; a direct symbolic differentiation of the two norms gives \(\nabla F=(1/\sqrt2,\sqrt2,1/\sqrt2)\), \(H\nabla F=(-1/4,1/2,-1/4)\), and \(\nabla F^{\mathsf T}H\nabla F=\sqrt2/4\). It also verifies convergence of the normalized finite-step split to that coefficient, all tested group families on at most three coordinates, sampled four-coordinate families, constructive unequal-ratio witnesses, and exact radial shrinkage for disjoint blocks.

No amount of numerical sampling certifies the all-dimensional iff statement; it follows from the positive-semidefinite Hessian argument and the explicit one-coordinate witness in the proof. The local \(O_x(h^3)\) remainder is justified by analyticity and the implicit function theorem near strictly positive inputs, not estimated by regression. Independent validation is not performed.
