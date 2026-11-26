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

At fixed census, D₁=N/P^(1/N) and D₂=N²/C where P=∏aᵃ and C=∑a², so strict discordance is exactly the opposite strict sign test on the two integer keys. For excess t≤7 every partition fits seven slots; comparing partitions with aligned lengths is equivalent to looking at that fixed seven-slot list and restricting to partitions of length ≤k. Explicitly zero-pad both excess vectors to equal length before adding ones, or equivalently use C−k=∑((e+1)²−1) over the positive parts. Common further singleton padding leaves differences unchanged. Convexity orders the two keys in the same direction on comparable partitions. An independent enumeration by sorted seven-tuples checked all pairs directly, including all six incomparable pairs in the stated table. The only reversed pair is excess (3,4) versus (1,1,5), admissible for each k≥3. Its first profile A has C=k+39 and P=800000, the other has C=k+41 and P=746496; both signs are strict and give the stated Hill rankings.

## originality

PASS

The supported distinct contribution is the fixed-richness, equal-census sharp integer threshold and its unique first pair, not that Shannon and Simpson can disagree or that majorization orders both. An inspected earlier primary example has equal census and reverses, but changes richness; the nearest indexed exact-cutoff statements change the indices or add a third-index constraint.

## value

PASS

Fixed richness and census remove two ordinary sources of changing rankings, making the first possible discordance of two common indices a natural discrete boundary. The uniform first obstruction and unique irreducible three-species pattern say more than finding an example or running a small-k survey; they clarify when a strict descriptive conflict can first occur and when ties must not be counted as reversals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
