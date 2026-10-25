---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Correct for the pure Fraisse-limit theory DMT of meet-trees in the order/meet language. For nonempty finite P, A=dcl(P) is exactly the finite meet closure, and A being term-definable from P gives the same 1-type space. The one-point generation lemma gives <A,b>=A union {b,c}, where c=max_{a in A}(a meet b), with at most one c outside A. By quantifier elimination, a complete 1-type is exactly its finite meet/order diagram over A. For m=|A|, algebraic types number m. For nonalgebraic b=c, its cut inserts b either below the minimum of A or in one of the m-1 cover edges, giving m types. For c in A and b>c, b uses one fresh cone over each possible old c, giving m types. For c not in A and b>c, c is in the same m gaps and b uses a fresh cone at c, giving m more types; c cannot lie above an old maximal vertex since then it would not be a meet with A. Density and infinite ramification realize every signature, homogeneity and QE make each signature a single type, so |S_1(P)|=m+3m=4m. An n-point generating set produces at most one extra maximal meet point when each next generator is adjoined, so n<=|dcl(P)|<=2n-1; an n-chain and n leaves of a finite full binary meet-tree attain the endpoints. Thus 4n<=|S_1(P)|<=8n-4 for n>=1, maximum 8n-4; S_1(empty)=1 by transitivity. Independent exact combinatorial enumeration, not a general proof, confirmed 3m nonalgebraic signatures for every finite meet-closed labeled base through m=4 and the closure inequality across 510293 subsets of rooted trees through six vertices.

## originality

FAIL

Decisive exact coverage by a distinct, already published SCOPE/Resultary record titled Exact finite-parameter 1-type growth in dense meet-trees (record 3c694ab1c174). Its complete RESULT.md states |S_1(A)|=4|dcl(A)|, the sharp bounds 4n to 8n-4 and the empty-set exception, in the same pure Fraisse-limit meet-tree theory, and proves them with the same algebraic/2m no-new-meet/m new-meet classification and the same sharp closure argument. The covered source commit bbe70f... has verified timestamp 2026-10-04T05:57:48Z; the assessed distinct source commit 7c8fb... has verified timestamp 2026-10-04T05:57:56Z, eight seconds later. Differences in names, notation, references, and bounded verification programs do not constitute an uncovered theorem. The source is published in Resultary with its own separate source record identity. This is positive coverage evidence, not a failed search or an access-based rejection.

## value

FAIL

Finite-parameter type growth is a natural local-complexity invariant, and an exact structural count can intrinsically be useful. But this submitted finding reproduces verbatim-equivalent exact formula, proof structure, sharp n-point extremum and empty-set case already present in the separately published Resultary/SCOPE record 3c694ab1c174. It offers no distinct theorem, motivated new boundary case, unexplored parameter regime or independently needed invariant; the separate finite verifier is redundancy, not a new contribution. The mathematical interest of the prior fact does not make a duplicate a worthwhile new research finding. This is a substantive duplication-based V failure, not a failure merely due to thin access or modest theorem size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
