---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Finite calculation and trace verification

The attached source `check_betweenness5.py` is Python 3 standard-library code. Execute it in the same directory as `facet_orbits.tsv` and `witness_4.tsv` using `python3 check_betweenness5.py`.

The script independently enumerates the complete permutation set both by recursive insertion and by direct generation; it independently evaluates betweenness by strict positional intervals and by contrasting pairwise comparisons. It compares the exact resulting concept-row sets. For three, four, and five labels it tests every candidate query subset at each potentially shattered size and checks the complete shattering polynomials. For five labels it exhaustively rules out all \(142506\) five-query supports, and monotonicity excludes every larger support. The result is a complete finite proof of the displayed face polynomial.

The script enumerates all facets and the natural \(S_5\) action on query coordinates, expands the twenty-five provided orbit representatives, checks their disjointness and exact coverage, and reconstructs the entire complex from their downward closures. It also verifies each of the sixteen explicit response/witness rows in `witness_4.tsv`.

Observed successful output: `BETWEENNESS5_PASS: 30 queries, 60 concepts, face counts 1,30,405,2700,510; facets 1530+510; 25 facet orbits; all 142506 five-query supports excluded`.

This computation proves only the stated small finite cases. It is not a proof of historical originality or a statement of independent mathematical auditing.
