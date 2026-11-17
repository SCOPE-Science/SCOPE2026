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

# Computational and analytical verification

Running `python check_random_great_circles.py` with NumPy and SymPy tests the following independently of the main algebraic derivation:

1. Directly constructs the three pairwise great-circle intersection vertices of each of eight chambers, and evaluates their areas via the spherical solid-angle identity. On 80 independent normal triples, all chamber areas agree with the signed arcsine formula to within \(2\times10^{-10}\), as do the exact area range and total surface area \(4\pi\).
2. Symbolically integrates the ordered positive polytope octant and confirms \(\operatorname{vol}(\mathcal B)=2\) and \(\int_{\mathcal B}\sum_{i<j}u_i^2u_j^2\,du=7/120\). The leading and seventh-order coefficients are evaluated exactly.
3. Compares 2,500,000 random triples with the two-term small-spread probability. Observed probabilities at \(\varepsilon=0.30,0.45,0.65\) were respectively 0.0005260, 0.0017996, 0.0054936, compared with expansions 0.0005371519, 0.0018129420, 0.0054643797. Each standardized deviation is under 0.8.
4. Integrates the exact Gram density on a fundamental ordered cone by 32-point-per-coordinate Gauss–Legendre quadrature. At thresholds 0.20, 0.50 and 1.00 the exact probabilities are approximately 0.0001591551761, 0.0024869412483, and 0.0199145281395. The discrepancies from the two-term expansion are positive, respectively about \(9.20\times10^{-13}\), \(3.60\times10^{-9}\), and \(2.03\times10^{-6}\), consistent with a ninth-order remainder. The quadrature is diagnostic, not interval-certified.

Expected standard-output markers: `DIRECT_SPHERICAL_TRIANGLE_GEOMETRY_OK`, `EXACT_ASYMPTOTIC_COEFFICIENTS_OK`, `RARE_EVENT_MONTE_CARLO_OK`, `SEVENTH_ORDER_QUADRATURE_DIAGNOSTICS_OK`.

**Limits.** Simulation and numerical quadrature are finite checks, not independent mathematical proof. The analytic derivation supplies the limiting theorem. Historical-priority review is provisional.
