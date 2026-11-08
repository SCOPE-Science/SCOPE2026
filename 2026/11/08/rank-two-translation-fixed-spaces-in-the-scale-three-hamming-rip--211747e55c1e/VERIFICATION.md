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

# Reproducible checks

`verify.py` reconstructs all orbit cosets using XOR and Hamming-weight distances, without constructing expected graphs from the proof. It tests each rank-two subgroup in dimensions 2–8, including all 14,311 possibilities and all three integer Rips scales 1, 2, 3.

For each scale-three graph classified as a cube, it independently builds a breadth-first coordinate labeling and checks every edge against Hamming distance one on the labels. For circle unions, it verifies that every component is a connected 4-cycle; empty cases are checked exactly. For scale two, it tests the precise count of isolated orbits. Counts are compared against the binomial expressions for all dimensions.

Actual command: `python3 verify.py`.

Expected terminal marker: `RANK_TWO_FIXED_GRAPH_CLASSIFICATION_OK`.

The log in `verification_output.txt` was produced by executing that code in the extracted package. The computation is a finite consistency test; the proof for all dimensions is in `RESULT.md`. No independent mathematical audit has been conducted.
