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

# Reproduction and scope

Compile `chvatal_enum.cpp` as C++17 and run it; the output is `chvatal_census.txt`. Run `chvatal_independent.py` with Python 3, which prints `chvatal_independent.txt` and writes `chvatal_joint_census.csv`. Both replayed successfully. The first implementation computes all \(531441\) successor states and peels indegree-zero transient states; the second computes successors from a different neighbor representation and memoizes each trajectory. Their full 52-class joint distributions and the exceptional period-eleven counts agree. The symmetry witness checks three excitations per vertex on every eleven-cycle and eight explicit graph automorphisms and confirms that the induced images of one eleven-cycle are all eight distinct eleven-cycles. The graph checker also verifies degree four, no triangles and chromatic number four. The source code and output files are the reproducibility evidence.

The proof is exhaustive only for this explicitly listed 12-vertex graph and the deterministic synchronous threshold-one three-state update. The results do not certify historical priority or claims for other graphs. Independent external audit remains unperformed.
