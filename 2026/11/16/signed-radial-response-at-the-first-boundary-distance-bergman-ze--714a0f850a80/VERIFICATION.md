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

The complete analytic proof and precise domain are in `RESULT.md`. `CHECK.py` is a standalone Python script using standard Python plus SymPy/mpmath; running `python CHECK.py` prints `PASS: 37 independent assertions (symbolic, integral and numerical)` on a successful run. Assertions reconstruct the squared-moment generating function, verify the sign-changing reciprocal quartic and its two roots, evaluate the exact linear-tilt integral, and compare monomial-series and integral expressions at finite parameters.

Critical infinite arguments are mathematical, not numerical: uniform exponentially small moment-coefficient corrections for interior-supported perturbations, pole dominance, compact-set zero exclusion, and Rouché/implicit function zero tracking; for the linear tilt, an exact integral decomposition supplies pole dominance. All zero counts apply to scalar products inside the open unit disk. No independent mathematical audit was performed and these finite checks are not independent certification.
