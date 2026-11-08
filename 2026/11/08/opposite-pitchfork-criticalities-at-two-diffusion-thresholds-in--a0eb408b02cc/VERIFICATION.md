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

Run `python verify.py` using Python 3 and `sympy` (tested against the available local installation). The verifier reconstructs the two reaction functions and checks the positive equilibrium, reaction Jacobian, graph Laplacian eigenvalue multiplicities, modal determinant factorization, critical left/right eigenvectors, center mean-shift coefficients, signed linear transversality coefficients, and signed cubic coefficients.

The cubic coefficients are checked in two ways: direct derivative-tensor contraction and exact series expansion of the original rational nonlinear functions. The local branch existence and stability statements rely on the proved simplicity of the critical eigenvalue and on standard analytic equivariant center-manifold and implicit-function theorems. These are not finite-state numerical assertions. The script does not establish global attractivity, nonlinear behavior far from the bifurcations, or publication priority. Independent audit has not been performed.
