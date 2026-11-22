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

# Reproduction and scope

Execute `python verify.py` using Python 3 with SymPy installed. The program checks symbolically that the displayed radial root solves the disk constraint, that its rationalized form is exact, and that the two parameter/angle derivative identities hold. It independently obtains area and polar second moment by midpoint integration of the pointwise minimum over all generating disk roots and compares them with the boundary-arc formulas for seven values of the polygon order and six center radii. It verifies sampled monotonicity and endpoint convergence solely as diagnostics. The performed execution printed `PASS: 151 independent symbolic and quadrature assertions`.

These computations support algebra and numerical reproducibility, but **do not** prove the continuous-parameter or infinite-order theorem: that proof is the strict comonotone-covariance identity plus uniform radial convergence in `RESULT.md`. The area and moment formulas are based on exact divergence-theorem identities. There is no independent mathematical audit at present.
