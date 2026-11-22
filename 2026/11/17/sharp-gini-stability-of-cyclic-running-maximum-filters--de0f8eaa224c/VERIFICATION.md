---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

A cyclic width-w maximum is continuous piecewise affine in input, with strict-order slopes given by site selectors. For selector counts c_j, exact Gini coarea makes the norm the maximum t(n-t)/[k(n-k)] on cuts S, with t=sum_{j in S} c_j. For 2w<=n, each c_j<=w, and the cases kw<=n/2 and kw>n/2 yield the stated upper w(n-w)/(n-1) by the occupancy and quadratic bounds. For 2w>=n the unique global peak wins all w windows containing it, forcing any output cut count t either <=n-w or >=w. This gives numerator at most w(n-w), denominator at least n-1. A small perturbation of one unique global maximum changes exactly w output coordinates, giving sharp equality. The n=2/w=n degenerate cases were checked. Fresh exhaustive strict-order selection and all-cut rational tests for all n=2..6, all 1<=w<=n matched the formula. Finite cases are corroboration only.

## originality

PASS

PASS (bounded best-of-knowledge). Flat dilation, sliding/rolling/running maximum and cyclic neighborhood supremum are equivalent operator aliases; the searched sources develop filter structure but not this exact all-pair Gini modulus. The proof requires a selection-count/cut argument and a long-window restriction; neither is an immediate corollary of order-statistic morphology identities. Material full texts and relevant primary sections checked; remaining historical-equivalence risks retained.

## value

PASS

The maximum filter is fundamental in discrete mathematical morphology; its exact two-input behavior can differ radically from one-input order properties and adjacent-edge variation. The sharp n/4 Gini amplification, exact window nonexpansivity set and single-peak extremizer form a useful structural stability theorem with a clearly motivated filter and seminorm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
