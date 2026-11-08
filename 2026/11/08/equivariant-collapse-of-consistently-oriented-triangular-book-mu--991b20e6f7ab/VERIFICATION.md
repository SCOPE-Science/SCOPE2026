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

The standalone program `verify.py` rebuilds the directed book and enumerates all admissible faces independently for page numbers one through seven. It cross-checks the explicit face list, the free-face pairs, and the residual graph, and calculates reduced mod-two homology for page numbers one through five. All 30 distinct two-generated subgroups of the permutation group on four pages were checked for invariance of faces, fixed-support equality and orbitwise free-face cancellation.

Run `python3 verify.py` in a directory containing the extracted files. The `verification_output.txt` file records the actual execution result and finishes with `ALL_VERIFY_OK`.

The general theorem depends on the symbolic face classification and equivariant elementary collapses proved in `RESULT.md`. Finite checks are corroboration only, not an exhaustive proof over arbitrary page counts or subgroups. All integer homology and fundamental-group assertions follow from the exhibited graph retraction. No external independent audit has been performed.
