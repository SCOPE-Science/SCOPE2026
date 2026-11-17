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

# Reproducibility and scientific limits

The proof is analytical. The standalone Python program `check_tetra_endpoint.py` was executed from the package source with `numpy` and `sympy` and returned `SPHERE_TETRA_UPPER_VOLUME_ELLIPSOID_CHECKS_OK`.

Exact symbolic steps checked: determinant at the regular tetrahedron, all five first derivatives, the full normalized five-by-five Hessian, each positive leading principal minor, the determinant \(243/2048\), and the final coefficient \(128\sqrt3/405\). Independent Cartesian determinants were compared with the elementary reduced-coordinate formula at 150 randomly selected nondegenerate configurations. Fifty local perturbations were compared with the quadratic Taylor term.

The same samples gave mean volume \(0.119635815\) and mean squared volume \(0.024677362\), agreeing with the classical values \(4\pi/105\) and \(2/81\), respectively. Nine million uniform reduced-coordinate samples gave the following event counts (threshold, count, empirical probability, leading asymptotic probability):

- \(0.016\): 175, \(1.94444444\times10^{-5}\), \(1.77261953\times10^{-5}\).
- \(0.025\): 507, \(5.63333333\times10^{-5}\), \(5.40960551\times10^{-5}\).
- \(0.040\): 1607, \(1.78555556\times10^{-4}\), \(1.75172348\times10^{-4}\).
- \(0.060\): 4388, \(4.87555556\times10^{-4}\), \(4.82718229\times10^{-4}\).

These finite computations check arithmetic and corroborate the limiting law. They do not establish the asymptotic for all small thresholds, independence of the orientation sign in the limit, novelty, or independent mathematical certification. Those mathematical properties rely on the analytic compactness, Taylor-expansion and dominated-convergence argument.

Run: `python check_tetra_endpoint.py` after installing `requirements.txt`.
