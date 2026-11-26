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

PASS

In the two-move game, after matching points of the same mask, the second move can be matched by equality, below, above or incomparability as appropriate. Conversely, each mask's realization is expressible at rank two. For orders of size at least two, an isolated point makes all other points have an incomparable point, yielding exactly three possible mask sets by whether any comparable or interior points occur. Without isolates, exactly one maximal mask and one minimal mask occur: a unique extremum is comparable to every point, and otherwise the same-side extrema witness incomparability. Then the two interior masks are independently optional as an upper bound, giving at most 16 further spectra. Including the singleton bounds the nonempty family by 20. An independent enumeration of all 33,867 forward seeds through six points, taking transitive closure, matched all 20 codes and their minimum sizes, with first appearances (1,2,4,7,5,1). A linear extension ensures exhaustiveness through six, while the structural bound ensures there is no additional spectrum at larger orders. Code 232 requires two minima, two maxima and two distinct interior points, proving the lower bound six directly. The empty structure, if allowed, is detected by the negation of the rank-one nonemptiness sentence.

## originality

FAIL

An earlier indexed record states the same classification, sharp universal representative size and all 20 least sizes for precisely the same vocabulary and class of orders. Its change of bit convention is a bijective re-encoding, not a different invariant.

## value

FAIL

The complete rank-two census and six-point extremum would be useful for this natural family if distinct, but the earlier indexed table already gives the exact information. Recomputing it and adding the empty-order observation do not provide a new substantive result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
