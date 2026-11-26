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

With two sequential PAL2 steps, a second start j≥i+4 commutes to the history (j−2,i), giving the canonical bound M_n. Local history collisions extend with fixed exterior context. The exact small spheres |D₂(000)|=1 and |D₂(0110)|=10 certify losses seven and four; any interior defect either lies in a constant triple or has the opposite bit on both sides. If only the two endpoints are defective, the three specified disjoint subsets of histories with sizes 3,2,3 force a loss of at least five, including at n=4. In parity coordinates an alternating source becomes constant; choose all ones. After one RC2 step the word is 1^a001^b, a≥2, a+b=n. The second 00 gives n−1 words, the mixed choices give (n−1)+(n−2) words, and 11 gives binomial(n,2) words with two zero pairs. The total is M_n. For an endpoint defect set N=n−1. The left first-step forms are 0101^N or 01^a001^b; the right forms are 1^N010 or 1^a001^b0, a≥2, a+b=N. The three mixed choices after the mixed first step coincide, and the mixed boundaries of the new zero pair and the original zero give the three four-zero templates on each side. On the right, the terminal 000 gives the extra three-zero word 1^N00011 from its last 00; among four-zero words only the first two families intersect, for b=1. For the five-zero templates, first insert after a+b ones and then after a to attain every spacing, including b=0 or 1. These run forms give the exact left and right spectra and equal totals M_n−3 for the four stated sources. Independent integer-bit insertion checked all words at n=4..12 and both RC spectra at n=4..60. Replay: python /workspace/branches/independent-checks/pal2.py.

## originality

PASS

The known maximum, all maximizers, commuting-history bound and even-length parity conjugacy are prior. The distinct claim is the exact strict runner-up and complete set of four binary endpoint-defect sources, plus the two different RC2 weight spectra. The closest inspected maximum-level and confusability-code results do not yield these conclusions.

## value

PASS

A maximum alone supplies no quantitative separation from nearly extremal sources. The sharp three-descendant penalty and exact four equality cases connect specific neighboring defects to the channel sphere size. The parity-coordinate output weights distinguish the two positions even though the totals agree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
