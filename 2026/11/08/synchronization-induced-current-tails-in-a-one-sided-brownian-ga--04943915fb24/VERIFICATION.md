---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

C PASS. Spatial Brownian crossing integral equals sqrt(Du/pi) by Gaussian integration, and independent Poisson marking yields the annealed Poisson current. Conditioning on the shared backward age, including atom e^{-rt} at t and exponential density below it, gives Poisson(c sqrt(A_t)); mixing yields same mean and strict convex-order inflation via positive Poisson second differences. Endpoint Laplace expansion gives finite-time ratio 1+2rt/q+O(q^-2), and stationary Gamma norm central-limit/concentration yields the *full* Rayleigh-mixed mass prefactor 1/sqrt(2)*exp(lambda²/8) with exp[-lambda sqrt(q/2)]. Stirling proves the 1 versus 1/2 negative-log exponents; density scaling follows conditional Chebyshev. Numerical quadrature is supportive only; all asymptotics fixed positive rates.

## originality

PASS

O PASS (best of knowledge). Inspected primary and published theorem statements and compared their precise objects, parameter domains and implications; none of the checked wider source theorems directly implies this full final claim. Source-level checks and narrower known deductions are credited; residual priority risk preserved.

## value

PASS

V PASS. Changing independent to shared clocks while keeping one-point marginals fixed is a natural dependence experiment in transport and resetting. An exact finite-to-infinite-time rare-current exponent transition and sharp prefactors are mathematically specific, useful results, not solely a generic Jensen inequality or unmotivated finite cutoff. The model-specific density-scale non-self-averaging supplies additional content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
