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

# Mathematical verification

The main assertion is established by a complete analytic proof in `RESULT.md` with an exact support-line reduction, an exact reciprocal substitution, trigonometric multiplier identities, a strict weighted-Bessel equality obstruction for all even periods at least six, and a separate exact square classification. The crucial two-character obstruction requires both indices two and four to lie in the nontrivial Fourier band, which explains the sharp four-versus-six distinction.

Reproduce the finite sanity checks by executing `python check_recurrence.py` with NumPy installed. The actual saved checker returned `PASS: 2488 finite exact-rational/numerical assertions.` The exact-rational cases verify four-period solutions and square-area atoms; numerical checks independently evaluate the cotangent identities and weighted operator norms for several even periods. A separate symbolic substitution verified that the change of variables in the geometric recurrence yields the reciprocal recurrence with residual identically zero. These calculations do **not** certify all periods; the written proof supplies that step.

No independent audit, priority determination, or external certification has been performed. The geometric claim is limited to positive-support strict polygons with the stated facet normals and fixed regular Minkowski sum.
