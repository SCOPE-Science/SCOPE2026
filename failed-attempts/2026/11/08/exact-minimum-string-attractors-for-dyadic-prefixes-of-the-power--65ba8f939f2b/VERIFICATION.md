---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Write t_j=2^j-1. Every occurrence of a factor with two ones contains a whole consecutive-one pair, and each pair has a selected endpoint. Factors with one one fit at the penultimate one unless their left overhang exceeds 2^(k-2)-1; then they must end at the last one and hit its preceding zero. All-zero factors fit in the last gap. For the lower bound, the distinct gap sizes give unique occurrences for the even-index pair witnesses ending at most at exclusive endpoint 2^(k-1) (even k) or 2^(k-2) (odd k). For odd k the additional near-penultimate witness has interval [3*2^(k-3)-1,2^(k-1)+1); the final witness starts at 3*2^(k-2)-1. The intervals are disjoint, with equality of adjacent boundaries allowed at k=2,3. Independently enumerated all byte substrings, marking those spanning the first selected point at or to the right of their start, and located each obstruction with two literal find calls to establish uniqueness. For k=2..9 the distinct-factor totals were 8,27,93,337,1273,4937,19433,77097; the hit sets were exactly the full sets and the sorted obstruction intervals were disjoint with cardinality 2,3,3,4,4,5,5,6. Replay: python replay/2_attractor.py. This bounds the replay, not the proof. The frozen checker was inspected, not run.

## originality

FAIL

The central exact minimum for the same word and all the same dyadic lengths was already expressly reported in the October 25 Resultary record, along with explicit optimal positions and disjoint unique-factor lower witnesses. A second, November 2 record reports a strictly broader all-length formula that entails the same equality. This is positive prior-coverage evidence, not a negative literature-search conclusion. The index establishes the overlap at the level of the mathematical results it reports; I do not assert identity of the uninspected witness sets or proof text.

## value

FAIL

The offline prefix invariant is worthwhile, but recovering the already published dyadic exact result within an already solved all-prefix profile does not fill the claimed gap. No genuinely new classification of optimal placements or new obstruction theorem is established; no valuable repair is justified by the frozen evidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
