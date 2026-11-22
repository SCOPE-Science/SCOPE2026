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

# Reproducibility

Run `python3 verify.py` (Python 3.10 or later, standard library only). The independent Fourier representation is evaluated at nine time values and 36 time/arc pairs, using the positive-tail bound stated in RESULT.md. The script also checks the critical hyperbolic equation, stationary arc roots, and asymptotic constants.

These checks do not by themselves establish universal sharpness: that rests on the measure-coupling proof, the exact periodic Green kernel, and strict monotonicity of the hyperbolic root function. No computer-assisted infinite certification or independent mathematical validation is claimed.
