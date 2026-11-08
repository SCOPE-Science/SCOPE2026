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

The polynomial identity follows from Pick's lattice-polygon Ehrhart count and the degree-four finite-difference formula. Run `python verify.py` with `DISCRIMINANT_CERTIFICATE.json` in the same directory and Python 3 with SymPy available. The script reconstructs, with integer and rational symbolic arithmetic, every coefficient of the 4-dimensional numerator, all 84 coefficients of the three positive discriminant polynomials, all three cubic discriminants, all degree-drop quadratic discriminants, and all strict negative-point witness inequalities.

The positive-discriminant criterion uses the elementary real quartic root-count alternative: positive discriminant means either four distinct real roots or two nonreal conjugate pairs; two sign-forced negative roots exclude the latter. For cubic boundaries, positive discriminant means three distinct real roots. These are exact all-parameter proofs, not limited root-finding experiments. The original Wagner theorem for factors with real-rooted numerators is used with its explicitly stated hypotheses. No separate independent mathematical validation has been conducted.
