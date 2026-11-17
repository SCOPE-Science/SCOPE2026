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

The analytic proof in RESULT.md uses the beta marginal density at one-half and an integrable two-gap joint-corner estimate. Exact coefficient checks give \(p_{3,1}=1/4\), \(C_{3,1}=12/\pi\), \(p_{4,1}=1/2\), and \(C_{4,1}=6/\pi\).

The executable `check_tail.py` tests the exact beta formula against direct gamma-sampled Dirichlet polygons. Tested configurations are \((n,\alpha)=(3,1/2),(3,1),(4,1),(4,2)\), 1,800,000 unconditional simulations each. The observed ratios for \(x=120,240,480\), respectively, were:

- \((3,1/2)\): 0.9911, 0.9909, 0.9936.
- \((3,1)\): 1.0443, 1.0309, 1.0099.
- \((4,1)\): 1.0310, 1.0085, 1.0240.
- \((4,2)\): 1.0400, 1.0293, 1.0241.

The checker returned `DIRICHLET_TANGENT_PARETO_CHECKS_OK`. It uses NumPy and SciPy. Finite numerical checks alone cannot establish an infinite-tail limit or independently certify historical priority. The 2015 Xu and 2018 Wang–Xu full texts were not accessible; they remain material literature risks.

As an independent geometric check of the tangent-area identity, `check_geometry.py` constructs supporting halfplanes, computes their exact floating-point polygonal intersection using SciPy spatial halfspace and convex-hull algorithms, and compares its area against the tangent sum for random bounded polygons with 3, 4, 5 and 8 normals. The check completed with `GEOMETRIC_POLYGON_AREA_INDEPENDENT_OK`. Both programs are standalone and require only the dependencies in `requirements.txt`.
