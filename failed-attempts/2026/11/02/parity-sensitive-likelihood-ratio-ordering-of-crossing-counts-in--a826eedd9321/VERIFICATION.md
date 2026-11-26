---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A fixed matching on m residual vertices and a uniformly chosen a-subset have the same cut-count law as a random matching and a fixed cut. The coefficient of u^a z^k in (1+2uz+u²)^(m/2), divided by binom(m,a), gives the displayed factorial mass after expansion: each pair contributes zero, one, or two selected endpoints, with two choices in the crossing case. The a inside vertices each contribute crossing probability b/(m−1), so the increment in the mean is (m−2a−1)/(m−1)>0. In a uniform nested sequence of subsets, a cut with x crossings loses one crossing if the new vertex is one of x outside partners, and otherwise gains one. If t is the least positive integer of parity a, only X_a=t can change the tails at the two thresholds t and t+1; differences are −t p_a(t)/b and (b−t)p_a(t)/b, respectively. Both are nonzero for 1≤a<n−1. At a=0 the adjacent pair is instead deterministically ordered. The ratio of coefficients at cut sizes a+2 and a is (a+2)(a+1)/(b(b−1)) times (b−k)/(a+2−k); the latter increases on the common support since b>a+2. The new maximal mass makes the LR order strict even when the common support is a singleton. Transitivity orders each parity class. This analytic replay covers all sizes; the frozen checker was inspected, not executed.

## originality

FAIL

Distinct Resultary record 9a5798d3e263 states the same conditional law, mean monotonicity, positive-adjacency stochastic incomparability and within-parity strict likelihood-ratio ordering on the same cut domain. Record 48fe8ff3ae08 independently overlaps the exact same-parity ordering and formula but gives a narrower opposite-parity example. The conclusion is substantive duplicate coverage, not an inference from catalogue dates or from Acan's earlier moment formulas.

## value

FAIL

The distinction between increasing means, contrary adjacent tails, and increasing same-parity likelihood ratios is mathematically useful for the cut model. The frozen finding, however, repeats that exact distinction; after removing the existing statement and classical matching count there is no separate quantitative invariant or order comparison here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
