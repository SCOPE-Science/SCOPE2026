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

# Verification steps

Run `python verify_600.py` in the directory that also contains `spanning_tree.json`. The script uses only the Python standard library; it reads the explicit 720-entry parent list and recreates the 600-cell from exact coordinates. The included `verify_output.txt` is the captured output of an actual local replay. The following were checked exactly: 120 unique radius-two vertices, 720 original nearest-neighbor edges, 600 exposed tetrahedral facets, two facets per each of 1200 triangular faces, 720 opposite-edge double vertices, 1800 distinct double edges, degree five at all double vertices, a root-reaching 719-edge spanning tree, and girth six. The count 1081 follows by the connected graph Euler characteristic.

Algebraic signs are evaluated using integer arithmetic in `Z[phi]`, where phi satisfies phi^2=phi+1. No floating-point geometry is used for the certificate. The program does not by itself establish publication priority or independently certify the mathematics; those are distinct from exact finite computation. The mathematical reduction from a connected graph to a wedge of circles is written in `RESULT.md`.
