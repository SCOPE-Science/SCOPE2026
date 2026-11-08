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

The claimed almost-sure count law is an analytic statement: conditional sampling hazards are sandwiched between \(c\delta^k\) and \(C\delta^k\), producing summable probability bounds for exceptional waiting times. Borel--Cantelli then gives \(\log\tau_n/n\to\log(1/\delta)\), which is inverted. The finite-size sampling frequencies follow by a bounded martingale-difference strong law. These arguments apply to any finite number of edges under the explicit assumptions.

The accompanying `CHECKER.py` uses only the Python standard library (`fractions`). It checks closed-form mean/variance identities on 99 combinations of rational \(\delta\), initial bad-edge weights and contact indices, and compares exact rational finite-horizon Markov-chain probabilities against independent geometric-convolution expressions in 38 additional checks. The run printed: `PASS: 137 exact rational identities and finite-horizon probabilities`.

These checks do not certify unbounded-time convergence by enumeration. The proof does not cover all-incompatible edge sets, vanishing initial edge weights, exogenous edge weights, or changing receptiveness without eventual stabilization. Independent audit has not been performed.
