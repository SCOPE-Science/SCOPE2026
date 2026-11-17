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
# Verification record

Run `python3 verify.py` with Python 3 standard library. This tests the second *distinct* squared vertex-pair Euclidean distance, its count, and its allowable unordered layer types, not any continuum second maximum.

Expected successful output:

`PARKING_SECOND_SHELL_PASS exhaustive=[(2, 3, 2, 1, 2), (3, 10, 9, 8, 6), (4, 41, 26, 23, 48), (5, 206, 54, 50, 120), (6, 1237, 100, 95, 720)] complete_layer_profiles_n=2..150`

Each exhaustive tuple records dimension, vertex count, largest squared vertex-chord distance, second-largest distinct squared distance, and number of unordered second-shell pairs. All statements for every dimension are proved analytically in RESULT.md. Finite verification alone proves nothing beyond tested dimensions. Numerical optimization, formal proof assistants, and external independent review were not used.
