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

# Reproducible verification

Run `python3 check.py` using Python 3 and no third-party packages. The checker exercises exact `fractions.Fraction` values for a two-step schedule with increasing steps, 480 random separable Huber trajectories, 375 random all-horizon first-order optimality checks, and scaled high-noise limits. It reports 6,248 completed checks. All random tests use a fixed seed.

The checker is an arithmetic and example verifier, not a computer proof for all dimensions or horizons. The analytic argument relies on a published smooth-convex interpolation certificate (Grimmer–Shen, 2026, Theorem 1.1 and Lemma 2.2), explicitly replacing each conditional second moment by its own ceiling, and proves the matching Huber construction and optimizer equations. No Lean or outside validation was performed.
