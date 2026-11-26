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

An unselected edge is uncovered exactly when both endpoints are unused; a selected edge is uncovered exactly when it is an isolated selected component. Each legal move therefore lowers the potential by one or two. The first destruction of an isolated selected edge necessarily joins to an unused endpoint or to another isolated edge, costing two. Any completed sequence has u in {0,1} and length n-u-b. In even order with u=0, a last two-unused move at unused count two is illegal, so there must be a positive even number of one-unused moves. The last such move must touch an isolated selected edge, and there is already a two-unit reduction no later than the first such move, from the initial matching phase. This proves the sharper bound and both directions of the equality test. The matching-first construction leaves one or two unused vertices after its matching phase and is legal at every connector, including n=3 and n=4. As a bounded independent replay, memoizing on the uncovered-neighborhood mask rather than the selected-edge set reproduced the six length/count pairs for n=3–8, over 5, 5, 37, 67, 429 and 1325 mask states. A previously selected vertex cannot be used again since its neighborhood is already covered. This supports, but does not replace, the proof in RESULT.md lines 21–45.

## originality

FAIL

A distinct indexed record has the identical all-order parity law and an equivalent proof identity giving the same two-case extremality test. It additionally classifies and counts all odd-order maximum sequences. This is verified existing catalogue coverage, not an assertion that the companion record preceded the assigned one or that either is the historical first proof.

## value

FAIL

The open-neighborhood extremal problem on line graphs of complete graphs is natural and the potential makes its proof succinct. But the frozen claim adds no distinct exact invariant or independently useful classification to the verified same-family result: the potential equality test is the companion length identity expressed as a two-unit count. The frozen finite counts are verification data, not a separate novel census theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
