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

# Verification record

The proof is in `RESULT.md`, with a self-contained script in `checks/regular_ideal_polygon.py`. Under Python 3 with the freely available `mpmath` numerical package, execute `python checks/regular_ideal_polygon.py` after extracting the artifact files together. A successful run prints `REGULAR_IDEAL_POLYGON_CHECKS_OK`.

The actual run passed all independent angular-density quadratures against the elementary antiderivative for seven values of polygon side count; a separate \(150000\)-sample area-uniform construction in the upper half-plane ideal triangle; numerical tests of the \(3/2\)-power transition; and convergence tests toward the many-side law through \(n=10000\). The sampling construction does not use the derived radial law. These tests are finite numerical evidence only and do not imply all-parameter or asymptotic completeness. Exact identities and analytic limiting arguments are presented in the proof. No independent mathematical audit has been performed.
