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

The analytic argument is the four-step proof in `RESULT.md`; its critical premises are independence, local continuity and global boundedness of the first-column density, and a finite dimension-matched moment of the second vector. The localization inequality justifies dominated convergence. The geometric integral uses an exact right orthogonal transformation followed by a polar-volume calculation.

The standalone `verify.py` checks exact-rational Gaussian special cases, evaluates the general volume integral, and performs seeded rare-event importance sampling for Gaussian, uniform-cube and Laplace inputs. It is an empirical consistency check, not a proof of the limit or a full verification for all distributions.

Limits: no full algorithmic stopping-time analysis, no uniformity in growing sketch dimension, no structured correlated sketches or floating-point effects. Independent audit is not performed.
