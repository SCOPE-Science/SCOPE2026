---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed exact independent Poisson-age OU maximum kernel R_{j+1}=exp(-kE/r)R_j+sqrt((D/k)(1-exp(-2kE/r)))M_N, with stationary contractive perpetuity. Beta-integral first and second moment equations give m_r=c_N sqrt(r)+O(r^-1/2) and v_r->(D/k)(nu_N-pi mu_N^2/4). Centered innovations have L2 limit H=sqrt(2DE)M_N-kc_NE; calculate variance 2D(nu_N-pi mu_N^2/4). Martingale triangular-array predictable variance and fourth moments yield Gaussian law, tail controlled; ordinary-time all-coordinate difference O_P(r^-1/2). Independent exact N=2 evaluation at D=1.7,k=.9,r=250: m=16.2116725068, variance=1.41624243337 versus limit 1.41666666667. Finite test is corroboration only.

## originality

PASS

Primary full HTML Lee–Yang–Park–Lizana gives renewal group reset, approximate large-N Gumbel kernel and sqrt(r) mean scaling; neither exact fixed-N maximum law nor complete high-frequency Gaussian variance coefficient with independent clock contribution is stated in the inspected results/appendix. Resultary also finds non-Gaussian stationary reset design and fixed-origin Brownian gas, which differ in the selected reset location. Standard random-affine/martingale CLTs alone do not provide this evaluated coefficient.

## value

PASS

Stationary high-rate distribution of collectively rightmost-reset OU groups is a natural stochastic invariant. Exact fixed-N shared Gaussian fluctuation, variance decomposition into maximum and clock terms, and explicit quantiles improve large-N mean/Gumbel approximations and clarify a model used in group avoidance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
