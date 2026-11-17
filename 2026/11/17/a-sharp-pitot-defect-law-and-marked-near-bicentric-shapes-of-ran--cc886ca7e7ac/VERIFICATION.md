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

## Reproducible checks

Run `python3 artifacts/check_bicentric.py` with Python 3 and no third-party packages. The checker uses a fixed random seed. It compares the exact chord-sum formula with the single sine normal form on 16,000 independent Dirichlet gap samples; checks that each analytic bicentric root is feasible, and that all sampled configurations obey the proven sharp transverse inequalities. It evaluates the explicit diamond integral by deterministic midpoint quadrature, then compares the exact clipped probability integral against independent Monte Carlo at two thresholds. At the recorded check, the script printed `CYCLIC_BICENTRIC_COORDINATE_AND_TAIL_CHECKS_OK` and yielded a coefficient close to the high-precision reference `0.8185431011367532`.

The proof of the all-threshold formula and of total-variation convergence is analytic and does not depend on Monte Carlo, quadrature, or a software convergence test. The numerical checks cover only finitely many samples and integral grid points.

## Source comparison and limits

The deterministic tangency characterization is classical and expressly not claimed novel. The novelty assessment concerns the near-zero distribution of the signed Pitot defect, its exact geometry-adapted normal coordinate with sharp universal transverse bounds, and the marked conditional shape law. The closest literature and remaining historical-priority risks are documented in `REVIEW.md` and `AUDIT.json`. There is no independent audit or finite-sample statistical performance guarantee.
