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

# Reproducible mathematical checks

Run `python candidate_check.py` and `python tridiag_check.py` using Python 3.10+ with the standard library only. The companion text files capture the respective complete outputs.

The first checker directly constructs the \(2^n\)-dimensional exterior-multiplication matrix from each coefficient vector over the seven tested prime-field cases, computes the ranks of all powers, compares with a separate inclusion-matrix rank formula, and checks the entire alternating-form population. This is exhaustive **within each listed finite test field and dimension**; the tests are not an exhaustive search over all dimensions or fields. Additional finite-field identities include field sizes \(q=4,8,9\), where polynomial totals are evaluated but complete coefficient matrices are not enumerated.

The second checker independently computes \(T_p^r\) and the resulting Jordan partition and checks that its power ranks agree with the incidence formula for 605 parameter triples. It also checks selected nonprojective fractions and alternating-form totals. The tested formulas have a general algebraic proof in `RESULT.md`; neither program certifies the infinite-family assertion by itself.

Expected final markers: `QUADRATIC_EXTERIOR_JORDAN_WILSON_PASS` and `QUADRATIC_EXTERIOR_TRIDIAGONAL_PASS`. All output data must be regenerated from the accompanying standalone source scripts; no external dependencies, network access or unprovided data are used.

Independent audit: not performed.
