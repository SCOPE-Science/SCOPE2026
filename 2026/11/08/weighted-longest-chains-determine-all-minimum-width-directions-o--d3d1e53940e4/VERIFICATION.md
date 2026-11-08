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

# Reproducible checks

Run `python3 verify.py` with Python 3. The script uses only the Python standard library and exact integer arithmetic. The observed output was:

`POSET_WEIGHTED_WIDTH_CHECKS_PASSED poset_weight_profiles= 1221 filter_sets= 15690 heaviest_chains= 1789`

The checker exhausts transitively closed relations compatible with one fixed labeling order for up to five elements, three positive integer inverse-square scale profiles for each relation, and a finite grid of signed integer normals. It verifies the sharp inequality after clearing denominators and checks the predicted equality directions against exact filter projections. These tests do not verify every finite poset, scale profile or real direction. The rigorous proof is in `RESULT.md`, and all facts needed for its mathematical argument are stated there.
