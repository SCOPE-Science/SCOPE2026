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

Run `python verify.py` with a recent SymPy release. The checker performs exact characteristic-zero Gröbner elimination, an independent discriminant calculation in the parameterized plane cubic, factor coprimality/squarefreeness and reduction-modulo-two irreducibility checks. It also tests the explicit critical-point ratios and the nonzero first-order smoothing coefficients. Each assertion executed successfully in the supplied environment.

These checks are finite symbolic identities, not a substitute for the geometric proof. The complete singularity count follows from the gradient classification including both projective endpoints; the local analytic type follows from the rank-three Hessian and a nonzero cubic normal term. The fourth-power discriminant follows from the order-two local discriminant of a transversal \(A_2\) deformation and is checked independently against the classical dual degree \(48\). The Galois assertions use the field-of-definition arguments in the proof.

No external or independent mathematical audit has been performed.
