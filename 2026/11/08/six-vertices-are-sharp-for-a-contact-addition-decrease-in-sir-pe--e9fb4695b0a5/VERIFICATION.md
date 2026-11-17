---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

From CTMC first-event conditioning in states (susceptible S, infectious I), with removals monotone, the success probability F(S,I) obeys a well-founded rational recurrence: terminal |I|≥k success and I=∅ failure; each infection/rate term and removal/rate term normalized by |I|+β∑d_I(v). The denominator is positive for I≠∅, recursive measure 2|S|+|I| strictly decreases. Independent graph-atlas census checked all connected graph isomorphism types n=2..5 (1,2,6,21), all missing edges, seeds, k, and the rational differences for all β>0: exactly 1,738 comparisons (1,475 with nonnegative numerator+denominator polynomial coefficients and positive sign; 263 identities). Exact independent six-vertex subset DP for β=50 proves R6(tree)-R6(+edge)=24352320312500/56704429847324259>0 with stated graph, seed1. Thus six vertices are sharp; no small-n numerical sampling is used to claim all β.

## originality

PASS

Primary exact Markovian SIR network equations and small-graph seed importance paper study expected node prevalence/final outbreak size, vaccination and detection, not hitting probability of realized max simultaneous |I_t| conditional on adding a contact. No published Resultary search record supplied the all-rate edge-addition monotonicity through five and sharp six-vertex SIR peak-overload counterexample under identical CTMC and single-seed conventions.

## value

PASS

A sharp failure of contact-addition monotonicity for *realized peak concurrent overload* is a structural counterexample with an exact first-order size cutoff under fixed natural homogeneous CTMC rules. Unlike routine average-final-size computations, the 1738 full-parameter rational classifications distinguish n≤5 from n=6, and the rational six-vertex witness gives a reproducible overload-risk design boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
