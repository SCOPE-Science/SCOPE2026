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

# Verification and limitations

The exact Jacobian identity is checked symbolically with SymPy. The same standalone checker constructs inverse points from the closed quadratic formula for four fixed parameter/target cases, confirms forward residuals to floating-point precision, and computes finite-annulus inverse-Jacobian sums at three annulus widths. The normalized densities approach the theoretical values for integer, half-integer and nonresonant phase gains; a target beyond the low-gain phase range has no sheets. The tests were executed after extraction from the final JSONL embedding. Exact statements on infinitely many inverse branches, normalized measures and strong total-variation convergence rest on the written proof, not these finite diagnostics.

The analysis makes no claim about forward-invariant stationary laws, long-term randomness, cryptographic quality or independence verified by another assessor. Independent audit has not been performed.
