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

The number of differing vertices is a lower bound; a swapped leaf cannot clear y and end at x with one leaf move and one center move. Without a swap, clear all y leaves directly before the center move, or change only leaves if the centers agree. With one swap a third color is a legal temporary leaf color. For w≥2 and m initial y leaves, at least m−1 of the k−2 noncenter colors are absent initially, while at most m−w can be targets of those leaves. An intermediate center color exists even at k=n+1; clear y by moving its leaves directly, switch the center to y, then finish any leaves targeting the intermediate color. Independent leaf choices give F, G and H; the shift by one or two depends on the presence of a swap. Every source attains h=n with a swap by using an initial leaf color as target center and setting all target leaves to the initial center color. This gives radius, diameter and the leading coefficient (divide by two for unordered pairs). At k=n, in the witness with all leaves initially y, one center move forces both swapped leaves to move twice; two center moves force the initially y leaf targeting the intermediate center color to move twice; three center moves already suffice for the n+3 lower bound. Using temporary x on the blocked leaf attains n+3. At n=k=2 the two states are disconnected. Independent all-source BFS covered n,k=(2,3),(3,4),(3,5), covering 144, 11664 and 102400 ordered pairs, and found distance 6 for the n=k=3 witness. The (3,4) counts were (108,744,2160,3600,3528,1524); the check is finite and the proof is not. Replay: /workspace/branches/30b76375-a2fd-4e7f-a7e7-68a1eec9e8a8/star_replay.py and star_replay.out. The frozen checker was inspected, not executed.

## originality

PASS

At the repaired scope, k=n+1, neither the exact list-tree metric nor the cited diameter results have the necessary center list size. The one-color improvement is mathematically substantive and sharp, rather than re-expressing the prior formula on its own domain.

## value

PASS

At the sharp threshold, every metric shell and extremal-pair count in a canonical configuration graph is available without constructing its exponentially large state set. A distinct obstruction and a constructive spare-color argument explain why the reduction by one is feasible and optimal; the result is not a larger-palette parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
