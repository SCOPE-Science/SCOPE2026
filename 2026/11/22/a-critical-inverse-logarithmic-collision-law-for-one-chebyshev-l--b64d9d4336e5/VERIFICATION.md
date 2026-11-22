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

# Reproducibility and verification limits

The theorem is supported by the exact interpolation identities, explicit bulk-cardinal estimates, a two-term compact-offset asymptotic, global maximum localization, and a strictly concave scalar optimization in `RESULT.md`. Numerical checks are supplementary.

To run the standalone diagnostic from this directory: `python3 checker.py`. The observed success marker is `NEAR_COLLISION_CHEB_DIAGNOSTIC_OK 4563`. Its finite tests compare algebraically distinct finite-degree cardinal formulas, verify partitions of unity and selected optimizers, and cannot establish infinite limits or source priority.

The exact mathematical hypotheses are one moved bulk Chebyshev–Lobatto node and a vanishing angular gap to its immediate neighbor. No external expert or independent audit has been performed.
