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

# Reproducibility and verification

The source proof is `RESULT.md`, with all hypotheses and normalized probability measures explicit. Run `python3 check_hyperbolic_annulus.py` with Python 3.9+ and no third-party dependencies. The standalone script contains three independent tests: (i) closed inverse-trigonometric expression; (ii) composite-Simpson integration of the conditional-angle integral using the hyperbolic area density; (iii) direct hyperboloid-model geodesic segment minimum-distance testing against the forbidden central disk, using no tangent-angle condition. The deterministic random seed and sample counts are recorded in the checker.

During preparation, the checker passed for five annuli with inner/outer radii \((0.2,0.8)\), \((0.5,1.5)\), \((1,2)\), \((0.3,7)\), \((2,2.0003)\); it also passed the strict monotonicity sequence, large-radius limit, thin-annulus leading equivalent and small-curvature Euclidean-limit checks. The final line was `HYPERBOLIC_ANNULUS_EXACT_AND_INDEPENDENT_SEGMENT_TESTS_OK`. Simulations and quadrature do not establish the theorem for untested radii; the analytic proof supplies those assertions. No external or independent scientific validation has been performed.
