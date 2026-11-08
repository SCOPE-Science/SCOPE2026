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

The theorem is proved analytically in `RESULT.md` by a universal centered Rayleigh quotient, a telescoping eigenvector flux identity, the Sturm nodal count for positive tridiagonal path Laplacians, and the equality case of the Rayleigh principle. These ingredients cover every integer \(m\ge2\), every positive real \(B,u\), and every asymmetric, symmetric or nonnegative budget-feasible assignment. They also establish uniqueness rather than merely local stationarity.

The included `verify.py` uses Python 3 standard-library exact rational arithmetic. Run with `python3 verify.py` in the package directory. In this review it printed `VERIFY_OK 9911`. The code checks a range of path orders, cap-phase parameters, budget identities, eigenvector equations, flux identities, Rayleigh quotients, the eigenvalue's Sturm location, and the concrete six-vertex example. It does not purport to exhaust an infinite parameter family.

The uncapped path optimum is earlier mathematics and is not a novelty claim. Source comparisons are recorded in `REVIEW.md` and `AUDIT.json`; one relevant older fixed-edge article could be examined only through its abstract and remains a publication-priority risk. This package has received a self-review; an independent mathematical audit has not been performed.
