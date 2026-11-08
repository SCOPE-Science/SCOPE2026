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
# Reproducibility and verification

Execute `python3 verify.py` from a directory containing the bundled standalone script. It requires Python 3's standard library and no network access. The captured `verification_output.txt` is the expected output. The script exhaustively enumerates scalar-normalized implementing matrices \(A\), tests \(A^2+A\) scalar and the original Leibniz/idempotence identities for derivations, and computes their bivariate rank distributions. It tests commutation directly on derivation maps in the smaller configurations, with a proved commutation-to-implementer equivalence used for the four-dimensional case. The checked fields are \(\mathbb F_2,\mathbb F_3,\mathbb F_4\), with \(\mathbb F_4\) implemented as a genuine extension field.

Verified pair totals include \(13\) for \((n,q)=(2,2)\), \(49\) for \((2,4)\), \(253\) for \((3,2)\), and \(18169\) for \((4,2)\). All coefficients agree, not only totals. The final marker is `COMMUTING_IDEMPOTENT_DERIVATION_BIVARIATE_RANK_OK`.

**Boundary:** finite exhaustive checks cannot prove an assertion for all dimensions or field sizes; the independent six-step mathematical proof is in RESULT.md. These checks do not verify conjugacy classifications, nonlinear maps, or arbitrary (non-idempotent) derivations. Independent audit is not performed.
