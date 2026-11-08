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

The included `check_area_loss.py` has only ordinary finite computational checks, all performed against the packaged program. It computes a rational rectangular boundary configuration and verifies its exact corner-triangle deficit \(7/8\). The transitive-pair permutation enumeration agrees with the moment–cumulant recursion for orders 1–4, giving \(1,3,26,426\). Direct convex-hull simulations with fixed random seed and \(N=800\) on a nonsymmetric four-vertex convex polygon give scaled mean deficit \(140.390\) compared with the analytic limit \(135.976\); the exact local-triangle decomposition has numerical maximum discrepancy \(1.6\times10^{-15}\). The exponential-product Laplace integral was checked at three positive parameters, as were 1520 admissible random turning-angle vectors and exceptional equality families.

To replay from the provided files: `python check_area_loss.py` with Python 3.9+, NumPy and SciPy installed. A successful replay prints `CHECK_OK` with the checks above.

The asymptotic quantifier over sample size, every integer cumulant, and all convex polygons is established analytically in RESULT.md. Finite simulations do not prove convergence, historical priority, independence of review, or finite-sample inference. No independent audit has been performed.
