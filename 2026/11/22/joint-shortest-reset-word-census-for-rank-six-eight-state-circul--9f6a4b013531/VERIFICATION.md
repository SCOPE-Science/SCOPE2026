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

I reproduced the full table independently using Python integers, not the frozen executables. The generator enumerates the 266 partitions of eight inputs into six nonempty fibers and all 8P6 injective output assignments; lexicographic cyclic conjugation gives one map per orbit. Breadth-first distances from the full subset define a shortest-path DAG. Backward suffix counting in that DAG sums each letter separately, including coincident image edges. I timed 8 fiber patterns, then exhausted contiguous ranges [0,8), [8,72), [72,136), [136,200), [200,264), [264,266), saving each range. All 5,362,560 maps yielded 670,608 representatives (576 size-four orbits, as by Burnside), and every one of the 648 joint entries and 121 word-marginal entries matched the frozen CSVs. This includes 6,928 nonsynchronizing, 663,680 synchronizing, 388,869 with one shortest word, the unique (30,110592) and (36,8) cells, both representative maps and quoted reset words, and the 1–32 range at length 10. The frozen prose incorrectly says both packaged algorithms guard overflow: the reverse guards its additions; the forward uses unchecked 64-bit arithmetic. The repair corrects that description; the claims and tables are unchanged and the independent exact computation does not rely on either arithmetic implementation.

## originality

PASS

Only the joint shortest literal word multiplicities and their new extremal information are credited. The same-day same-family threshold spectrum, orbit count, and threshold extremizer are explicitly cited and excluded from the distinct contribution. No order within that date is inferred.

## value

PASS

This is the complete multiplicity classification of the same eight-state defect-two circular stratum whose length distribution was already a studied finite census, not an arbitrary small instance. Literal shortest words distinguish automata with the same threshold and measure how many minimal control sequences are available. The complete table and sharp witness show that the longest-threshold automaton is not the multiplicity extremizer, and give exact benchmark counts for independent algorithms or later structural work. No new shortest-path algorithm or extrapolation is credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
