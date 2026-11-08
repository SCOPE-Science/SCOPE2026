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

# Verification scope

The proof is analytic and covers all real gains \(a>8\), all nonexceptional interior diagonal starting positions and all sufficiently small fixed separation thresholds. The parameterization of the alternating cycle, exact transverse eigenvalue, local summability estimates, positive finite-transient normal derivative and gain asymptotic are explained in `RESULT.md`. The bounded-error claim requires local hyperbolicity and does not apply at the parabolic boundary.

Run `python3 CHECK.py` in the extracted directory. The reproducibility program uses standard-library floating-point arithmetic only and checks six representative gains for cycle identities, eigenvalues and multiplier monotonicity, thirty representative first-exit comparisons, and four high-gain asymptotic ratios. These are demonstrations, not certificates of global uniqueness, infinite-quantifier correctness or publication novelty.

No independent mathematical audit was performed.
