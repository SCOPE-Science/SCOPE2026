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

# Verification notes

Reproduce the independent SciPy-based numerical checks using `python verify.py`. The program verifies the exact \(J_0\) Bessel integral relation, independently checks analytic transforms of the Pareto survival function at all three marginal indices, computes the positive constant \(G(1)\), and compares 9 small-\(s\) renewal-Laplace evaluations to the analytically predicted leading terms. All 29 assertions passed at packaging. The convergence of ratios is logarithmically slow, so these samples are not themselves proofs of an infinite-time limit. The mathematical proof is the exact renewal decomposition plus monotone Tauberian inversion for the first two rates and the renewal-density convolution argument for the third.

The proof requires infinite volume first, unit hopping rate in both directions, instant global step-reset and independent Pareto waiting times of minimum length \(t_0>0\). It does not establish finite-size uniformity or critical waiting laws with arbitrary slowly varying factors.
