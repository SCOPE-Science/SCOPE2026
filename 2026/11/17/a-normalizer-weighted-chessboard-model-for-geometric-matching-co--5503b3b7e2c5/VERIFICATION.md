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

# Reproducibility

Run `python3 orbit_chessboard_verify.py` using the Python standard library. The exact expected stdout is contained in `orbit_chessboard_verify_output.txt`.

The script constructs eight explicit small group actions, generates all row/column orbits and edge orbits, enumerates equivariant bijections from their underlying finite group action, checks all invariant simplicial matching supports, and compares every eligible-orbit subset to the predicted multigraph face condition. It separately enumerates 19,091 faces of a five-by-five board having two parallel edges per square, checks the exact face-count formula in every dimension, and verifies the forget-color/choose-color maps on every matching.

The verification is finite. The all-group statement is supported by the abstract proof in RESULT.md. The split three-torsion conclusion relies on the previously established integral homology of the ordinary five-by-five chessboard (Jonsson, Theorem 3.1; Shareshian–Wachs), not on a new computational homology calculation. No independent audit is represented by these checks.
