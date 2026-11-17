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

# Reproduction and proof boundary

Execute `python verification.py` with a standard Python 3 interpreter. It uses only `fractions.Fraction` and small exact integer/rational matrix operations; no numerical tolerance, network access, or untracked dependency is needed. The observed output is:

```text
VERIFY_OK exact_rational_projector_identities= 5 critical_center=1 supercritical_growth=7/25
FINITE_CHECK_ONLY: global convergence and universal sharpness are analytic.
```

The exact-rational checks assert projector idempotence, the symmetrized-reflector identity, a planar threshold rotation, a planar expanding example, and a rank-two projector example in three coordinates. They are consistency checks for the displayed formulas, not proof of the universal statement. The proof is the dimension-free matrix expansion plus the strong-convexity energy estimate, followed by the complete planar rotating-projector counterexamples for equality and the supercritical range.

There is no numerical approximation in the proof. The dynamical conclusion is conditional on global orthogonal separability and a uniform projector-error bound; it is not evidence for any nonseparable potential, discrete integration, or coupled frame-tracking flow. Independent mathematical validation has not been performed.
