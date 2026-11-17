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

Run `python3 verify_mayer.py` with a standard Python 3 interpreter. The script requires no external modules. Its output is recorded in `verification_output.txt`.

The two finite fields are used only for exact finite arithmetic verification, not as replacements for characteristic-zero proof. The script checks the exact boundary matrices for all tournament sizes 1 through 9 and independently checks the three-step lost-edge complement for each size 4 through 9. The coefficient of the missing arc in the double boundary is nonzero, and every checked third boundary is zero. The all-size proof, including bar-splitting and the direct complement for the deleted edge, is in `RESULT.md`.

This verification does not establish claims for other primitive root orders, arbitrary missing arcs, or unindexed literature; no independent mathematical audit has been performed.
