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

# Arithmetic checks and limitations

Run `python3 verify_osculation.py` in this directory using standard Python 3. It constructs exact finite fields with \(q^6\) elements for \(q=2,3,4,5\) (irreducible moduli are explicitly recorded in the code), iterates all nonzero parameters, checks the norm–trace condition and projective fixed-point relation, confirms that each resulting point lies on the cyclic plane curve, and computes minimal Frobenius periods. The recorded successful output is in `verification_output.txt` and ends with `OSCULATING_VERIFY_OK`.

The all-prime-power result is mathematical, not computational extrapolation. Its necessary proof steps are the tangent restriction identity; the residual map \(R=\sigma\Phi^2\); Hilbert-90 normalization of its fixed points; surjectivity and sizes of the finite-field norm and trace fibers; and the conic/line count in the cubic-field twisted projective plane. None of those infinite-quantifier steps is established merely by finite enumeration. The self-review is not an independent audit.
