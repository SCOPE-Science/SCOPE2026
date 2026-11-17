---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

An orientation of the query graph F containing an undirected cycle can realize a directed cycle, so shattering requires a forest. When two comparable poset elements lie in the same query tree, orient the unique path opposite their fixed precedence; shattering fails, so each component must be an antichain. A directed cycle of fixed poset relations among query components can be connected by suitable within-tree path orientations to obstruct at least one label pattern. Conversely, if the quotient DAG is acyclic, any orientation of forest F remains acyclic with all fixed poset relations: a hypothetical directed cycle entirely inside a component contradicts forest/antichain, and a cycle across components projects to a quotient directed closed walk. Topological sorting yields every answer pattern. Longest chains force >=height(P) forest components, giving VCdim<=n-height; antichain rank levels each with spanning tree attain equality. Empty/total/antichain cases obey the stated conventions. An independently written full n=4 oracle tested 219 distinct labeled posets times 64 supports = 14,016 cases, comparing all linear-extension traces to the quotient criterion, with zero mismatches. Infinite validity follows from the graph proof, not finite enumeration.

## originality

PASS

The no-precedence antichain case recovers the classical all-permutation forest criterion; Mirsky rank levels are classical. Those are acknowledged. Semantic searches of linear extensions, static pairwise comparisons, VC shattering and height found no earlier all-fixed-poset forest+antichain+acyclic-quotient classification. Duan–Ouyang–Wang 2024/26 study VC dimensions of compatibility sets whose instances are entire posets/total orders, not individual pairwise precedence queries within linear extensions of a fixed poset. Dittmer–Pak address counting rather than trace shattering; related SCOPE records concern different adaptive/constrained hypotheses. The new quotient-cycle obstruction is not implied merely by the known antichain forest case; best-of-knowledge PASS with terminological search risk.

## value

PASS

The complete support classification is an intrinsic structural theorem for inference of rankings constrained by prerequisites. It identifies a genuine global quotient-cycle obstruction and yields the exact simple VC dimension n-height(P) despite #P-hard enumeration of the underlying linear extensions. This is natural in learning/order theory and more than a textbook chain-decomposition count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
