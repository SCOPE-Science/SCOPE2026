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

# Reproducibility and verification

The complete analytic proof is in `RESULT.md`, Steps 1–5. Run the included standard-library script using `python3 verify_founder_quorum.py` from the directory containing that file. It performs direct numerical checks of the beta-MGF defining equation, Poisson quorum probabilities, global superiority to interior grid policies, monotonicity in budget and female quorum, and both asymptotic regimes.

The diagnostic completed with `PASS: 13569 diagnostic assertions` and returned the independently reconstructed values for the \(r=2,n=4\) and \(r=3,n=10\) cases quoted in the theorem. Large-intensity probability comparisons are performed on the logarithmic scale to prevent floating-point underflow; finite-precision estimates are illustrations only. The uniqueness and ordering statements for all real \(n>0\) and all integer \(r\ge1\) follow from the positive beta-integral MGF, its tilted variance and stochastic order, and the derivative-sign argument in the proof, not from the finite diagnostic run.

No external independent scientific review or validation has been performed. The model does not prove long-term reintroduction survival or stability under empirical measurement error.
