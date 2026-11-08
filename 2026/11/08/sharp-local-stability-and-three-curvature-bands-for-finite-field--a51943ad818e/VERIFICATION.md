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

`artifacts/verify.py` executes using Python 3 and SymPy, declared in `requirements.txt`. From the same directory as `RESULT.md`, run `python3 artifacts/verify.py`. The recorded replay checks 36 complete modular collision-fiber identities, 36 exact nonnegative-deficit comparisons, and full symbolic Taylor-polynomial identities at three field sizes. It also approaches the computed least local curvature along an explicit antipodally even amplitude direction. Its success line is:

`CUBIC_CURVE_STABILITY_VERIFY_PASS collision 36 deficit 36 hessian 3`

The finite replay covers prime fields of orders five, seven, and eleven. It does not exhaust all finite fields, bound any unspecified higher-order remainder uniformly in field size, or substitute for the universal collision proof in `RESULT.md`.

The proof's critical steps are: additive-character orthogonality; the cubic pair-sum factorization away from zero; exact quartic completion; the three-block real/imaginary even/odd Hessian decomposition; and a compact embedded-torus tubular-neighborhood argument. The full result is a deterministic self-review, not an independently verified theorem.
