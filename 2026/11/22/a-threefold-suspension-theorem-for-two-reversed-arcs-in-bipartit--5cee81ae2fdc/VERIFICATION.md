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

# Reproduction and proof limits

Run `python verify_two_reversals.py` with Python 3. The script uses only the standard library and computes full directed-multipath face sets for small graph instances. It verifies the missing-cycle cone cases, the link as a three-edge-path avoidance subcomplex, the identification of the residual matching link and the predicted shifted reduced homology over the field of two elements. The included `verify_output.txt` records the actual run with 457 graphs containing both crossing edges, 100 missing-cross checks, 70,002 enumerated faces and 435 homology checks.

These enumerations do not prove the unbounded all-graph theorem or establish its integral torsion: those follow respectively from the cofiber proof and the published integral chessboard calculation cited in the theorem. The finite checks test the critical structural equalities and expose small-case counterexamples if present. This is not independent expert verification.
