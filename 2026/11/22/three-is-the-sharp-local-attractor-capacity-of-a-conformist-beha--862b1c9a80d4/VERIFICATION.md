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

The enclosed `verify.py` is a dependency-free CPython 3 program using exact `fractions.Fraction` arithmetic. It checks the right-hand-side equations at each of six claimed rational equilibria, their biological-domain constraints, both interior endemic roots, the sign of each reduced-feedback derivative, the determinant identity, and the cubic characteristic-polynomial Routh–Hurwitz conditions. The three attracting states have strictly positive Hurwitz margins; the three excluded states have positive real eigenvalues. All checks pass when run against the embedded source file.

The universal capacity proof is analytic: the reduced endemic feedback is strictly concave for positive private protection, mixed disease-free states are repelling or absent, and the two pure-adherence faces contribute at most one hyperbolic sink apiece. Neither sampling nor computer output is substituted for these general arguments.

No finite computation certifies all possible parameter choices by itself. The result does not provide an independent audit, global attraction certificate or epidemiological policy prediction.
