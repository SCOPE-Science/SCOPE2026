---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Unary rank-r types consist of first r vertices, last r vertices and an interior class once n>=2r+2; the two-variable quantifier recurrence checks equality, predecessor, successor and nonadjacent occurrence. Closed q-sentences depend on realized rank-(q-1) unary types. The explicit Theta_{a,b} with a+b=t-5 yields each t from 3 to 2q-1 at depth <=q; rank-two formulas isolate t=1,2. Fresh rank-refinement computations over lengths 1..22 and ranks 1..6 reproduced exactly 1 and 2q classes. This is not a proof by finite enumeration; the induction provides all n.

## originality

FAIL

Weis and Immerman 2009 Theorem 21 already characterizes rank-q FO2[<,Suc] equivalence on all words by successor-ranker occurrence and successor-order patterns. On one-letter words these stabilize beyond 2q endpoint positions; forgetting < gives the exact claimed long-path FO2[S] collapse, and the remaining small-length separations follow by elementary successor-only formulas. Thus the assessed theorem is a routine corollary/specialization of a stronger published structural result. Distinct wording or failure to print 2q as a headline is not originality.

## value

PASS

The sharp 2q resource cutoff for a natural canonical structure family is a useful exact model-theoretic invariant and the proof is instructive, notwithstanding its coverage by a stronger existing theorem. Value cannot compensate for originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
