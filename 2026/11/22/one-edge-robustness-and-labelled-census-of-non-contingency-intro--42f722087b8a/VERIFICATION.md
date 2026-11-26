---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For nonadjacent a,b sharing w, any v in N(a) but not N(b) gives a countervaluation with p true only at b: Δp holds at a and v but fails at w. Therefore distance-two vertices have equal neighborhoods, ruling out geodesics of length at least three and making nonadjacency with equality an equivalence relation within components. Conversely, in a bipartite complete component the neighbors of a vertex all have the same successor set. With ≥3 parts, if p is constant on the neighbors of a vertex in A, each of those neighbors sees all of A and some vertices of that common exterior value; all neighbors therefore agree on Δp. Isolates satisfy the schema vacuously. In a complete multipartite component the only bridges occur in stars; deleting a nonbridge must make its endpoints equal-neighborhood nonneighbors, which requires two singleton parts. Inserting internally splits a two-element part, and inserting between components creates a bridge and hence must form a star. These give precisely the marked edit locations, with both endpoints counted for K₂. The component series x+B−e^x counts one isolate type and set partitions into at least two parts; marking a singleton pair or a center and leaf of a larger star gives D. For an independent insertion-side derivation, two marked isolates and a marked size-two part in a nontrivial component give x²/2+(x²/2)(B−1); attaching an isolate to a designated star center gives x[x²+x(e^x−1−x)]. The sum equals D, and each is multiplied by H for the rest of the components. A fresh exhaustive semantics/location check over orders 0–5 and a separate exact coefficient recurrence through the displayed ranges reproduced both sequences.

## originality

PASS

Credit general modal correspondence to Zolin, ordinary multipartite structure to the symmetric loopless specialization, and the unmarked EGF to the classical partition/exponential construction. The distinct result supported by the comparisons is the exact location and count of all individual safe edits in that class, including the marked labelled census. The decision does not rely on an originality claim for the unmarked coefficient sequence or the general modal axiom.

## value

PASS

Once a standard modal validity condition is interpreted as a graph property, knowing precisely where individual edits preserve it is a natural next question. The local distinction between splitting a bridge, merging parts, and attaching to a star gives a structural answer for every valid labelled graph. It also yields a two-sided marked census without exhaustive search, beyond the routine unmarked Bell enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
