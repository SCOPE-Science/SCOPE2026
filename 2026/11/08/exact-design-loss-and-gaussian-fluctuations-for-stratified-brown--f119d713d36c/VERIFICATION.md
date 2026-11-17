---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Given Brownian observations, each interior interval is a Brownian bridge with integrated variance h^3/12 and the terminal interval is a free Brownian increment with integrated variance h^3/3. The exact gap functional follows. Strict convexity with weights 1,...,1,4 yields unique gaps 2/(2n+1) and 1/(2n+1), including n=1 and all equal strata. Independent exact polynomial integration yields E W=3/2, E W^2=127/28, E W_iW_{i+1}=449/336, giving long-run variance 11/24 and CLT 11/3456 after division by 144. Bounded 1-dependence supplies CLT and even/odd strong laws. These identities were independently recomputed symbolically.

## originality

PASS

General Gaussian process quadrature and Brownian bridge theory give ingredients but not this full finite-budget mean, unique asymmetric anchored optimum and location CLT coefficient. The related published stationary OU result has the same 3/2 and 1-dependent asymptotic constants after local Brownian scaling but has two unknown terminal boundary conditions and different finite optimum; it does not imply the exact anchored Brownian formula. Stronger Gauss–Markov sampling literature not exhaustively inspected.

## value

PASS

Quantifies exact expected loss and its fluctuations when replacing optimal Brownian-kernel quadrature nodes with simple randomized stratification. Distinguishes finite-design effects from conditional path uncertainty and gives a reusable explicit design coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
