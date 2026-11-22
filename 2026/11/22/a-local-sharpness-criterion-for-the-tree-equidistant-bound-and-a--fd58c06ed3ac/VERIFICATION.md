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

# Reproducible finite checks

Build and run `verify_trees.cpp` with `g++ -O3 -std=c++17 verify_trees.cpp -o verify_trees && ./verify_trees`. Expected exact output: `TREE_LOCAL_EQUALIZER_VERIFY_OK trees=18748 part_classes_valid=19090 both_classes_valid=5991`.

Run the separately written standard-library script with `python3 verify_midpoints.py`. Expected output: `TREE_MIDPOINT_INDEPENDENT_OK 1616`.

The C++ verifier examines all labeled Prüfer trees on two through seven vertices, then 100 deterministic additional trees at each order eight through twelve; for each tree it tests every vertex subset with the literal shortest-path definition. The Python verifier repeats the comparisons with a different tree construction and direct distance computation for 1,616 cases. These tests establish only their finite coverage; the general theorem is proved in `RESULT.md` by parity, midpoint geometry, and the local branch condition.
