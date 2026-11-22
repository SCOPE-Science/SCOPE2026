---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Two standard-library Python programs reproduce the exact finite enumeration using different algorithms: `verify_global.py` constructs every globally disjoint-shadow family and checks each family against references, while `verify_reference.py` constructs each reference's word set and searches its deletion-shadow graph directly.

The measured reference counts by maximum correcting-code size are:

| Reference length | Capacity-count distribution |
|---|---|
| 3 | 1:27 |
| 4 | 1:81 |
| 5 | 1:33, 2:210 |
| 6 | 1:39, 2:336, 3:342, 4:12 |
| 7 | 1:45, 2:570, 3:1074, 4:498 |
| 8 | 1:51, 2:1002, 3:2490, 4:3018 |
| 9 | 1:57, 2:1824, 3:5292, 4:11214, 5:1296 |

The exact optimizer set at reference length six is the orbit of `012021` under alphabet relabeling and reversal. All twelve support one four-word correcting code whose one-deletion output sets partition the nine ternary digrams. The finite calculations check exhaustive reference spaces, not randomly selected samples.

The all-length capacity claim relies additionally on the mathematical proof: every five-word correcting code is one of three classified families, all containing three copies of each constant word, so a reference must have at least nine positions to synthesize it; the shorter-length bounds follow from embedding-set intersections. No result beyond ternary length-three codewords is asserted.
