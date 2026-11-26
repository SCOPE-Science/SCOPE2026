---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

FAIL

The character values and rational quotient conclusion independently check out, but the frozen Finding's conjugacy-class annotation is false for the full group A to which the table refers. The order-seven row is ONE class of 48 in A (two of 24 only in the collineation subgroup A0); the exchanging order-eight row consists of TWO classes of 42 in A. Direct conjugation of all 336 enumerated permutations certifies this. The two order-7 collineation types are also interchanged by inverse transpose, which swaps their reciprocal irreducible cubic polynomials. The column labels split/order do give an elementwise character, not a fine conjugacy classification as worded. Correct core: connectivity enumeration gives 98 connected four-sets and 903 disconnected ones, with a private triangle for each dual tetrahedron and every five-set having a disconnected four-subset. The private unit minor and full dual two-skeleton give only rank-188 reduced homology in dual degree 2; Alexander duality gives only degree 9 for the cut complex. Recompute all automorphisms through permutations of Fano points preserving the line collection and their compositions with polarity. For each, recompute signed Lefschetz sums on unions of vertex cycles both directly and in the dual, with the full vertex sign in duality; all 336 values match the table and both averages vanish. The rational quotient follows from barycentric subdivision and averaging. Independent replay: python -B /workspace/review_evidence/4_fano.py; output 4_fano.txt. The uploaded script was not executed. Even reading the ambiguous class sentence as meant only in A0 would leave the overall rejection unchanged.

## originality

FAIL

The equivariant theorem for ordinary high-girth cut complexes in the earlier distinct Resultary record 1919c3ab7881 covers this very case, with a stronger integral lattice result and an explicit rational trace formula. Exact table publication is not needed for implication. The 2024 Bayer et al. virtual-character formula is a second general source; it is not restricted to the neighboring families discussed in the frozen comparison.

## value

FAIL

The equivariant invariant is natural, but calculating this table is a finite specialization of an existing explicit general formula plus straightforward character averaging. Conjugacy labeling can be corrected as above, but that does not make the underlying scientific claim distinct or create a valuable new remainder. No repair submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
