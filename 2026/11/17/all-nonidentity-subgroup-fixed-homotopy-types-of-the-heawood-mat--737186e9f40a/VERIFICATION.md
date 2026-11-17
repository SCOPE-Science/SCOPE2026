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

The reconstruction uses `verify_fixed.py` and the self-contained finite certificate `census.json`, placed in the same directory. Run `python3 verify_fixed.py`. The program reconstructs every automorphism, subgroup, conjugacy class, edge orbit, matching face, and collapse pair; verifies the residual complexes and group-presentation eliminations; and compares its complete calculation with the independently saved census. The expected concluding line is `ALL_HEAWOOD_MATCHING_SUBGROUP_FIXED_HOMOTOPY_TYPES_PASS`. The completed run is recorded in `verification_output.txt`. The computation proves the stated finite exhaustiveness, but does not certify novelty or replace external independent review.
