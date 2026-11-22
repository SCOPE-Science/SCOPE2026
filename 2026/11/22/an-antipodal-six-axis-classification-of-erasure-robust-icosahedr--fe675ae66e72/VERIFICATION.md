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

## Reproducible checks
From the directory containing the complete extracted files, run `python3 -S verify_sets.py` and `g++ -std=c++17 -O2 -Wall -Wextra verify_masks.cpp -o verify_masks && ./verify_masks`. Neither verifier uses downloaded datasets or nonstandard libraries. Their code is included complete, not as a difference or a reference to any external file.

The Python program reconstructs the thirty edges by an explicit cyclic-ring construction and independently checks all 4096 subsets against every closed-neighborhood and vertex-pair distinguishing requirement. It obtains minima and counts \((5,120),(6,20),(11,12),(12,1)\); finds exactly twenty triangular faces, verifies their 3-sun extensions, and asserts unique extension of all 120 ordinary optima. It also calculates graph distances and the pair-union structure of the fifteen distinguishing four-sets, each arising from two edges.

The C++17 program constructs the same abstract graph from a separate literal thirty-edge list, uses bit masks to check all 78 constraints per candidate, and independently verifies all optimum sizes/counts and additional graph structure. Each program terminates with a `PASS` message only after its numerical and structural assertions succeed. The mathematical proof in RESULT.md additionally derives the counts and sharp bounds from antipodal occupancy constraints and a five-cycle pattern count, without using the programs' asserted results as premises.

The verification applies exactly to this twelve-vertex graph and the specified closed-neighborhood erasure convention. No independent scholarly review or external proof certification is claimed.
