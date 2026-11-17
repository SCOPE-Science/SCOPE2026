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

Run `python3 check_sphere_double_sum.py`, followed by `python3 validate_gluing_types.py` from the directory containing both files. No external Python dependencies are required. The former directly enumerates facets, double edges and their connected components for 16 admissible parameter pairs; the latter checks all 24 gluing permutations for a 4-by-5 polygon join. The exact output is embedded in `verification_output.txt`.

Numerical enumeration verifies finite cases only. The proof for all admissible integer parameters is in `RESULT.md`. The checker does not independently prove the general path-detour lemma, and no independent human audit or certification has occurred.
