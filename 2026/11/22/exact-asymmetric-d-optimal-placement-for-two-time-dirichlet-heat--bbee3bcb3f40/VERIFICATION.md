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

# Verification and limits

The analytical global-optimality proof is in `RESULT.md`. A supplementary executable, `CHECK.py`, uses only the Python 3 standard library and directly reconstructs the two-by-two heat-observation matrix for multiple time ratios and unrestricted sensor locations. Its previously observed output is in `CHECK_OUTPUT.txt` and is reproduced by `python3 CHECK.py`.

Its finite grid and random comparisons provide numerical corroboration only, not exhaustive proof over the continuum or publication-priority certification. The exact equality cases follow from strict concavity and the triangle-equality step. The long-time and short-time formulas follow from analytic expansion of the quadratic root. The scientific scope excludes nonidentical observation noise, additional modes, and sensor motion constraints.
