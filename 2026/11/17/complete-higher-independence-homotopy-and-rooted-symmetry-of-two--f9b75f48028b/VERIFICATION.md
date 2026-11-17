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

Run `python3 height_two_verify.py` with Python 3.9 or later. It uses no third-party dependencies. It independently enumerates graph faces and link faces, performs exact mod-two boundary rank calculations, checks the full oriented face-incidence graph of every link matching for a directed cycle, computes exact signed simplicial Lefschetz traces for rooted symmetries and compares with the exterior-power formula. It checks 75 threshold/profile instances, 25,452 face incidences, 1,118 group-character identities, and the mixed profile \(q=(4,4),r=3\). The script reports `HEIGHT_TWO_TREE_EXACT_PASS`.

These tests are exhaustive over the *listed finite cases*, not over all parameters. The mathematical proof in RESULT.md supplies the unbounded argument, including the only nonstandard needed classification step (critical-face enumeration). No integral equivariant splitting is asserted.
