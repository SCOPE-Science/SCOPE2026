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

The ordinary Python 3 program `verify.py` constructs the 16-state fixed-column transfer graph and computes all coefficients of its determinant using integer Newton identities. It also performs independent direct Moore-neighborhood updates on all configurations of two-row cylinders of circumferences three through eight (87,360 one-step cases), comparing them against the independent column update, checking the strict potential, and comparing exact fixed-point counts to matrix traces. The 3-by-4 width-three two-cycle is checked in the same direct-neighbor engine. Run `python3 verify.py`; the expected single-line JSON is embedded as `verify_output.json`.

The finite test is not relied upon for the proof at arbitrary circumference. The all-length correctness comes from the exhaustive symbolic three-column occupancy cases in `RESULT.md`, integer descent, and the closed-walk bijection. The upper bound on convergence time is not claimed sharp. The reader can independently inspect the core transition cases, the integer matrix, and the direct witness.
