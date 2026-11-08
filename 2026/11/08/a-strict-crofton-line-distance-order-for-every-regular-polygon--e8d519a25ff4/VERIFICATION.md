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

# Reproducibility and scope

The exact probability and global monotonicity are derived analytically in `RESULT.md`. `verify.py` independently implements the angular support-function integral and performs rejection sampling from kinematic line coordinates, rather than substituting the closed-form result into itself. One execution returned:

`VERIFY_OK quadrature_pairs=36 accepted_rejection_lines=811820 ordered_n=3..100 radii=6`

The checker uses only Python's standard library. The finite quadratures and Monte Carlo experiments test normalization and boundary regimes but do not verify an infinity of side counts or prove any limit. The strict inequalities, contact differentiability, and continuum of radii follow from the analytic proof, not from the test counts. Independent audit has not been performed.
