---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The lower bound follows because undirected adjacency is quantifier-free definable by \(S(x,y)\lor S(y,x)\), so Brown--Hoshino's exact undirected separating sentences transfer without increasing rank. For the upper bound, their cycle proof cuts at the first chosen vertex and invokes an endpoint-preserving path strategy; inspection of the primary proof shows that its coordinate responses preserve signed displacement and corresponding left/right endpoint gaps, hence preserve successor orientation as well as undirected adjacency. The q=1 and q=2 cases are checked directly. A fresh independent exact EF-game solver agreed with the formula on 144 cycle pairs over \(1\le q\le4\), \(3\le m\le n\le10\); this is corroboration only.

## originality

FAIL

The exact numerical threshold is already Brown--Hoshino's cycle threshold, and the only extra step for the directed signature is to observe that the published coordinate/endpoint strategy preserves signed orientation. Pichler's later finite-model-theory notes explicitly state that the same cycle-composition method works for directed as well as undirected cycles, albeit with a coarser stated sufficient bound. Thus the final directed theorem is an implication-level transfer of prior machinery rather than a surviving new theorem under the audit rule.

## value

PASS

The exact quantifier-rank profile of the canonical directed cycle family is a natural finite-model-theoretic invariant and would be useful as a benchmark. The record is rejected because that invariant is already mechanically supplied by prior methods, not because the question is unmotivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
