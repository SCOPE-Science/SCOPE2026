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

The proof uses the explicit support formula, a uniquely crossing tangent equation, monotonic support levels, and Green's theorem. Its complete quantifiers cover every real \(T>0\). Asymptotic statements use analytic Taylor expansions at the stated endpoints.

Run `python3 CHECK.py` with NumPy and SciPy installed. The checker computes actual convex hull areas and perimeters of dense independent point samples for eleven arc lengths, tangency comparisons and the asymptotic scales at the two limits. It returns `ARCHIMEDEAN_SPIRAL_HULL_CHECKS_OK` when all tests pass. Finite samples cannot validate all parameter values or independently certify the proof. Independent audit status is not performed.

The strongest closely related geometric published result concerns a logarithmic spiral, not the present finite linear-radius family. Historical priority is still subject to independent assessment.
