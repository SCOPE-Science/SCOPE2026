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

The proof uses the exact Euclidean squared-distance inequality, cone-volume homogeneity, a beta integral, coarea disintegration on the strictly positive linear slice, and an implicit-function expansion uniform on a compact slice. The all-dimensional conditional Dirichlet law follows from the homogeneous radial density and has a total-variation (not only weak) local form for the endpoint pair. The normalized distance deficit is \(\operatorname{Beta}(2d,1)\), not its complement. The second coefficient is positive because the transverse quadratic moment is strictly positive in dimensions at least two.

Run the standalone checker with `python check_diameter_cone.py` after installing packages listed in `requirements.txt`. It compares exact rectangle quadrature with the two-term coefficient, performs independent cone-simplex importance sampling in dimensions two through four, and checks two triangles with distinct diametral vertex multiplicities. An actual successful execution produced the marker `POLYTOPE_DIAMETRAL_CONE_TWO_TERM_DIRICHLET_CHECKS_OK`. Numerical quadrature, randomized sampling, and finite-dimensional examples cannot prove the uniform analytic remainder, the all-polytope result, or historical novelty; these claims rely on the mathematics in `RESULT.md`.

No external independent audit has been performed. The prior literature is not claimed to have been searched exhaustively. In particular, the 2016 arbitrary-polygon distance-distribution report and the 2002 sample-diameter paper were not completely inspected and could cover part of the marginal problem. A mathematically stronger general localization result may exist under different terminology.
