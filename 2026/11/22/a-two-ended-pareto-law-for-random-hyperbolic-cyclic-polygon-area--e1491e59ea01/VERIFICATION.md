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

# Verification of the geometric and probability calculations

Run `python check_cyclic_area_tail.py` using Python 3 and NumPy. The script is a standalone artifact and does not depend on any other row, file path, external data, or network service. It printed `HYPERBOLIC_CYCLIC_PARETO_CHECK_OK (1310 deterministic checks)` when run from this package's actual source path.

The checks compare two algebraically different area implementations: an oriented geodesic-edge `atan2` formula and a Gauss--Bonnet interior-angle formula. They test irregular gap patterns for \(n=3,4,5,7\) and radii \(R=0.3,1.2,3.1,9\), the exact maximizing regular configuration, the \(e^R\)-scaled limit at larger radii, and the positive quadratic Hessian at regular spacings. They also simulate large Dirichlet samples to check the inverse-linear limiting upper tail and asymptotically uniform rare shortest-gap mark.

These are finite numerical consistency diagnostics, not exhaustive enumeration and not proofs of convergence, independence, sharp constants, or novelty. The analytic proofs of those statements are given in `RESULT.md`. Tests do not imply uniform accuracy in radius or sampling size. No independent audit has been performed.
