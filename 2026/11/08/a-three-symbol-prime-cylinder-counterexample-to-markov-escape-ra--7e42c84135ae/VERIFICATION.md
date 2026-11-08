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

# Verification of the counterexample

The enclosed `check.py` is standalone Python 3 code using only the standard library. It verifies the row-stochastic matrix, stationary vector, exact prime hole probabilities, determinant polynomials of both entry-deleted transition matrices, the strict endpoint signs and exact finite-horizon survival identities.

The decisive infinite-time proof is analytical: the exact stationary Markov law gives survivor probabilities \(\pi B^n\mathbf 1\) at all \(n\), and the primitive Perron--Frobenius theorem gives their exponential decay rate as \(-\log r(B)\). The explicit characteristic-polynomial sign tests separate the two positive radii around \(9/10\). No finite numerical experiment is treated as an infinite proof.

The theorem is confined to prime length-two cylinders in the given stationary full shift and does not assert independence, mechanical certification, or publication priority.
