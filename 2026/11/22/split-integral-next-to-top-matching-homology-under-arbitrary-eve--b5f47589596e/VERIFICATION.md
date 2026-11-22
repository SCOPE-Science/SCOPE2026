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
# Verification

Run `python verify.py` from the extracted package. The standard-library code reconstructs every matching of the two eight-vertex graphs and explicitly checks acyclicity in the full oriented nonempty-face Hasse diagrams. It verifies all 45 relative free-face pairs after deleting a graph perfect matching. It also checks the six-cycle's complete face vector, connected one-skeleton and free triangles.

The reported counts and full PASS output are recorded verbatim in `verification_output.txt`. The finite results justify the two concrete sphere-wedge and cofiber computations; the all-even-order theorem is established by the relative collapse and exact-sequence proof, not extrapolated from data. No independent audit or full literature-uniqueness certification has been performed.
