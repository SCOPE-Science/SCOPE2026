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

The algebraic proof uses the renewal resolvent and an explicitly invertible block-Schur complement. The homogeneous matrix is nonsingular for every positive Laplace parameter, so affine-hull dimensions are preserved for arbitrary parameter families. Laplace-transform uniqueness identifies complete joint finite measures, while a finite-dimensional nullspace construction disproves finite-rate identifiability.

`verify.py` was run using Python 3 and NumPy; it passed 210 deterministic numerical consistency checks on gamma waiting-time networks, affine and nonaffine perturbation families, and matrix-rank preservation. These finite computations only corroborate the formulas; they are not a substitute for the general proof.

The reconstruction assumes complete ideal occupation data and exactly known background kernels. It does not establish stable recovery under noisy data or numerical Laplace inversion. Independent audit has not been performed.
