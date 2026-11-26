---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The rational branch images give the stated finite Markov graph. After identifying reflected states, the first return from state m+1 takes any length k=2,...,m+1 with multiplicity two: choose the initial target j=m+2-k, advance to m, then choose its reflected or unreflected successor. States I_0,J_0 contribute at most a spectral radius of one. Thus the growing component satisfies 2 sum(lambda^(-k), k=2,...,m+1)=1. Closed endpoints are retained; the nested cylinder map is onto and each point has at most two codes (once a side of an endpoint is chosen its next interval is forced). This finite-to-one coding preserves entropy. The inverse similarities satisfy the graph-directed open set condition on interval interiors, giving dimension log(lambda)/log(2). Adding a return term shows strict monotonicity. For delta=2-lambda the exact identity delta(3-delta)(2-delta)^m=2 first gives m delta=o(1), then delta=O(2^-m), and on substitution gives the asserted O(m 2^-m) relative error. The supplied rational checks are corroborative only; no uploaded code was run.

## originality

FAIL

The principal formula is a direct specialization of a prior entropy theorem for the identical open negative-doubling survivor system. The eventual tail contributes a geometric series, and its reduced numerator is exactly the claimed Perron equation. Strict monotonicity and the stated shrinking-hole estimate are elementary consequences of that same equation. Absence of a separately printed family formula does not remove prior implication.

## value

FAIL

The symmetric family and exact coefficient are natural, and the elementary Markov proof is useful exposition. But the exact invariant and the quantitative error are obtained by geometric summation in a known applicable formula and elementary manipulation of its numerator. The submitted statement supplies no separate new cutoff, mechanism, or nonmechanical exact result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
