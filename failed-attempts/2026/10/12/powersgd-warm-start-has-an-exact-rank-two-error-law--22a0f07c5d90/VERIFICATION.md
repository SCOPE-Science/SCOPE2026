---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Induction gives the direction of p_t as U diag(sigma_1^(2t−1),sigma_2^(2t−1))z, where z is standard bivariate Gaussian on the two-dimensional right singular support. Normalization is well-defined almost surely and discarded factors are scalar. The reconstruction is the orthogonal projection p_t p_t^T M. Orthogonal decomposition gives normalized residual 1+(kappa²−1) times the squared second coordinate of p_t in the left singular basis, with the 1 outside the product. Write d=kappa^(2t−1). That coordinate-square is 1/(1+d²V²) for V=z_1/z_2, standard Cauchy. Its expectation is 1/(1+d) by partial fractions against 1/(pi(1+v²)); at d=1 the expectation is 1/2 by symmetry. This recovers the stated law, benchmark sigma_2², geometric-mean initial error, one-reuse ratio and large-gap orders. At kappa=1 any attained left direction is in the column space and loses precisely sigma_2²; the explanatory equality of errors across left lines should be read within that support, not as a claim about all ambient lines for rectangular M.

## originality

FAIL

The algorithm is prior and its fixed-matrix specialization immediately produces a bivariate elliptical direction. Dürre–Vogel–Fried's exact bivariate spatial sign covariance proposition already evaluates the whole normalized projector expectation, a stronger statistic than this one trace. Inserting the two scatter eigenvalues determined by the source iteration and taking that trace gives the full law mechanically. The later Resultary Gaussian power-sketch formula is also exactly equivalent; the decisive prior coverage does not depend on adjudicating dates between the catalog records.

## value

FAIL

Stationary compression is a motivated baseline, but this particular expected error is just the trace of the known bivariate normalized projector moment with the algorithm's scatter eigenvalues. The finding neither needs a new warm-start argument nor addresses moving gradients, noise, higher rank, or another non-mechanically-implied effect. The special values and asymptotics are algebraic re-expressions of the same covered fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
