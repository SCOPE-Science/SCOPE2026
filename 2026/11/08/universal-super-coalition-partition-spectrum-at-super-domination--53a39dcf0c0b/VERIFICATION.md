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

# Verification

Run `python3 verify.py` with a standard Python 3 interpreter and no network access or third-party packages. The program independently tests the super domination witness definition, generates the feasible-pair graph, computes disjoint edge pairs, exceptional perfect matchings, and triangles, then compares exact formulas with exhaustive enumeration of all unordered vertex set partitions.

Observed successful results from the standalone verifier:

```text
MULTIPARTITE_EXHAUSTIVE_OK 15
ALL_SIX_VERTEX_GRAPHS_OK 24509
SEEDED_OTHER_GRAPHS_OK 7 197
SEEDED_OTHER_GRAPHS_OK 8 108
SAME_SET_POLYNOMIAL_DIFFERENT_COALITION_SPECTRA_OK
VERIFY_OK
```

The complete six-vertex scan considers all labelled simple graphs with six vertices, filters graphs with isolated vertices and those with feasible omitted triples, and directly checks the complete partition-count formula on each of the \(24{,}509\) eligible labelled graphs. The 15 multipartite profiles include the exceptional six-vertex boundary. Larger checks use a fixed pseudorandom seed and test all partitions in each retained graph.

This checks many finite instances; the general unrestricted claim follows from the symbolic case analysis in `RESULT.md`, not from sample extrapolation. The verification is not independent mathematical validation, and no independent audit was performed. Literature originality assessment remains provisional because the motivating manuscript's full text was unavailable.
