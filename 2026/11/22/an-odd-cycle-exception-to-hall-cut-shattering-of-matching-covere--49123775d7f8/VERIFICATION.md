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

# Reproducible verification

With Python 3, run `python3 verify_cycles.py` in the directory containing the supplied checker. It enumerates actual graph matchings, all vertex-query supports, crossing-matchings and exceptional covers, and finite Littlestone recursion, for orders 3 through 11. Compare with `verification_output.txt`.

The unrestricted proof is in RESULT.md; finite experiments do not establish claims beyond the verified range. An independent scientific audit has not been conducted.
