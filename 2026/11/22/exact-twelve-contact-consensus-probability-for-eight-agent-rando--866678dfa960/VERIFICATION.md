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

All coefficient rows stay dyadic and sum to one; general position and mean conservation identify opinion consensus with every row equal to the uniform row. The sum of Shannon entropies must increase from 0 to 24, while mixing two rows gives at most 2 bits by conditioning on a fair input-source bit. Equality identifies the source from the sampled label, i.e. disjoint supports. Starting at the terminal uniform rows and reversing, disjointness forces each contributing parent to be uniform on exactly half of the merged support. Thus at length 12 every agent participates once at each of the three support-doubling stages. Conversely twelve valid equal-cardinality disjoint unions reach entropy 24 and hence consensus; no shorter word qualifies. I independently reproduced the count using triples of perfect matchings and exact linear-extension counts, not the frozen forward state recurrence. For a fixed first matching, 384 viable triples each admit 49,920 words and 96 each admit 51,200. There are 105 choices of the first matching by relabeling. Thus 105*(384*49920+96*51200)=2528870400, and exact reduction after division by 28^12 gives 225/20661046784. The same method gives 24 of 1296 four-agent words.

## originality

PASS

The count of ordered twelve-contact words, and hence the eight-agent minimum-time probability, is distinct on the evidence examined. Minimum length and a staged matching reduction are not credited as distinct; a same-day structural result materially overlaps those parts but does not count the orderings.

## value

PASS

The exact minimum-horizon probability was an explicit question for the same stochastic model, and eight agents are its first untreated size. The exact word-sensitive count is a meaningful benchmark for fastest possible uncoordinated averaging, not merely the minimum contact bound or a topology table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
