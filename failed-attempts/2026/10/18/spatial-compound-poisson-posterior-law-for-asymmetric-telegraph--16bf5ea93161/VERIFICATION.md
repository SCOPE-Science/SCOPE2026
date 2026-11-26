---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The two-state Fourier resolvent has numerator q+2b−ikd/2 and denominator K(ζ₊−ik)(ζ₋+ik). Both real spatial roots are positive since their product is q(q+2b)/K and their sum is HΔ/K. Evaluating the numerator at ik=ζ₊ and ik=−ζ₋, and dividing by HΔ, gives the displayed A₊ and A₋, respectively. The joint subprobability density therefore gives the posterior transform by division at s=0, with a positive continuous version on each open ray. The Bessel transforms normalize the base law, including its zero atom. Differentiating the spatial root gives 1/c_σ plus H/(2K) times the transform of ηI₁(ηt); integrating in q gives the claimed nonnegative jump measure common to both signs. It is bounded near zero and exponentially integrable at infinity since a+b>η, and its total mass is H(a+b−Δ(a))/(2K). The finite positive jump rate and independent positive drift increment give the stated atom and strict stochastic order, and derivatives at zero give both affine moments. The formulas include u=v, do not require a convention at x=0, and apply to all strictly positive rates and speeds in the finding. The quadrature script was inspected, not executed; no assertion requires numerical extrapolation.

## originality

FAIL

The explicit posterior factorization is not printed as such in the inspected predecessors, but its claimed new spatial mechanism and explicit laws are direct corollaries of Ratanov's stronger asymmetric first-passage and fixed-time kernels together with the strong Markov property and exponential tilting. This is concrete prior implication, not a failure based on a possible unnamed Wiener–Hopf theorem or an unsuccessful search.

## value

PASS

As an inference formulation the result is useful: it gives the full ordering and an explicit coupling of posterior times at all distances on each ray, which a fixed-time density alone does not make transparent. The common jump kernel with different ballistic drifts cleanly separates kinematic asymmetry from uncertainty in elapsed time. This utility does not make an already implied law original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
