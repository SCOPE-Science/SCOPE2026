---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The morphism has constant first letter 0 and complementary second letter. Thus in φ(W)0 a factor meeting at least one second position is specified by a source factor and two zero flags. Every occurrence of the source factor lifts with the same flags, including across the right boundary using the appended zero. For the remaining singleton zero, a mark on a source 1 supplies an even-position zero. This proves forward lifting and T_{k+1}=φ(T_k)0. In the converse a two-mark set must hit both singleton letters. Its 1 must be at an even one-based position. For k≥5, the 24 short factors of T5 impose the exact obstruction to an odd-position zero mark. A complete radius-four window lies in at most two adjacent level-four blocks, aligned modulo two; the only source pairs are 00,01,10. Include the first four truncated contexts; at the right end a finite context only loses occurrences relative to the infinite one. Independent replay (python3 /workspace/independent_checks.py 5) checked all 8×5 possible mask combinations and found no cover, and enumerated precisely the six base pairs at k=4. For projection, the possible three-letter factors at odd starts are 000 and 010, and at even starts 001,100,101. Hence every occurrence of φ(Y), for |Y|≥2, aligns to a block start, and its even length precludes inclusion of the appended last zero. Even marks halve to a covering pair, including singletons by complementation of the second letters. This proves the unbounded classification by induction, not by testing a finite sequence of lengths. The full-dyadic multiplicity two is established by Banbara et al. Theorem 30.

## originality

FAIL

The frozen finding's exact six-pair relation is mechanically covered by a published stronger all-prefix result. In Banbara et al., Appendix A gives the actual exact three-track automaton pdfa2, not only a minimum-size bound or an existence theorem for some unspecified algorithm. The pre-dyadic restriction is ordinary regular intersection on its length track. In their zero-based coordinates, for k=4+m and base pair a,b, the k-digit tracks for (n,i,j) are the length-four stems for (15,a−1,b−1) followed by m copies of the column (1,1,1). The complete assertion is equality of a restriction of the published regular language to a six-stem regular language. Indeed one can extract the stems directly by classifying the 120 ordered increasing pairs of four-bit index stems under continuation by (1,1,1), and test for any accepted nonconstant-column tail by regular-language difference and emptiness. These operations use only the supplied exact automaton and require no fresh word-combinatorics lemma. No claim is made that these automaton operations were rerun or that the printed paper explicitly states the formula. The morphic lifting/projection is a different proof, but the frozen Finding is the covered pair classification plus a comparison to the known full-dyadic classification.

## value

FAIL

This is a natural boundary and the six-to-two contrast is readable. However, as a narrow invariant of this exact family, it is already mechanically determined by the published all-prefix pair relation and the known full-dyadic result. The submitted Finding does not establish a distinct useful invariant beyond that specialization. The structural proof may be instructive; it does not change the status of the invariant under review.

The dated certificate retains the supplied scientific assessment, sources and limitations.
