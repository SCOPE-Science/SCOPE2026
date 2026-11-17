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

The standalone `verify.py` uses only Python 3 standard-library exact rational polynomial arithmetic. It reconstructed and equated both full two-step quartics and both completed-square normal forms coefficient by coefficient in three indeterminates. It also evaluated exact rational representatives of all four phase-ordered valence regions, checked interval-width arithmetic, and tested the four-versus-two phase-specific successor equations for \(\varepsilon=1/100\) together with the exact multiplier \(-10000\).

The logical passage from derivative signs and completed squares to *all* real targets, all real parameters and the optimal inverse exponent is proved in RESULT.md, not inferred from finite tests. The checker does not establish independent certification or publication priority. Expected terminal marker: `VERIFY_OK exact_polynomial_normal_forms=2 distinct_phase_maxima=4 witness=1`.
