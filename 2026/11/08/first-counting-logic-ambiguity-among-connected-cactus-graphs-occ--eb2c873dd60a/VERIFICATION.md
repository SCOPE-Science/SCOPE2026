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

The graph enumeration and globally synchronized color refinement are contained in `verify.py`. It uses exact nested integer tuples, sorted neighbor multisets and graph-block canonical strings, with no hash-based acceptance condition. The 12-vertex layer comprises exactly 24,118 isomorphism types and 24,116 stable-color classes, including two doubletons; `verification_output.txt` records the full exact replay. Other explicit checks compare published connected-cactus order counts, test each doubleton with NetworkX isomorphism, and verify blocks and degrees. The exhaustive finite computation proves only the displayed cutoff; a machine-independent proof of the generated census is not claimed, nor has an independent external mathematical audit been performed.
