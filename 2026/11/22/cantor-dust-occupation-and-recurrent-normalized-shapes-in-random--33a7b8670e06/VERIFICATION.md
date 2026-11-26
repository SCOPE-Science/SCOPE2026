---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The exact coordinate update at move r+1+jd uses thickness F_(d-1+r+jd) and sends length F_(jd+r) to F_((j+1)d+r). The generating function 1/(1-t-t^d) has a unique simple pole of least modulus, at 1/rho_d: equality in the triangle inequality at that modulus forces t to be positive. Thus the length ratio tends to lambda=rho_d^(-d)=1-1/rho_d in (0,1/2). Coupling to the stationary sum of the same innovations plus an independent past gives error e_(m+1) <= q e_m + |a_m-lambda| eventually for one q<1, hence uniformly vanishing error for all coordinates and phases. Each phase and each fixed complete-cycle window of the comparison is a factor of the ergodic iid shift; the coordinates at a fixed phase still use independent streams. A countable test family and finitely many phases give the stated almost-sure time occupation. Positive mass for neighborhoods of the support gives infinitely many completed cycles near each support point, and the uniform error excludes exterior cluster points at all phases. Cylinder separation and cylinder mass 2^(-dj) give the exact local dimension and support dimension. The geometric sum of squared weights gives variance (1-lambda)/(4(1+lambda)); independent later innovations yield the lag factor lambda^h and independent coordinates give zero cross-covariance. The planar case and failure of total-variation convergence follow from the same formulas and nonatomicity.

## originality

PASS

Supported for the model-specific pathwise occupation law and full recurrent cluster set of normalized rectangle positions, together with the complete-cycle window description. The one-time marginal and the fractal calculations are not credited as stand-alone advances: exact covering laws already encode finite-time marginals and the limiting dimension and covariance use standard methods. No compared result covers the time-occupation and all-cluster-points theorem for this nonhomogeneous cyclic model.

## value

PASS

Coordinatewise normalization is intrinsic to comparing the random displacement with the deterministic growth in each direction. The occupation and cluster theorems answer whether the actual growth keeps visiting every supported configuration and quantify that behavior, which neither a static marginal nor a fixed-target covering law decides. Exact dimension and fixed-lag dependence give useful scale and memory information for this path description, without claiming to solve the rescaled-curve problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
