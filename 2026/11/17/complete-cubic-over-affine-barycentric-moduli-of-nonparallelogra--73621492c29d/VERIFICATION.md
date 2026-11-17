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
# Verification record

The included `verification.py` executes with SymPy. The script checks symbolic normalization, both coordinates of linear precision, and the unique solution of the generic affine-denominator boundary system; it also establishes a polynomial identity proving projective injectivity and verifies the four closed-polygon denominator vertex factors. It matches the explicit trapezoid example in Baumbach–Winter, arXiv:2611.02110v1, exactly.

The rational-grid diagnostics use four pairs of base lengths, multiple cone-boundary and interior parameters, and a \(17\times17\) grid for each such instance. All checked denominators were positive and all checked numerator values nonnegative; these grid checks are finite diagnostics, not proofs for arbitrary real parameters. The universal validity and sharp positivity conditions are proved in `RESULT.md` by factor signs and affine interpolation. The program does not purport to certify literature priority or independent validation.

Reproduction: `python verification.py`, requiring Python and SymPy. The script has no external-data dependencies.
