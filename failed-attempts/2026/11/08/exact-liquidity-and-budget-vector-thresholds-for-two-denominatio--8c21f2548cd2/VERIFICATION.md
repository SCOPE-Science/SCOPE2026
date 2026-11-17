---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Identical valuations plus zero-sum transfers force equal effective utility W/n and therefore cap bin load by floor(W/n+b_i)=q+b_i. With item sizes h and 1, greedy large-item placement then unit placement proves necessary and sufficient capacity inequalities. Aggregate minimum budget follows an extra h-good slot costing h-s and Δ<n; one-unit budgets cross a slot boundary exactly when s=h-1. Independently enumerated 7020 small indivisible allocations against criteria. All correctness statements follow the general construction, but the entire capacity region was published before the target.

## originality

FAIL

An earlier November 2 all-budget-vector theorem for the IDENTICAL additive-valuation model with item sizes 1 and h and budget-balanced individually capped payments already establishes precisely the two necessary-and-sufficient capacity inequalities and greedy construction for arbitrary real heterogeneous budgets. The submitted integer-budget q/r form is a direct specialization, while minimum aggregate budget and Bernoulli-one-unit feasibility follow by elementary floor thresholds and binomial counting, with no independently motivated new hard gap.

## value

FAIL

Individual cap feasibility and construction are an exact previously published stronger general theorem. The new total-budget optimization costs h-s per additional slot and unit-budget Bernoulli tails are mechanical consequences of that same region. Correct reformatting of known complete capacity criterion is not independently valuable novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
