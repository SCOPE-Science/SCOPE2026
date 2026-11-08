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

# Computational and analytic verification

The standalone `verify.py` requires Python 3 and SymPy. Running `python verify.py` reconstructs the endemic equilibrium and differentiates the original nonlinear vector field; it checks the exact trace, determinant, discriminant endpoints, and one nonsemisimple critical Jacobian, followed by 180 exact-rational parameter tests. The output observed was:

`PASS: symbolic equalities, exact critical Jordan example, 180 exact-rational parameter checks.`

The unrestricted statements follow from the algebraic and local-dynamical proofs in `RESULT.md`; finite parameter tests cannot replace those proofs. The verification does not test a global finite-time optimality claim or an infinite stochastic population limit, because neither is asserted. The negative eigenvalue at the optimum has a Jordan block, and a polynomial prefactor is expressly retained in the interpretation of spectral decay.
