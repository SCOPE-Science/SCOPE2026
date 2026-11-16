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

The included `check_bicycle.py` executes entirely with Python's standard library and checks the direct Boolean Walsh transforms against finite-field bicycle ranks for all 771 connected simple labelled graphs on 2--5 vertices. It verifies the full \(Q_1,Q_2,Q_3\) transforms and a \(Q_4\) sharpness determinant witness, as well as one cographic regular matroid.

Run `python3 check_bicycle.py`. The expected terminal marker is `REGULAR_MATROID_BICYCLE_WALSH_CHECK_PASS`. The verifier uses exact integer arithmetic and has no cached data dependency. It does not certify the all-dimensional proof or independent mathematical audit, and it does not check general regular matroids exhaustively.
