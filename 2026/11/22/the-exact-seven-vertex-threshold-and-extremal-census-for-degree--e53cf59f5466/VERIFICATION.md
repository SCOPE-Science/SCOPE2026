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

Independently enumerated complements with 8 and 7 edges (203490 and 116280 masks). For smaller shore size k=1,2,3, test each vertex's missing cross-degree against the opposite shore's size minus 2. These are all possible cut sizes, including singleton cuts. Zero immune graphs at 13 present edges also excludes fewer edges since adding edges preserves immunity. Exactly 15015 graphs at 14 present edges passed. Independently transformed the ten TSV edge sets under all 5040 permutations: the disjoint orbits exhaust those 15015 graphs, with sizes 105,2520,2520,1260,2520,1260,630,2520,1260,420. The redundant graph6, degree and automorphism columns also agree. Replay: /workspace/review-check-3.py (Python/NumPy); frozen C++ inspected, not executed.

## originality

PASS

The directly verified closest preprint has the same invariant but only a weaker general lower bound at order seven. No inspected independent exact census claims or determines the 13-edge obstruction and 14-edge extremizer inventory. This is a best-of-knowledge decision, not publication priority.

## value

PASS

This natural small order resolves whether the general 2n−2 sufficient edge bound for existence of a 2-cut can be sharpened there. The ten-way extremal census and orbit sizes provide concrete witnesses and benchmarks for structural conjectures, beyond a single threshold calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
