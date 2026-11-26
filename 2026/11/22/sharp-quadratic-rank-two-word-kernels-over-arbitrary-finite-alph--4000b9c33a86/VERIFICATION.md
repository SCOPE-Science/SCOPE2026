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

After a first choice of position in a two-round EF game, the second move can be matched exactly when the first positions have equal letters and the available letters on both strict sides agree; an equality move is matched by the first position itself. A missing triple is also distinguished by a rank-two existential sentence with all the required presence and absence tests. This handles the empty word. Retaining one position per triple necessarily keeps each letter's first and last occurrence, so the strict supports of every retained position are unchanged, regardless of the representatives chosen. At least one position per signature element is necessary. For k used letters, the at most 2k first/last positions contribute at most 2k profiles. In each intervening gap an unmarked profile is specified by an active letter. Splitting singleton events into adjacent opening and closing events cannot reduce this bound. For opening and closing indices o_a,c_a the active-gap total is sum_a(c_a-o_a), maximized at k^2 when the closing indices are the k largest. This avoids the source's ambiguous 'distances ... minus k' wording: subtract k only if using endpoint-inclusive spans. In the given all-openings-then-all-closings construction, any event between two gaps changes a support permanently, so gap insertions of the same letter have different profiles; event positions are distinguished by own-letter absence on one side. This attains k(k+2), including k=1, and applies to the used alphabet when it is smaller than the named alphabet.

## originality

PASS

The pointed-type characterization is standard in method and is already explicit for binary words in the prior corpus. The supported distinct contribution is the exact word-by-word optimal thinning rule together with the sharp worst-case representative length for variable alphabet size, not an independent novelty claim for bounded-rank typing or the binary theory count.

## value

PASS

This gives an exact compression rule for each individual class in a natural bounded-depth logical equivalence, preserving the original order with arbitrary profile-witness choices. The worst-case storage cost as the alphabet grows is sharply quadratic, with witnesses for every alphabet size and an explanation in terms of first/last events. This is a useful structural boundary beyond merely counting binary theories or restating a generic small-model bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
