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

# Verification performed

The exact two-input bound follows from the polar-rotation formula, full trace/skew sign extremization, one-variable derivative optimization, convex-segment integration and an explicit accretive one-sided witness. The radical satisfies \(C_*^2=(71+17\sqrt{17})/108\); the critical skew ratio is the positive solution of \(2t^2+3t-1=0\). These steps establish the assertion for every real admissible matrix and every margin \(\mu>0\).

Run `python3 check_polar.py` with Python 3 and no dependencies to reproduce supplementary algebra, scalar-grid, randomized two-input inequality, and boundary-difference checks. The checker prints `PASS: 115037 supplementary assertions; C=1.142985028074638; t*=0.280776406404415` when successful. This numerical evidence is not an exhaustive enumeration or an independent audit. Higher-dimensional and rank-deficient extensions are not established. Historical-priority risk remains for unknown equivalent polar-factor conditioning formulas.
