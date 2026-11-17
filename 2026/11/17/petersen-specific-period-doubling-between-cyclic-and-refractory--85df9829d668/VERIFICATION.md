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

# Verification of the finite joint-period classification

All three included programs are deterministic, require no network access, and use integer-state encodings. They are replayable from the directory immediately above `verification`:

```
python3 verification/verify_graph.py

g++ -std=c++17 -O2 -Wall -Wextra verification/verify_trajectories.cpp -o verify_trajectories
./verify_trajectories

python3 verification/verify_symmetry.py
```

Compare the three resulting outputs, respectively, against `verification/verify_graph_output.json`, `verification/verify_trajectories_output.txt`, and `verification/verify_symmetry_output.txt`. The first computes complete transitions and removes indegree-zero states before enumerating cycles; the second reconstructs the local rule and runs Floyd cycle detection on every input; the third enumerates the 120 vertex-permutation actions on all discrepant states.

For each graph, precisely 59049 initial three-colorings are enumerated. The nonzero Petersen joint-count classes are 1/1:7839, 3/3:4500, 4/4:5040, 5/5:27270, 8/4:4800, and 8/8:9600. The pentagonal-prism classes are 1/1:8409, 3/3:2460, 4/4:38430, 5/5:2190, and 7/7:7560. All other classes are zero, and each table sums to 59049. The value 4800 partitions into exactly forty 120-element symmetry orbits.

Limits: finite graph pair only, no probabilistic sampling or extension to arbitrary cubic graphs; program agreement is not equivalent to independent external validation. No external mathematical audit has been performed.
