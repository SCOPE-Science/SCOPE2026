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

# Reproduction and proof dependencies

The `verify.py` script requires Python 3 and only its standard library. It independently enumerates the 156 rational points of projective three-space over \(\mathbb F_5\), its 806 projective lines, all 66 rational points of the Weddle quartic, all 25 contained rational lines, and the complete six-fivefold/sixty-double line-incidence table. It separately enumerates 16,276 points of projective three-space over \(\mathbb F_{25}\), obtaining 1,026 points on the quartic and 460 outside the distinguished line divisor. It finishes with `VERIFY_OK`; the exact output is in `verify_output.txt`.

The `verify_singular.py` script requires SymPy 1.12 or later. It reproduces the determinant identity \(\det(\partial q_i/\partial x_j)=2f\), the two complete affine projective Jacobian Gröbner bases, and nonzero three-variable Hessian determinants at all six singular points. It finishes with `VERIFY_OK`; the exact output is in `verify_singular_output.txt`.

The infinite extension-degree point count is a *proof*, not an extrapolation from the two enumerated finite fields. It additionally invokes the standard odd-characteristic Weddle/Kummer correspondence and basic facts about finite-field Frobenius on Jacobians and the uniqueness of minimal smooth models of K3 surfaces. These external mathematical inputs are identified and cited in `RESULT.md`. No independent scientific audit is asserted.
