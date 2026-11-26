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

An independent exact program checked both strongly regular graphs and exhaustively calculated dominance faces from the union of closed neighborhoods of the proposed dominating set. On the ordinary nonempty face poset, it reproduced the matching by disjoint addition pairs at each vertex and tested every directed incidence by iterative depth-first search. It found 59,819 and 59,747 faces including empty, 29,903 and 29,871 ordinary pairs, 461,552 and 460,656 ordinary incidences, no back edges, and critical-cell vectors {0:1,9:11} and {0:1,9:1,11:2}. The difference from the frozen incidence counts is precisely the 16 edges incident to the empty face. The discrete Morse theorem gives the Shrikhande wedge since the 9-cells attach to a point, and gives free rook integral homology in the indicated degrees since no positive critical dimensions are consecutive. For an invariant face with j vertex orbits, orientation times reduced Euler sign is (-1)^(j-1). Only odd degree 9 contributes to the reduced homological trace. Independent signed inclusion-exclusion on orbit projections of the 16 forbidden neighborhoods reproduced every trace (including the identity) and exact finite Fourier inversion reproduced every stated multiplicity. Equivalently, the trace is four times the sum of the indicators of the three cyclic lines, minus one; this gives one copy of each line-annihilator character and subtracts one trivial character.

## originality

FAIL

No distinct component remains against the verified indexed coverage at review. A separate same-date rook theorem gives the stronger homotopy type for every rectangular rook graph, including the frozen homology. A subsequent indexed theorem supplies both frozen topological claims and the full Shrikhande automorphism character. Its exact array, restricted to the sixteen translations according to the supplied affine enumeration, agrees entry by entry; the Fourier list is then forced. This is an assessment of demonstrable overlap as of review, not an assertion that the later records predate this frozen item or that either of the two same-date items took priority.

## value

FAIL

The topology of this canonical strongly regular pair and its symmetry action are well-motivated, useful exact invariants. But at review the rook calculation is a weaker instance of a family theorem, and the remaining wedge and translation data reproduce exact existing topology and an already determined character. The smaller matching and compact line formula are useful reproduction and presentation, not a distinct exact invariant or a new theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
