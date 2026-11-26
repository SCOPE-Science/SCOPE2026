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

For n=1 the graph is K_m and a nonempty dominating set must leave at most k vertices out. For n≥2, the word rule gives at most one link per vertex, tied to the symbol preceding its maximal constant suffix, and exactly one link per adjacent pair of quotient prefixes. The omitted-set relation has k residues per row (the symmetric ± offsets, plus a common diagonal bit if k is odd) with no duplicate offsets because 2 floor(k/2)≤m−1. The last two symbols of linked words are either transposes or both diagonal, so no link crosses membership. Every row clique has m−k selected vertices; domination and the limitedness bound follow inside each row. For the lower bound a nonempty row requires at least m−k selections; an empty row forces every linked endpoint on the other side to be selected and gives each neighboring row at least m−k+1 selections. In a quotient clique of size m at most one row can be empty, and then (m−1)(m−k+1)=m(m−k)+(k−1). Summation proves equality for all stated parameters. I independently reconstructed word adjacencies and checked constructions on nine instances and all smaller subsets on six of them, including S(2,4) for every k; replay: python3 /workspace/checks/frozen_review_checks.py sierpinski. The proof, not these tests, establishes the universal claim.

## originality

FAIL

Resultary 023a3f7ea943 establishes the identical conjecture, on the same classical word graph, definition and complete parameter range. It gives both an explicit final-two-symbol circulant-type construction and the same charge for an empty row within each two-level block. Complementing the selected/omitted relation and expressing the block as a quotient clique do not identify a distinct theorem or materially different mechanism. The overlap is demonstrable without adjudicating publication timestamps or authorship; the comparator's indexed path is earlier, not proof of priority by itself.

## value

FAIL

Resolving the full conjecture is mathematically worthwhile, but the frozen submission offers no substantial increment over the inspected all-depth solution: it neither classifies minimizers nor extends the parameter range, and its quotient formulation recasts the same empty-row charge and regular-relation construction. A second presentation of those arguments is not a distinct scientific result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
