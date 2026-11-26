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

A subset that becomes a singleton stays a singleton, so collapsing all singleton states to one absorbing reset state preserves shortest reset lengths in each factor and in the triple. Independently of the frozen signature quotient, I partitioned all 729 tables into 129 orbits under simultaneous state relabeling of both letters, found 94 synchronizing orbits of total mass 549 by subset reachability, and ran full product BFS over every multiset of three such orbit representatives. Weighting by the product of orbit sizes and 3! divided by the factorials of the orbit-index repetitions restores all ordered labeled triples. The exact length counts for 1–7 were 1062153, 48991068, 66420432, 35524872, 10653120, 2651616, and 165888, totaling 165469149. A separate word scan confirmed the 28 signatures and the six length-seven reset words for the specified witness, including 0010110; BFS excludes shorter words. The supplied seven-level signature quotient is also valid: each individually resettable subset graph has a singleton path of length at most six, right extensions preserve reset, and every signature triple had a nonempty intersection by seven. In arXiv v1 the cited product results are Lemma 5 and Proposition 7, not Lemma 3.1 and Proposition 3.4; this bibliographic slip does not enter the finite proof.

## originality

PASS

The exact triple threshold and weighted labeled census are not supplied or implied by the strongest located pair or product results. The 549 single machines and the pair length census are not separately novel; the general product identity is established background.

## value

PASS

The natural first extension from two to three shared-letter components has a distinct obstruction: even universal six-letter pair compatibility does not give six-letter triple compatibility. The exact seven-layer classification, including 165888 worst-case labeled triples, gives a usable complete benchmark for simultaneous synchronization rather than an arbitrarily sampled enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
