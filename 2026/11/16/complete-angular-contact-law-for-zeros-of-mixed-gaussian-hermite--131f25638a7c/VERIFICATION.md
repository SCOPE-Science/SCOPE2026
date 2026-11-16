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

To reproduce the finite independent covariance check, run `python CHECK.py` in this directory with NumPy installed. The program builds the four Hermite-coordinate jets for the coherent two-window field and performs proper complex Gaussian conditioning by a Schur complement, then computes the squared imaginary Jacobian moment by Wick's theorem. It checks 444 angle/parameter combinations plus prior axis formulas and asymptotic cases, totaling 649 assertions. Expected final line: `DIRECTIONAL_CONTACT_CHECKS_PASSED 649`.

The infinite contact theorem itself is proved analytically in `RESULT.md` through a directional Kac–Rice Taylor limit and Gaussian moment calculation. Finite checks cannot establish that limit. Unproved extensions include arbitrary relative phase, joint small-noise/separation scaling, finite-distance pair density, and absolute publication priority. Independent audit has not been performed.
