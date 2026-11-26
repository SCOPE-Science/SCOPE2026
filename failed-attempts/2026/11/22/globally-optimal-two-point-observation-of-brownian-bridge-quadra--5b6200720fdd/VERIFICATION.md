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

At fixed sites the orthogonal L² projection is the conditional mean. The pinned Markov decomposition is piecewise-linear interpolation plus independent zero-endpoint bridges, giving the stated conditional quadratic form. Wick's identity gives Var(Q)=1/45 and explained variance 2 tr((HΣ)^2), including the degenerate designs by the same interpolation with zero-length intervals. Writing r=(y−x)/2 and t=(x+y−1)/2, the centered polynomial has its unique maximum at r=(√41−1)/40 by the derivative sign. For r≤1/4 the polynomial is convex in t²; the extreme off-center candidate has only one effective site and strictly less explained variance. For 1/4≤r<1/2, the derivative in r increases with t² and its upper bound at t²=(1/2−r)² is strictly negative by the reported factorization. Decreasing r to 1/4 at fixed t is feasible and the maximum on that cross-section is strictly below the centered optimum. The pinned endpoint pair supplies no information. Thus the uniqueness claim and the three reported risks are correct.

## originality

FAIL

A distinct indexed result, 71ce7bada853, proves a stronger theorem for exactly this experiment with independent delivery of each exact reading with success probability p in (0,1]. It explicitly includes p=1, where the optimization problem, unique ordered pair and risk reduce to the frozen ones without additional assumptions. Its exact all-design risk gives the optimum and benchmarks by substitution. This establishes direct mathematical coverage even though the same-day catalog records do not establish historical order and the earlier deterministic antecedent mentioned by the stronger record is unnamed.

## value

FAIL

The nonlinear sensing question is well motivated and the global comparison rules out a tempting but inferior trisection mesh. As a separate frozen contribution, however, the exact optimizer and risks add no independent design insight or unknown invariant beyond the reliability theorem: they are its explicitly included endpoint and direct evaluations of its risk formula. An alternate polynomial proof here does not supply a new reusable lemma or an additional experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
