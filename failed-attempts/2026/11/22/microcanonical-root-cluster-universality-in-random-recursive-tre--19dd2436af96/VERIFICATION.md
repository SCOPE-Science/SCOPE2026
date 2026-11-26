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

For any fixed retention schedule η_j, the cluster grows at stage j+1 with conditional probability η_j C_j/j. The rising factorial is multiplied in conditional expectation by 1+rη_j/j. Iterating from r! and averaging the uniform schedules of N−h retained positions gives (1), including h=0 (size n) and h=N (size 1). This independently checks the marked transform and its normalization. At n=3, direct averaging over the two recursive trees gives moments 7/4 and 5 at h=1 for orders 1 and 2. Equations (4)–(7) correctly use Bernoulli parameters (1−p_n)/(1+rp_n/j), variance Np_n(1−p_n)+O_r(log n), and a shift from h_n of order log n. The characteristic function bound controls all off-central frequencies, so both point probabilities have the same leading term; a weak CLT alone would not suffice. Uniform gamma ratios, lower-order moment estimates, uniform integrability from higher moments and Carleman's criterion give (2), only for fixed orders and interior limiting retention, with n raised to the actual p_n. The frozen checker was inspected, not run.

## originality

FAIL

Both stated results are mathematically covered by the exact canonical transform already published by Desmarais–Holmgren–Wagner, Prop. 4.1, also available as the root-cluster marginal of Resultary 3992334979d1. The finite conditional moments are literally the coefficients of this known canonical moment polynomial in its binomial basis. The moving-fraction limit then follows from the same known product and monotonicity, without the paper's tilted local-limit strategy. The failure is demonstrated prior implication, not a claim that the older papers explicitly state the same formula with deletion-count notation, and not a judgment that the frozen result is false.

## value

FAIL

The fixed-budget interpretation is natural and the closed form is convenient, but neither the exact invariant nor its claimed asymptotic consequence is distinct from the exact canonical transform under a direct change of basis and routine monotone concentration. The tilted Bernoulli argument is a valid alternative proof but the frozen claim gives no new local-limit regime, joint law, error rate or other independent result beyond the mechanically recovered conclusions. No distinct valuable remainder is established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
