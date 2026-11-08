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

The mathematical proof in `RESULT.md` is the basis of the universal claim. The critical analytical steps are (1) invertibility of the Brownian Green kernel via its Dirichlet–Neumann boundary conditions, (2) the exact nonlinear oscillator energy integral and odd-quarter-period endpoint rule, (3) strict monotonicity and range of the quarter-period map, (4) its small- and large-amplitude limits, and (5) the free-energy spectral, entropy, existence, and positive-kernel arguments. These steps establish all inverse temperatures and all nodal indices without numerical extrapolation.

Execute `python3 check.py` with Python 3 and the standard library. On the reviewed implementation it reports `PASS 147 numerical consistency checks`. It numerically compares Simpson-evaluated quarter periods against critical and large-amplitude asymptotics, integrates the nonlinear ODE independently with fourth-order Runge–Kutta, and verifies its Neumann endpoint, extrema, nodes, total magnetization, and the original graphon integral equation for selected amplitudes and indices. The numerical tolerances appear in the checker. Finite numerical checks do not prove the universal classification.

The exact source dates and scientific claims used for comparison are documented in the references. The preexisting graphon fixed-point and spectral principles are not claimed as new. Appendix C of Searle–Tindall (2023), including the growing-uniform-attachment graphon \(W(x,y)=1-\max\{x,y\}\) and its semilinear boundary equation, was inspected and is credited as the same kernel under coordinate reflection; unindexed global classifications may still affect priority. No finite-size dynamical or metastability result is asserted.
