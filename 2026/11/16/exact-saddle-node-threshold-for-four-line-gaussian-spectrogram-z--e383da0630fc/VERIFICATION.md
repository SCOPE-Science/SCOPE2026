---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

From actual Gaussian four-line RESULT.md and CHECK.py: Gaussian integration reduces STFT zeros to entire exponential sum with covariance 2e^-δ²(cosh u+k cosh3u); Edelman–Kostlan density δ²/π d²log/du². Independently symbolic checked derivative cubic P_k(tanh²u), endpoint positivity P(0)>0,P(1)>0, discriminant -16384 k^3(3k−1)^6(27k²+18k−1), special k=1/3 positivity and double root z*=1/√3 at k*=(2√3−3)/9. Sign continuity then gives no other roots and one/two pairs of extrema. Central V_k(0)<0 throughout; matched derivative fold ∂kP=∂z²P yields z±=z*±√(2(k*−k))+O(k*−k). δ*≈0.608777 with angular frequency gap 2δ*. This concerns expected zero intensity, not individual realization peaks.

## originality

PASS

The new portion is the exact four-line modal root classification with a persistent central maximum, outer saddle-node threshold and square-root fold, not the general Gaussian analytic zero-intensity identity.

## value

PASS

The first symmetric four-atomic Gaussian spectral model has a mathematically distinct outer saddle-node with a persistent central expected-zero-density maximum, an algebraic sharp threshold and fold scaling, separating it from the three-line pitchfork mechanism. Exact mode topology is a motivated singularity/phase-diagram fact, not just a generic covariance differentiation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
