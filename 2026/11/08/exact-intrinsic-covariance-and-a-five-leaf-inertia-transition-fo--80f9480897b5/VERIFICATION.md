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

The proof is exact for every integer \(q\ge3\) and relies on the invertible fiber parametrization and elementary uniform-cube moments. The following supplemental checks were performed by executing `python verify_k2q.py` with NumPy and SciPy.

For \(q=2,3,4\), the checker separately enumerates images of all edge-coefficient cube corners, computes the convex hull in an orthonormal basis of the intrinsic hyperplane, and integrates the quadratic moment over oriented simplicial hull cones. The distinct projected generator-box corner images numbered 15, 54 and 189 (including non-extreme images); the corresponding triangulated boundary simplex counts were 24, 232 and 2758. Intrinsic volume relative errors were less than \(6\cdot10^{-11}\), and maximal covariance-coordinate errors less than \(2\cdot10^{-11}\) against the closed formulas.

For \(q=5,8,15\), separate fixed-seed rejection sampling uses the independently described fiber volume weight and 200000 accepted samples at each size. The largest diagonal parameter-moment discrepancy across these sizes was below 0.0015, and the largest fiber-coordinate second-moment discrepancy below 0.005. These stochastic checks test implementation and normalization; their outputs are not proof of the infinite-dimensional family.

The checker printed the success marker `K2Q_VOLUME_COVARIANCE_CHECKS_PASSED`. All necessary source for reproducing these checks is included. An independent mathematical audit has not been performed.
