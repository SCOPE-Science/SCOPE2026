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

# Reproduction

Execute both Python standard-library scripts from this directory: `python3 verify_deletion.py` and `python3 verify_geodesics.py`. Both require Python \(3\); no third-party packages or external data files are needed.

The first checker constructs the \(20\)-vertex dodecahedron as \(GP(10,2)\), calculates its \(30\) edge-deletion distance matrices and exhaustively tests all seven- and eight-element subsets. It then derives the induced-edge classes, intersection counts and the radius/diameter of the three-replacement reconfiguration graph.

The second checker uses an independently listed planar dodecahedron and counts shortest paths using breadth-first-search recurrence. It validates an explicit isomorphism permutation to \(GP(10,2)\), independently enumerates the same candidate sizes and checks the same configuration geometry.

Both scripts must exit successfully and print `PASS`. Failure of any assertion invalidates the computational certificate. The included `optima.json` is a complete list of the optima in the first labeling. Exhaustive finite testing proves only this particular graph result; it does not prove generalization to other graph orders or establish literature priority.
