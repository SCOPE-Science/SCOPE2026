---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Definitions are consistent: arcs of fully bidirected simple graph, faces are directed vertex-disjoint simple paths including augmented empty face, no directed 2-cycles. Independently enumerated all 2^(n choose 2) labelled graphs at n<=5 up to permutation, 52 isomorphism types with counts (1,2,4,11,34). Rebuilt each multipath complex from direct arc-subset combinations and acyclicity tests, and independently computed exact integer Smith normal forms of every ordinary boundary with SymPy over ZZ. Across all 52 classes, the ONLY nonunit Smith factor is 2 for n=5 mask 127 (orbit size 10), at boundary degree two. Witness nonempty face numbers (14,54,60,12), boundary ranks (13,41,12) and factor 2 imply reduced H1=Z/2, H2=Z^7, nothing else. Checked direct chain condition d1 d2=d2 d3=0 on the witness. The source code additionally checks two distinct fully Hasse-acyclic Morse matchings with residual entries (2,2,2) and (2,-2); no hidden infinite extrapolation is needed for this finite theorem.

## originality

FAIL

The 2026-10-18 Resultary published theorem is an exact earlier theorem with identical graph-domain, arc-face definition, unique five-vertex exception, integral H1 and H2, and an even stronger homotopy classification. All content in the current 2026-11-08 final claim is a formal corollary or a restatement of that full theorem. Additional 2026-11-08 triangular-book homotopy results independently cover the witness homology. This is decisive positive coverage, not novelty inferred from failed search, and cannot be repaired by disclaimers or an extra certificate.

## value

FAIL

The five-vertex first-torsion boundary and the B3 integer homology are mathematically natural and interesting in isolation. But the assigned finding adds no distinct exact invariant, object characterization, boundary, independent structural lemma or stronger scope beyond the full 2026-10-18 published five-vertex census plus RP2 wedge decomposition. The fresh certificate and implementation are useful as verification, not a new valuable scientific claim under the audit standard. A narrower disclaimer would only restate the known theorem and cannot make this final claim original or independently valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
