---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For T the 12-vertex graph of ordered pairs (i,j), edges share first index or are opposite arcs. The complex Ind(T) is exactly the matching complex of once-subdivided K4. Independent enumeration gives face counts (12,48,72,30), 162 nonempty faces and 432 Hasse covers. Exhaustive independent 78-pair acyclic discrete Morse matching leaves one vertex and five 2-cells, giving integral wedge five 2-spheres. Enumerating all 24 S4 label permutations with oriented fixed simplices produces rational character (5,-1,1,2,1) on five cycle types; this equals 1+sgn(g)*#Fix(g), hence 1⊕sgn⊕(sgn⊗Std3). Averaging shows one invariant H2 quotient class and no other reduced rational homology.

## originality

FAIL

FAIL: earlier 2026-11-08 published Resultary theorem explicitly identifies the same ordered-arc graph as line graph sd(K4), states Ind(T)=M(sd(K4)), proves wedge five 2-spheres, and gives exact S4 character 1 ⊕ (sgn⊗Q4) with full-group quotient H2 rank one. Decomposing Q4 into trivial plus Std3 is a textbook equivalence, and the earlier result proves stronger all-subgroup quotient statements.

## value

FAIL

FAIL: natural exact invariant and full symmetry group would be valuable if unknown, but these values, group action and quotient were already explicitly published for the identical complex. Replacing the graph name, reorganizing representation summands, or repeating a finite Morse certificate does not add new mathematical content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
