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

# Finite exact verification

The claim applies only to levels one to fifteen of the published accelerated graph recurrence. The standalone `forward_census.cpp` reconstructs all graphs and performs exhaustive BFS from every source vertex; connectivity, eccentricity and all-pairs distance histograms are computed exactly with integer arithmetic. The tabulated histograms have sum \(2^{2n}\), with exactly \(2^n\) zero-distance ordered pairs.

The separately implemented `reverse_census.cpp` constructs the same adjacency recurrence in a different loop, transposes each permutation and runs BFS from every terminal vertex; its results reproduce the fifteen diameters and fifteen farthest-pair counts in `reverse_checks.txt`. The Python tuple-state verifier reproduces the first nine levels independently.

Compile with `g++ -std=c++17 -O3`; no additional libraries are required. The complete distance histograms, which distinguish directed ordered pairs, are stored in `census.tsv`. Full graph enumeration at level 15 covers \(2^{30}=1,073,741,824\) ordered pairs; this is exhaustive finite evidence, not a proof for levels beyond 15. The elementary outdegree-two lower bound \(D_n\ge n\) holds for all finite connected graphs in this family. Accelerated-edge distance is not original shift-time distance. No independent mathematical audit was performed.
