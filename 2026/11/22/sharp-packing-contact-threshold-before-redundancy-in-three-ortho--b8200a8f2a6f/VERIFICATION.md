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
# Verification notes

The entire claim is reconstructed analytically in `RESULT.md`: corner containment, strict concavity and supporting-plane/KKT certificate, branch threshold, nonredundancy witness, centering uniqueness, and one-sided derivatives. These checks do not involve any unproved numerical global optimization claim.

Run `python3 check_tricylinder_boxes.py` in the directory containing the complete files. The standard-library checker passed 2,507 deterministic sorted squared-radius triples, 80 independently generated feasible competitor boxes each, strict positivity/feasibility, KKT equalities, and three quadratic-onset benchmark values. Separately, 250 independent constrained SciPy numerical optimizations agreed to at most 1.23e-6 maximum relative coordinate error. The latter external check is not required to reproduce the standalone checker.

Unproved limits: no rotated-box optimum or higher-dimensional classification; no independent mathematical audit, and priority among unindexed older sources remains open. Earlier source dates without an independently verified exact day are not replaced by fabricated day dates.
