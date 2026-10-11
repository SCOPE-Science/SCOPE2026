---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For the normalized geodesic-cap kernels used in the source sharpness argument, Proposition 4.3 gives the Hausdorff-Choquet alpha quasi-norm at the exact scale r^(2*alpha-(n-1)). The source's critical weak-type theorem gives a radius-independent upper bound for the weak operator norm of each normalized cap, while the indicator test used in Theorem 4.4 gives a radius-independent positive lower bound. Dividing these two-sided operator bounds by the quasi-norm therefore gives precisely the claimed two-sided power r^(-(2*alpha-(n-1))) in the supercritical regime. The argument is analytic and no finite experiment is needed.

## originality

FAIL

The quantitative power is already mechanically contained in Chen and Ji's own sharpness proof. Their Proposition 4.3 computes the cap quasi-norm as r^(2*alpha-(n-1)); their critical theorem supplies the uniform upper weak bound; and Theorem 4.4 uses the same normalized cap together with a fixed indicator test to obtain a radius-independent lower weak bound. The assigned result introduces a normalized quotient and divides these published estimates. Under the implication-based originality rule, that is a routine corollary of the primary source even though the source phrases its conclusion as a qualitative sharp threshold.

## value

FAIL

Quantifying a sharpness degeneration can be valuable in principle, but here the complete power law is obtained by directly dividing estimates already placed next to each other in the source's own cap sharpness argument. It adds no new estimate, boundary mechanism, or optimized constant, so it is too routine to clear the independent value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
