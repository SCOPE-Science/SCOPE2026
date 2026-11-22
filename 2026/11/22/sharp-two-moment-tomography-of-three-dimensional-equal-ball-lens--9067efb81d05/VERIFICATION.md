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

## Scope

Exact moments for two independent area-uniform points on the entire surface of a three-dimensional intersection of congruent balls; radius positive and normalized half-separation in \([0,1)\).

## Reproduction

Run `python3 verify.py` with `sympy` and `numpy` installed. The checker integrates the polynomial axial-coordinate surface measure symbolically, reproduces all radial and coordinate covariance moments, and reconstructs \(\mathbb E D^2\), \(\mathbb E D^4\), and their ratio. It then simulates both actual boundary patches by independently sampling surface-area coordinates for five radius/separation pairs, checking ten two-sample moment comparisons. Expected output: `PASS: 17 symbolic identities / Monte Carlo comparisons; five independent parameter pairs`.

## Logical limits

The analytic integral identities, boundary decomposition, and elementary inverse/stability proof in RESULT.md establish the universal theorem. Finite simulations cannot prove universality or source priority. The bound on normalized separation is sharp with comparison to the sphere; no radius stability under statistical noise is asserted. No independent audit has been performed.
