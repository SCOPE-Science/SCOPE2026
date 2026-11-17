---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For K_{a,b} with a,b≥2, W has w=b*C(a,2)+a*C(b,2) central generators and Vdim=a+b. Since E⊕W is abelian, rankKirillov≤2(a+b). A specific K2,3 mixed matrix has an integer unimodular (a+b)-minor; extending by vertices via one new two-path and a formerly unused edge column preserves determinant ±1, giving full row rank over every field for all nonexceptional bipartitions. For K2,2 the symbolic 4×4 mixed-block determinant is identically zero, giving rank≤6, and a rank-three D witness gives rank six. Hence index w+ab−a−b except K2,2 index w+2=6. Independently recomputed the special determinant in sympy and its rank-three witness; read the independent graph-bracket checker source and its unimodular minor construction. The all-fields assertion is supported by integer minors, not finite experiments.

## originality

PASS

PASS for the two-parameter K_{a,b} family excluding (2,2), including its uniform unimodular minor and arbitrary-field index. The exceptional K2,2=C4 value six is ALREADY COVERED by the same-date published cycle-index theorem; no originality credit for that boundary. No accessible general three-step all-graph index theorem was identified. Priority subject to inaccessible defining full text.

## value

PASS

The nonexceptional complete-bipartite class supplies a natural two-parameter exact Kirillov index over every field, distinguishing a rank-saturated family from the singular four-cycle. A unimodular witness explains why finite-field size introduces no further exceptions; this is usable structural information for graph Lie algebras beyond routine dimension counting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
