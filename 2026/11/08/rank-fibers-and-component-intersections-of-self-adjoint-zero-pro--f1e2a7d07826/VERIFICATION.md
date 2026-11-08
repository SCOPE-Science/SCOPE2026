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

# Reproduction and verification

Use Python 3 and NumPy, executing `python verify_zero_product.py` and `python verify_incidence.py` in a directory containing the supplied files. Each script is standalone except for this declared dependency; neither reads earlier research artifacts. Actual standard output is supplied as `zero_product_output.txt` and `incidence_output.txt`. Their terminal success markers are respectively `ALL_SELFADJOINT_ZERO_PRODUCT_TESTS_PASS` and `ALL_SELFADJOINT_INCIDENCE_TESTS_PASS`.

The rank checker literally multiplies symmetric matrices over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\), checks every rank fiber, separately verifies a nonstandard symmetric bilinear form over \(\mathbb F_3\) and an alternating symmetric form in characteristic two, and evaluates a complete \(\mathbb F_4\) example with an explicit irreducible polynomial. The incidence checker enumerates every pair over \(\mathbb F_2\) in dimensions one through three and verifies the proposed rank-defined component sets and their pairwise incidence cardinalities.

Specific total checks include \(Z_2(2)=18\), \(Z_3(2)=204\), \(Z_4(2)=4392\), \(Z_2(3)=69\), \(Z_3(3)=2601\), and \(Z_2(4)=172\). The scripts do **not** prove smoothness, geometric irreducibility, or the formula for arbitrary fields; those claims depend on the incidence-bundle argument in `RESULT.md`. The verification does not establish scheme-theoretic radicality or historical uniqueness.
