---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Encode each rule as a labeled edge, with terminal rules going to one sink. Words are bounded by complete path count. Removing the r edges out of the start leaves budget e=p-r and at most M(e) continuations per head, counting the sink's empty continuation as one. Matching parallel chains give the maximum integer product over positive parts summing to p. M(p) increases strictly for p>=2 by increasing a part of a maximizing composition of p-1. At equality all p rules lie on complete paths and the word labels are collision-free. The case e=0 gives a single terminal layer; e=1 is impossible for p>=2 since at most p-1 paths would result. For e>=2 each maximizing suffix head must use every remaining edge by strict monotonicity. Distinct heads would have to reach each other, using an outgoing edge of the other, contradicting acyclicity. Thus there is one head per layer, inductively. The p=1 case requires exactly one terminal production at the start. Merging ones, replacing a part b>=5 by 3 and b-3, and replacing three twos by two threes give strict improvements; splitting a four into two twos preserves equality and yields the listed maximizing compositions. Mixed-radix labels yield exactly each exponent 0 through M(p)-1 once even over a unary alphabet. For the cover, the necessary count bound and the interval produced at the least feasible p coincide, giving the stated inverse and bounded additive remainder.

## originality

PASS

Pass for the sharp production-count capacity, equality structure with injective word labels, and exact consecutive-unary cover threshold. The integer-product calculation is classical. The closest primary graph result gives different extremal path functionals, including the important one-sink count from all starts; neither that result nor the general cover results establishes the stated fixed-endpoint grammar theorem in the inspected material.

## value

PASS

The exact maximum and structural equality theorem address a natural resource question in the regular-cover model: how many distinct words a production budget can buy, and what must happen in an optimal description. The collision-free unary realization turns that maximum into an exact inverse for a natural test family, substantially sharpening the older cardinality bound rather than merely restating integer-break arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
