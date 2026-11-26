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

Independently reconstructed the disjointness graph and reproduced the entire enumeration with block masks, not either supplied program. Distinct intersecting two-subsets have distance two via their common disjoint complement. For each nonempty block, precomputed the mask of the 105 unordered edge pairs distinguished using the minimum of endpoint distances. Recursion takes each block containing the least remaining vertex, giving exactly one path per unordered partition; all 105 bits must be covered. The replay counted 115975 partitions, with accepted counts (0,0,0,40,11965,14877,5045,720,45,1) for 1–10 blocks, totaling 32693. All four-block optima have sizes (1,3,3,3) and their set equals the 40 distinct images of the stated witness under all 120 ground permutations. Independently recovered the 105 and 15 three-block screen counts and checked that the latter partitions have two adjacent singleton blocks. Replay: python3 /workspace/reviews/petersen_replay.py. The frozen scripts and logs were inspected but not executed. This is an exhaustive finite verification for the Petersen graph only.

## originality

PASS

The exact global edge-partition census and orbit classification are distinct from surveyed vertex-partition and edge-landmark results, and correct a conflicting printed global value. This is a bounded statement-level assessment, not a historical priority guarantee.

## value

PASS

This corrects a specific published value for a standard invariant on a canonical graph, with a concrete short counterexample. The exhaustive finite census also settles the lower bound, identifies the unique symmetry orbit of optima and quantifies all block counts; it is useful as a benchmark for broader partition-resolvability work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
