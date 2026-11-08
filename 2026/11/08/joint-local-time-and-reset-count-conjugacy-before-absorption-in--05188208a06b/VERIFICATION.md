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

The analytical proof rests on the ordered-time Kac identity with a terminal-event mark, its regularized occupation-density limit, and independent geometric restarting. In particular, the one-cycle local-time law is exponential and *independent* of the cycle's terminal type. That step justifies the Gamma and Poisson conditionals without extrapolating from a marginal transform.

Reproduce by running `python verify.py` with NumPy and SciPy installed. The script solves three finite killed Ornstein–Uhlenbeck chains with 25 distinct pairs of occupation penalty and reset-count weight for each chain. It compares an explicit rank-one reset perturbation against independently computed killed absorption and Green resolvents and also checks continuum OU and free-Brownian closed formulas. The script reports 462 successful deterministic assertions.

The finite-chain discretization and OU quadrature are diagnostic calculations, not certificates of continuum local-time convergence. The proof uses the stated regular-diffusion/local-time hypotheses, which are stronger than bare nonexplosion. It does not address non-Poisson resetting, nonidentical reset and local-time points, random reset sites or nonstationary reset mechanisms. Independent scientific audit has not been performed.
