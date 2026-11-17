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

# Verification and limitations

The scientific proof is in `RESULT.md`. To corroborate the critical exact arithmetic, run `python3 verify_threshold.py` with Python 3 standard library. The script checks the modulus-14 rational witness, the strict discriminant inequality, selected geometric probabilities, and convergence toward a two-cycle for one initial scalar value; the universal claims are proved analytically in the result.

No independent mathematical validation has been performed. The older scalar quadratic map dichotomy is used as a cited result. No claim is made that finite computations independently establish the infinite-family statements or that novelty is mathematically certified by unsuccessful search.
