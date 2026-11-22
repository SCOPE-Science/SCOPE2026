---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Angular samples rescaled by n converge as a point process to stationary rate λ=1/(2π) Poisson by multinomial rare-event convergence. Between nearest angular neighbors α=A/n and β=B/n, exact chord radius sin(α+β)/(sin α+sin β) gives n² radial deficit AB/2+O(n−2) on bounded gap sets. Uniform exponential empty-arc bounds and exponentially rare semicircle exclusion imply uniform integrability and convergence of first/second moments for any fixed site collection. Conditioning on the first right Poisson arrival yields a same-gap term e^(−u)(u+2)²/(4λ⁴) and a regenerated process integral [1−e^(−u)(1+u+u²/2)]/(4λ⁴); subtract product of means gives e^(−u)(3+3u+u²/2)/(4λ⁴), i.e. 4π⁴ times that polynomial, zero-lag variance 12π⁴. Exponential-product survival integral identifies the Bessel K1 inclusion law. Independent numerical integration for u=0,0.4,1,2.5,5 agrees; the asymptotic assertions rest on the Poisson/renewal proof.

## originality

PASS

The one-point modified-Bessel boundary window is ALREADY COVERED by a November 17 published theorem for arbitrary C³ positive-curvature curves and densities; it must not be attributed as original. That general theorem explicitly treats fixed distinct boundary sites and independence and excludes sites coalescing at n−1 angular scale. The surviving central finding is the exact covariance of the *same* coalescing Poisson-gap process at separation s/n and finite-dimensional joint radial law; no matched published exact two-point covariance was identified. This is a substantial mathematically different joint statement, not rescued merely by a certificate.

## value

PASS

The nontrivial explicit microscopic covariance distinguishes overlapping from separated local Poisson-chord neighborhoods and quantifies correlation range on the natural n−1 angular scale. It is independently useful for local random-polygon fluctuation analysis even though the one-point Bessel corollary is already published.

The dated certificate retains the supplied scientific assessment, sources and limitations.
