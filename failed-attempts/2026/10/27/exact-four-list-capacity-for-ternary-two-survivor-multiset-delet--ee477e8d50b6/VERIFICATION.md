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

There are six possible outputs and the cap of four gives at most 24 incidences. At n≥4 the three pure sources have degree one, the six (n−1,1,0) sources degree two, and every other source has degree at least three. Degree three requires exactly two positive coordinates, both at least two; three positive coordinates already give the three mixed pairs plus a monochromatic pair. For a putative 12-word code the total degree is at least 36−2·3−6=24, hence all nine low-degree words and exactly three degree-three words are required. The nine use three places in each monochromatic list, whereas the other three would need six of the three remaining places. Deleting codewords cannot violate the list restriction, so every larger size is also impossible. The nine low-degree words plus (n−2,1,1) and (1,n−2,1) give distinct words with loads (4,4,3,4,4,4) in the stated convention. At n=2 the channel is identity on six sources; at n=3 each output acquires precisely three distinct parents by adding one symbol, so all ten sources fit. The contextual first-failure claim is correct: at allowance one use just the pure words; at allowance two add the three cyclic majority/minority choices; at allowance three use all nine low-degree words.

## originality

FAIL

The exact n≥4 capacity 11 for this same channel is explicitly stated in the 2026/10/26 Resultary high-list record, which calls it a separately recorded special case. The distinct 2026/11/22 optimizer-classification record states and proves the same capacity with the same hypotheses and a stronger classification (including the frozen construction). This is affirmative equivalent coverage. The first record's unidentified antecedent does not resolve historical priority, and the second record's later path date is not evidence of earlier priority. The leftover n=2 and n=3 statements are just the full source space, not a distinct theorem.

## value

FAIL

The first departure from the monochromatic capacity bound is a motivated channel question, and the degree proof is useful for understanding it. But the frozen contribution is the already indexed exact capacity and a construction in an already indexed optimizer family, without a new structural consequence. The remaining lengths just use every source. There is no distinct useful exact fact here to retain as a separate contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
