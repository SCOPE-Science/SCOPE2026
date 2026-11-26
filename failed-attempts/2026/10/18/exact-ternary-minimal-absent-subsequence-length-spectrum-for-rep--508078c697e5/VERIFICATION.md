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

In the infinite period 012, greedy matching must advance to the next block exactly at each weak descent, so a nonempty word is absent precisely when H≥k. Deleting an endpoint drops H by its adjacent indicator; for a triple the drop is 0 or 1 by transitivity (two descents give 1, two increases give 0, mixed gives 1 iff a<c). Thus minimal absence is exactly H=k with every deletion dropping H by one, and proper subsequences are then present by transitivity. This yields exactly the starting/ending weak descents and triple tests, and an adjacency on ordered pairs, weighting each new edge by t and each weak descent by s, including the initial st². In fact at most k−1 strict ascents are possible, since both endpoints are descents and two ascents cannot be consecutive; hence the stronger length bound 2k (the weaker frozen bound suffices for t=1). Independently computed the characteristic polynomial, identified its reversal with D, and checked the full numerator by the first nine coefficients and Cayley–Hamilton; verified all eight totals, plus complete direct histograms for k=1..6 by listing the present subsequences and testing all one-letter extensions of present prefixes (no assumed length cutoff). Replay: /workspace/branches/independent_replays/replay4.py and replay4.out. The shortest absent words are exactly the weakly decreasing words of length k+1; their multiset count is binom(k+3,2). From state 00 each of 1100 and 2100 is a valid four-symbol return, with three new descents, and 0 is an available one-descent loop. The initial 00, independent return choices and final zeros prove the bound at every k, including k≤3. The finite histograms corroborate rather than replace the formal identities.

## originality

FAIL

The main finding is wholly covered in the inspected current catalogue: two separate records give the identical complete ternary rational spectrum and local classification, one via a broader arbitrary-alphabet ordered-block transfer formula. Their displayed directory dates are later than this frozen record, so this is a finding of equivalent existing coverage, not that those records had historical priority or that independent earlier discovery is disproved. The explicit elementary lower bound does not supply a substantively distinct counting result once the same language and spectrum are known.

## value

FAIL

An exact ternary MAS spectrum is a useful invariant of a motivated family, but duplicate current coverage includes the exact spectrum and the structural rules behind it. The shortest layer is known, and the weak exponential estimate is an elementary consequence of those rules rather than a distinct extremal estimate or new phase of the spectrum. Reproduction adds confidence but does not provide an independently useful unknown exact fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
