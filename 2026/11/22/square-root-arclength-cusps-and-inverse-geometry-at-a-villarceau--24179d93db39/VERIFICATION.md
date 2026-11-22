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

The exact boundary-length quadrature is derived in `RESULT.md` from the radial solutions of a torus–plane intersection. The proof separately factors the critical quartic, derives the weighted hyperbola local model and evaluates its signed arclength defect by complete elliptic integrals. It identifies the two node multiplicities, the angular normalization, the positivity of both coefficients, and the strict monotonic inverse function.

Run `python checks/torus_section_checker.py` from the extracted package root, with `numpy` and `scipy` installed. The packaged script passed 174 assertions concerning five independent torus aspect ratios, one-sided coefficient convergence, endpoint lengths, independently polygonized intersections and inverse-order comparisons. Finite-precision tests do not establish an infinite-range theorem, historic novelty or independent certification. The little-oh remainders are pointwise for fixed strictly positive radii with \(R>r\).
