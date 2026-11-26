---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For consistent rows, each delivered projection multiplies the error by I−aaᵀ. Conditioning backwards across independent deliveries gives the nested expected-energy map H↦(1−p)H+pPHP, so the objective is the largest eigenvalue of a positive semidefinite matrix, with maximization after expectation. Reflection pairs up the six orders. The exact reconstruction confirms equal traces for central-last and central-first, with determinant difference 54p³(p−2)(p−1)(36p−100)/100000<0 for 0<p<1; this strictly excludes central-last there. A common eigenvalue of central-first and central-middle is forced by subtracting their characteristic equations, and substitution yields the stated quintic times (1−p)/250000. The transformed quintic has exactly one Descartes sign change; exact opposite signs at 7/8 and 9/10 establish existence and uniqueness. The forced eigenvalue is strictly above both half-traces throughout that bracket (the two excesses decrease there and are positive at 9/10), so the common root is on both upper branches. The comparison at 1/2 and the perfect-delivery factors 1/100 versus 8/125 orient the two intervals; at p=1 the common zero eigenvalue is irrelevant and central-last loses, and at p=0 all six are identity. The exact root isolation and decimal 0.8823801245146625… agree with the frozen result.

## originality

PASS

The exact row geometry and the general phenomenon of order effects both have nearby precedents. The supported distinct result is the complete minimax order classification across Bernoulli delivery probabilities for three fixed once-each attempts. The inspected same-geometry and finite-sweep claims do not imply this classification. No priority order was assigned to same-day entries, and full-text comparison to two older Kaczmarz papers remains limited.

## value

PASS

Equal-budget fixed sweeps are a natural comparison in a setting where attempted but missed updates still count. The exact example shows that the best deterministic order need not even remain minimax as reliability decreases, and separates central-last from central-first despite their equality at perfect delivery. The complete threshold, tie cases and exclusion result make a reproducible benchmark for the interaction of noncommuting projections and independent omissions, beyond the observation that order sometimes matters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
