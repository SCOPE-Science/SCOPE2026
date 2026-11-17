---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The rates in assigned RESULT.md b20a4ed9f90dedc5ac8324088b71de68f3310062 match the explicitly described global clock with replacement. Detailed balance w_(k+1)/w_k=λ_k/μ_(k+1) with w_k=binom(S,k)^(1-q). Multiplying backward differences by w_k λ_k telescopes to exact finite mean; the prefix sum of inverse binomial powers is 1+O(1/S) uniformly for k<S. The outer sum localizes near S/2 and the standard central Gaussian integral of binom(S,k)^(q-1) supplies constant 2^(q+1)(2/pi)^((q-2)/2)/sqrt(q-1), power S^(-(q-2)/2), exponential 2^((q-1)S). Independently recomputed small exact first-passage sums for q=2,3 and S=10,20,40; ratios trend to 1. Such finite evidence is not a proof of the asymptotic.

## originality

PASS

Original source already establishes rates and invariant distribution, but no inspected sharp one-per-side fixed-count switching law with exact polynomial prefactor; best-of-knowledge originality remains qualified.

## value

PASS

The exact fixed-count metastable clock resolves the rate and leading constant for a motivated singular regime poorly represented by positive-zealot-fraction diffusion approximation. q-dependent polynomial correction and finite sum offer a concrete benchmark distinct from merely confirming exponential growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
