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

Each perfect packing picks one vertex per rung, forcing one of two alternating row sequences. For a prescribed sequence the greedy output is that set exactly when every outside priority exceeds the minimum of its neighboring target priorities: otherwise an outside vertex in violation cannot be blocked by a previously accepted target; conversely the first accepted outside vertex is impossible under the condition. Integrating gives two endpoint factors g and L-2 interior factors k, including L=2 where the integral uses g twice on the same pair. T is bounded by Cauchy–Schwarz, and T squared is Hilbert–Schmidt with a strictly positive a.e. kernel. The positive simple Perron eigenvalue and gap for T squared pass to T: T preserves the leading projection, acts positively on its range, and on the complement its spectral radius squares to the smaller one. The positive pairing with g yields the nonzero leading coefficient and spectral-radius control gives the exponential remainder. Association gives the stated product lower bound, and disjoint consecutive triples give the upper bound. A maximal packing cannot have an empty end rung. Every internal empty rung is isolated and flanked by occupied rungs in opposite rows; successive occupied rungs, with or without an intervening empty rung, therefore alternate. Compositions of L-1 into steps one and two, times two initial rows, give 2F_L jammed packings. Binet's formula gives the ratio and strict enrichment. CHECK.py was inspected, not executed; the midpoint value is not used as a proof or certified numerical enclosure.

## originality

FAIL

Chern–Hwang–Tsai give an exact generating function in the identical open ladder model. Its top-degree specialization has a simple isolated pole at the positive root of 1-u+exp(-u), yielding the same pure exponential asymptotic with exponential remainder and an explicit rate and leading constant. Their paper need not state this endpoint as a separate theorem for it to be covered by this direct extraction. The Fibonacci denominator is already known. The transfer integral is an alternate representation and the positive-operator argument is a separate proof route, but neither supplies a further endpoint result not covered by the prior formula.

## value

FAIL

The kinetic-versus-uniform endpoint contrast is worth understanding, but the earlier exact equations already yield it and even provide the rate in scalar form. What remains is an alternate integral for a prescribed greedy outcome and the usual transfer construction for overlapping triples, followed by a standard positive-kernel argument. The frozen scope does not exploit this representation for an additional invariant, new bound beyond the exact rate, or a second model. No independently useful distinct claim survives narrowing the endpoint theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
