---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS — Oddness of increasing-branch F gives G^n=(-1)^nF^n and Q^n(u)=|F^n(u)| for Q(u)=|F(u)| (Q(0)=1), away from excluded cut. For odd n, nonperiodicity of critical/cut orbit gives H_n(0)=Q^n(0)>0 and H_n(1)=Q^n(1)−1<0; smooth monotonic laps and absence of neutral regular fixed points force a finite set of transversal crossings. Each decreasing fixed lap crosses H_n downward; increasing laps with slope below/above one cross downward/upward. The endpoint index yields D_n+S_n−R_n=1. The signed ± lifts imply a_n(F)=2(S_n+R_n), a_n(G)=2D_n, A_n(F)=2S_n; hence a_n(G)−a_n(F)=2−2A_n(F). Even n coincides. Summing over primitive odd attracting cycles yields the formal infinite product correction, coefficient-wise (no analytic convergence claimed). Explicit monotone real-analytic family F_K(u)=u−e^{−Ku}P(u), with 2k simple positive roots and K sufficiently large, has exactly 4k F fixed and 2 G fixed, hence defect 2−4k; this construction does not assert all-period noncriticality. Numerically sampled source checks are not proof; the crossing and monotonicity inequalities are the analytical argument.

## originality

PASS

PASS best of knowledge — Oliveira 2026 Theorem 10.3 proves only the uncorrected ratio (1+t)/(1−t) for **uniformly expanding** symmetric increasing Lorenz maps. Its argument's universal crossing index is background, but it does not cover maps with attracting regular cycles and the exact all-period correction, nor give analytic families with arbitrarily negative first-period defect. Anušić–Bruin–Činč studies unimodal/Lorenz correspondence without this identity. More general fixed-point-index and kneading determinant theorems may furnish an alternative derivation; no inspected prior explicitly states the same corrected quotient and sharp realization. Inaccessible/unindexed older sources remain a priority risk, not false evidence of absence.

## value

PASS

PASS — The sign-reversal zeta ratio is a meaningful dynamical invariant that ceases to be universal beyond uniform expansion; an exact correction by odd attracting cycles explains the failure and quantifies arbitrarily large negative first-period defects in analytic, monotone branches. The construction separates a robust general formal identity from a sharp counterexample family rather than just renaming Oliveira's expanding result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
