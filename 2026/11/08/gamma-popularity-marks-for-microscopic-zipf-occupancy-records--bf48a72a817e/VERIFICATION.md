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

At ranks j~n^gamma (gamma=1/a), np_j=c(j/n^gamma)^(-a). Exact binomial rare-count asymptotics and two-label multinomial covariance give a concentrated conditional intensity m_n sum_j p_j 1{N_j(n)=r-1}; its diagonal variance is O(n^(-gamma)) on compact rank intervals and off-diagonal covariance O(n^(-1)). The probability of repeating an eligible label twice in the short future window is O(n^(-gamma)); conditional product Laplace functional differs from Poisson exponential by O(n^(-(1-gamma))). The resulting compact Lipschitz L1 rate is O(n^(-gamma/2)+n^(-(1-gamma))); tail estimates ensure finite global mass. Substitution y=cx^(-a) yields Gamma(r-gamma,1), independent uniform time; actual proof handles fixed R and exact Zipf only. Finite multinomial sanity checks verified but do not prove the asymptotic limits.

## originality

PASS

The Derbazi–Gnedin–Marynych full text proves short-window UNMARKED r-record times and conditional Poisson limits. Its push-forward to time cannot recover the rank j/n^gamma or gamma popularity marks; the submitted joint space/time intensity and a quantitative fixed-draw quenched Laplace bound are strictly more informative. Related 2026 outer-measure work is Gaussian/macroscopic. Best-of-knowledge original marked refinement with priority risk.

## value

PASS

Conditional record frequency composition is meaningful in Zipf species/vocabulary sampling: it predicts the normalized popularity rank of each rare new record and distinguishes classes by Gamma(r-gamma) shapes, a genuinely new observable absent from unmarked count convergence. The compact quantitative approximation offers useful finite-window error control.

The dated certificate retains the supplied scientific assessment, sources and limitations.
