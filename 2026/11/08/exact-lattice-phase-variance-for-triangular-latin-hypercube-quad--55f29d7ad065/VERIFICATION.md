---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Let a_ij be each cell success probability, T their sum, A the sum of their squares, and S the sum of squared row totals (equal to the corresponding column sum by symmetry). For the number M of successful draws, E M=T/n and the non-diagonal term in E M² is (T²-2S+A)/(n(n-1)), since only pairs in distinct rows and columns may be jointly selected. With ns=m+θ, cells have the full/partial diagonal probabilities 1, 1-(1-θ)²/2, θ²/2. Integrating the row directly gives nonzero totals j+θ+1/2 for 0<=j<m, and θ²/2 if the extra row exists. This gives the stated A and S, including m=0 and m=n (the absent extra term at m=n is zero). Exact expansion of Var(M)/n² gives (1). Reflection preserves the sampling law and almost surely complements the indicator; the expectation is triangle area. With B=s(6θ²(1-θ)²-1)/12 the exact centered residual is n(V+B)/(n-1)+P(θ)/(12(n-1)), with bounded polynomials on the whole parameter square. This gives the uniform remainder, diagonal and endpoint cases, and the dense irrational or periodic rational limit sets, with the stated parity maxima.

## originality

PASS

Best of current knowledge, the exact jittered-LHS finite-offset formula and the position and amplitude of the phase in the LHS expansion are a distinct result. Related indexed work has the same quartic phase and arithmetic classification for an independent grid, and general LHS variance machinery is known. Neither is credited as new here; the two estimators do not share their exact variance laws.

## value

PASS

A diagonal threshold is a standard discontinuous benchmark whose two-dimensional interaction cannot be read off from one-dimensional stratum means. The all-offset, all-n variance is usable for exact calibration. It explains why increasing resolution changes variance smoothly to two orders before arithmetic dependence appears, and quantifies every possible third-order residual rather than only giving a convergence rate. This is specific to the Latin-hypercube estimator, not a new claim about the familiar quartic in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
